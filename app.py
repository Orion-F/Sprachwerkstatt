import streamlit as st
from deep_translator import GoogleTranslator
from difflib import SequenceMatcher

translator = GoogleTranslator()

def main():
    st.set_page_config(
        page_title="Sprachwerkstatt",
        page_icon="✍️",
    )

    st.title("Sprachwerkstatt")
    st.subheader("Übe und lerne verschiedene Sprachen")

    # Texteingabe auf Deutsch
    german_text = st.text_area("Schreibe einen Satz auf Deutsch:")

    # Texteingabe auf Französisch
    french_text = st.text_area("Versuche denselben Satz auf Französisch zu schreiben:")

    # Wenn der Nutzer beide Texteingaben abgeschlossen hat
    if st.button("Vergleichen und Übersetzen"):
        if german_text.strip() and french_text.strip():
            try:
                # Übersetze den deutschen Text ins Französische
                translator = GoogleTranslator(source='de', target='fr')
                translated_text = translator.translate(german_text)
                
                # Zeige die Übersetzung und den Vergleich an (in einer Zeile)
                st.markdown(f"<div style='display: flex; align-items: center;'>"
                            f"<span style='color:blue; margin-right: 10px;'><strong>Übersetzung von Deutsch nach Französisch:</strong> {translated_text}</span>"
                            f"<span style='color:green; margin-left: 10px;'><strong>Dein französischer Text:</strong> {french_text}</span>"
                            f"</div>", unsafe_allow_html=True)
                
                # Vergleich der Texte
                similarity_ratio = SequenceMatcher(None, translated_text.lower().strip(), french_text.lower().strip()).ratio()
                if similarity_ratio == 1.0:
                    st.success("Gut gemacht! Deine Übersetzung stimmt überein.")
                elif similarity_ratio > 0.7:
                    st.info(f"Die Texte sind zu {similarity_ratio * 100:.1f}% ähnlich. Gute Arbeit, aber es gibt noch Unterschiede.")
                else:
                    st.error(f"Die Texte stimmen nur zu {similarity_ratio * 100:.1f}% überein. Schau dir die Übersetzung an und versuche es noch einmal.")
            except Exception as e:
                st.error(f"Fehler bei der Übersetzung: {str(e)}")
        else:
            st.warning("Bitte gib sowohl den deutschen als auch den französischen Text ein.")

if __name__ == "__main__":
    main()
