import re
import unicodedata
import ollama


class OllamaChat:
    """Ollama wrapper with casual conversation + bounded local-reference context."""

    def __init__(
        self,
        model_name="qwen3-vl:2b-instruct",
        system_prompt=(
            "You are a friendly Color Science Agent. "
            "You may respond naturally to greetings and ordinary social conversation. "
            "The app already displayed an introductory welcome message. "
            "Never repeat the introduction unless the user specifically asks who you are. "
            "Respond to the latest user message and continue the conversation. "
            "For technical or factual Color Science questions, use ONLY the LOCAL "
            "REFERENCE CONTEXT supplied by the application for that question."
        ),
        max_history_messages=6,
        num_ctx=8192,
    ):
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.max_history_messages = max(2, int(max_history_messages))
        self.num_ctx = int(num_ctx)
        self.messages = [{"role": "system", "content": self.system_prompt}]

    @staticmethod
    def _normalize(text):
        text = unicodedata.normalize("NFKD", text or "")
        text = "".join(ch for ch in text if not unicodedata.combining(ch))
        return re.sub(r"\s+", " ", text.lower()).strip()

    @classmethod
    def is_casual_message(cls, text):
        q = cls._normalize(text)
        technical_terms = (
            "color", "colour", "color science", "colour science",
            "sci", "sce", "specular included", "specular excluded",
            "specular component included", "specular component excluded",
            "delta e", "cie", "lab", "l*a*b", "cielab", "xyz",
            "rgb", "cmyk", "spectral", "spectrum", "spectra",
            "reflectance", "transmittance", "measurement", "measurements",
            "target", "targets", "sample", "samples", "chromatic",
            "chromaticity", "illuminant", "observer", "wavelength",
            "metamer", "metamerism", "hue", "chroma", "lightness",
            "luminance", "color space", "colour space", "color difference",
            "colour difference", "gloss", "whiteness", "yellowness",
            "opacity", "density", "spectrophotometer", "colorimeter",
            "colorimetry", "colorimetric", "white point", "black point",
            "d50", "d55", "d65", "d75", "a illuminant",
            "2 degree observer", "10 degree observer", "cie 1931",
            "cie 1964", "cie 1976", "delta l", "delta a", "delta b",
            "de2000", "de94", "de76",
        )
        return not any(term in q for term in technical_terms)

    _is_casual_message = is_casual_message

    def _history_for_request(self):
        recent = self.messages[1:][-self.max_history_messages:]
        return [self.messages[0], *recent]

    def user_message(self, user_input, extra_context="", images=None):
        extra_context = (extra_context or "").strip()[:9000]
        casual = self.is_casual_message(user_input)

        if casual:
            request_content = f"""
MODE: CASUAL CONVERSATION

Respond naturally and warmly.
Continue the conversation rather than introducing yourself again.
Your name is Color Science Agent.
Do not require a local reference and do not add a Source line.

USER MESSAGE:
{user_input}
"""
        else:
            request_content = f"""
MODE: LOCAL-REFERENCE TECHNICAL ANSWER

RULES:
- Use ONLY the LOCAL REFERENCE CONTEXT below for technical/factual claims.
- Do NOT use general knowledge, memory, assumptions, or outside information.
- If the answer is not supported by the supplied context, say exactly:
  I could not find that information in the local reference documents.
- Do NOT invent a filename.
- Do NOT add a Source or Sources line. The application adds it.

LOCAL REFERENCE CONTEXT:
{extra_context if extra_context else "[No relevant local reference text was retrieved.]"}

USER QUESTION:
{user_input}
"""

        user_message = {"role": "user", "content": request_content}
        if images:
            user_message["images"] = [str(path) for path in images]

        request_messages = self._history_for_request() + [user_message]

        stream = ollama.chat(
            model=self.model_name,
            messages=request_messages,
            stream=True,
            options={"num_ctx": self.num_ctx},
        )

        full_response = ""
        for chunk in stream:
            content = chunk["message"]["content"]
            if content:
                full_response += content
                yield content

        self.messages.append({"role": "user", "content": user_input})
        self.messages.append({"role": "assistant", "content": full_response})
        self.messages = [
            self.messages[0],
            *self.messages[1:][-self.max_history_messages:],
        ]

    def new_session(self):
        self.messages = [{"role": "system", "content": self.system_prompt}]


ollamachat = OllamaChat
