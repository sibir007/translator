import nltk
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
nltk.download('punkt_tab')

def ntlk_sentences(text):
    return tokenizer.tokenize(text)

def words(text):

    t = nltk.word_tokenize(text)
    return t

if __name__ == '__main__':
    # t = words()
    text = """
    A new window should open, showing the NLTK Downloader. Click on the File menu and select Change Download Directory. For central installation, set this to C:\nltk_data (Windows), /usr/local/share/nltk_data (Mac), or /usr/share/nltk_data (Unix). Next, select the packages or collections you want to download.

If you did not install the data to one of the above central locations, you will need to set the NLTK_DATA environment variable to specify the location of the data. (On a Windows machine, right click on “My Computer” then select Properties > Advanced > Environment Variables > User Variables > New...)

Test that the data has been installed as follows. (This assumes you downloaded the Brown Corpus):
"""
    s = """Зна́ки препина́ния — элементы письменности, выполняющие вспомогательные функции, например: разделение и выделение смысловых отрезков текста, предложений, словосочетаний, слов, частей слова; указание на грамматические и логические отношения между словами, на коммуникативный тип предложения, его эмоциональную окраску, степень законченности.

Благодаря знакам препинания, синтаксически оформляющим текст, читателям становится легче воспринимать и понимать его, а при произнесении текста вслух — интонационно оформить его (в частности, подчеркнуть смысловые паузы, логические ударения).

В письме А. П. Чехова начинающему писателю Н. А. Хлопову отмечается роль знаков препинания в тексте, в частности обращено внимание на переизбыток одних из них (многоточий) и дефицит других (точек) в дебютном рассказе адресата[1][2]:"""
 
 
    t = ntlk_sentences(s)
    
    print(t)