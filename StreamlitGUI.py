import streamlit as st
import trigram as aa

def typingSuggestions(inputText): 
    inputText = aa.prepText(inputText)
    inputText = tuple(inputText)
    # print(aa.bis['mental'])
    try:
        if len(inputText) == 2:
            suggestions = aa.tris[inputText]
            return aa.sentenceSuggestion(inputText, suggestions)
        elif len(inputText) == 1:
            suggestions = aa.bis[inputText[0]]
            return aa.sentenceSuggestion(inputText, suggestions)
        elif len(inputText) > 2:
            inputTextT = inputText[-2:]
            suggestions = aa.tris[inputTextT]
            return aa.sentenceSuggestion(inputText, suggestions)
        else:
            return []
    except KeyError:
        pass


sentence = '<center><h1><span style="color:#113758">Potato</span> <span style="color:#ee202b">Health</span></h1></center>'
st.markdown(sentence, unsafe_allow_html=True)
# st.title("Mental Health Search Engine")
path = "Images/potato.png"

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(path, width=250)

title = st.text_input("Start Searching..")

suggestions = typingSuggestions(title)

if suggestions:
    # st.markdown("Mental Health Search")
    try:
        for i in range(15):
            st.write(suggestions[i])
    except IndexError:
        pass
    # to show a drop list and navigate through:
    #         selected_sentence_index = st.selectbox("Mental Health Search", options=suggestions)
    #         st.write(selected_sentence_index)
