import ply.yacc as yacc
from pyarabic import *
from flask import Flask, render_template, request, redirect, url_for, session,jsonify
import speech_recognition as sr


from lex import tokens
import re
global resultParser;global positionParserError

positionLexerError,positionParserError = dict(),dict()



def p_quote(p):
    ''' quote : quote1
              | quote2
              | quote3
              | quote4
              | quote5
              | quote6
              | quote7
              | quote8
              | quote9  
              | quote10
              | quote11
              | quote12
              | quote13
              | quote14
              | quote15
              | quote16
              | quote17
              | quote18
              | quote19
              | quote20
              | quote21
              | quote22
              | quote23
              | quote24
              | quote25
     '''
    p[0] = p[1]


def p_quote4(p):
    'quote4 : KHABAR3 MODAFILAYH2 FI3LNA9ISS FI3LMADI6 7ARFJAR5 FA3IL'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote1(p):
    'quote1 : ISSMMAWSOUL FI3LMADI2 MAF3OULBIH FI3LMADI'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote2(p):
    'quote2 : MOBTADAE1 KHABAR1 NA3T1 WAW3ATF MOBTADAE2 KHABAR2 NA3T2 FI3LAMR1 MODAF1 MODAFILAYH1 ISSMMAJROUR1 WAW3ATF FI3LAMR2 MAF3OULBIH1 ISSMMAJROUR2'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote3(p):
    'quote3 : 7ARFNAFY1 FI3LMODARI3 ISSMMAJROUR3 7ARFNASSB FI3LMODARI31 ISSMMAJROUR4 ISSM1 WAW3ATF2 ISSM2 ISSM3 FI3LMADI3 NA3T3 ISSM4 FI3LMADI4 WAW3ATF2 MA3TOUF ISSM5 FI3LMADI5'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote5(p):
    'quote5 : FI3LNA9ISS FI3LMADI7 ISSMJALALA 7ARFJAR6 ISSMMAJROUR6 MODAFILAYH3 FI3LMODARI32 HARFGHAYA FI3LMADI8 7ARFJAR7 ISSMMAJROUR7 MODAFILAYH4 7ARFNASSB FI3LMODARI33'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote6(p):
    'quote6 : FI3LNA9ISS MOBTADAE3 KHABAR4 FI3LMODARI34'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote7(p):
    'quote7 : ADATNAFY ISSM6 ISSMMAJROUR8 7ARFJARZA2ID 7ARFJAR8 ISSMMAJROUR9 MOBTADAEMARFOU3 MODAFILAYH5 FI3LNA9ISS FI3LMADI9'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote8(p):
    'quote8 : FI3LNA9ISS FI3LMADI10 FI3LMODARI35 DARF'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote9(p):
    'quote9 : FI3LAMR3 MAF3OULBIH2 MODAFILAYH6 7ARFISTI2NAF ISSMJALALA FI3LMADI11 FI3LMADI12 MAF3OULBIH3 7ARFJAR16 ISSMMAJROUR10'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote10(p):
    'quote10 : MOBTADAE4 KHABAR5 MODAFILAYH7 WAW3ATF MOBTADAE5 KHABAR6 MODAFILAYH8'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote11(p):
    'quote11 : 7ARFTAWKID ISSMICHARA ISSM7 FI3LMODARI36 7ARFJAR9 FA3IL1 FI3LMODARI37 DAMIRMOTASIL4 MAF3OULBIH4 MODAFILAYH9'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote12(p):
    'quote12 : 7ARFNAFY2 ISSM8 ISSMMAJROUR11 7ARFJAR11 ISSMMAJROUR12 MODAFILAYH10'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote13(p):
    'quote13 : MOBTADAE6 MODAFILAYH11 KHABAR7 MODAFILAYH12 WAW3ATF MOBTADAE7 MODAFILAYH13 KHABAR8 MODAFILAYH14'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote14(p):
    'quote14 : ISSMTAFDIL MODAFILAYH15 FI3LNA9ISS FI3LMADI13 MOSTATNA 7ARFJAR12'
    p[0] = " ".join(p[1:])
    print("BRAVO")

def p_quote15(p):
    'quote15 : FI3LNA9ISS FI3LMADI14 FA3IL2 MAF3OULBIH5 MOBTADAE8 FI3LMADI15 7ARFJAAR ISSMMAJROUR14 MODAFILAYH16 MA3TOUF1 MODAFILAYH17'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote16(p):
    'quote16 : ISSMMAWSOUL FI3LMADI16 FA3IL3 ISSM9 MODAFILAYH18 7ARFISTITNA2 FI3LMODARI38 ISSMMAWSOUL FI3LMADI17 JARWAMAJROUR MAF3OULBIH6'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote17(p):
    'quote17 : MOBTADAE9 KHABAR9 MODAFILAYH19 WAW3ATF 7ARFNAFY2 FI3L MAF3OULBIH7 7ARFJAR16 ISSMMAJROUR15 MODAFILAYH20'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote18(p):
    'quote18 : MOBTADAE10 7ARFJAR13 ISSMMAJROUR16 KHABAR10 7ARFJAR14 ISSMMAJROUR17 MODAFILAYH21'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote19(p):
    'quote19 : ISSMMAWSOUL FI3LMADI18 FA3IL4 MAF3OULBIH8 7ARFNAFY3 FI3LMADI19 FA3IL5 MAF3OULBIH9'
    p[0] = " ".join(p[1:])
    print("BRAVO")
def p_quote20(p):
    'quote20 : MOBTADAE11 KHABAR11 ISSMMAJROUR18 MODAFILAYH22 WAW3ATF MOBTADAE12 KHABAR12 FA3IL6 JARWAMAJROUR1 7ARFJAR15 ISSMMAJROUR19 MODAFILAYH23'
    p[0] = " ".join(p[1:])
    print("BRAVO")

def p_quote21(p):
    'quote21 : DETERMINER ADJECTIVE CONJUNCTION VERB PRT VERB1 PRONOUN'
    p[0] = " ".join(p[1:])
    print("BRAVO")

def p_quote22(p):
    'quote22 : NOUN1 VERB2 DETERMINER1 ADJECTIVE1 NOUN3 PREPOSITION1 DETERMINER2 NOUN4'
    p[0] = " ".join(p[1:])
    print("BRAVO")   

def p_quote23(p):
    'quote23 : ADJECTIVE2 NOUN5 VERB3 ADVERB1 ADVERB2 ADJECTIVE3 CONJUNCTION1 ADJECTIVE4 NOUN6 VERB4 ADVERB3 ADJECTIVE5'
    p[0] = " ".join(p[1:])
    print("BRAVO")

def p_quote24(p):
    'quote24 : DETERMINER3 NOUN7 PREPOSITION2 NOUN8 VERB5 DETERMINER4 NOUN9 PREPOSITION3 DETERMINER5 NOUN10'
    p[0] = " ".join(p[1:])
    print("BRAVO")

def p_quote25(p):
    'quote25 : PRONOM SUJET1 SUJET2 VERBE ADJECTIF SUJET3 ADJECTIF2 COMPLEMENT2'
    p[0] = " ".join(p[1:])
    print("BRAVO")
parser = yacc.yacc()

def p_error(p):
    print("Syntax error in input!")



# Build the lexer
#path = 'Quote1.txt'

# Open the file in binary mode for reading
#file = open(path, 'rb')
#data = file.read()
#text = data.decode('utf-8')

# Now you can create a lexer and input the text
#lexer = lex.lex()
#lexer.input(text)

#quote14
#quote8
#quote4
#quote7
#quote1


quote1 = 'مَنْ صَارَعَ الْحَقَّ صَرَعَهُ'
quote2 = 'الْحِلْمُ غِطَاءٌ سَاتِرٌ وَ الْعَقْلُ حُسَامٌ قَاطِعٌ فَاسْتُرْ خَلَلَ خُلُقِكَ بِحِلْمِكَ وَ قَاتِلْ هَوَاكَ بِعَقْلِكَ'
quote3 = 'لاَ يَنْبَغِي لِلْعَبْدِأَنْ يَثِقَ بِخَصْلَتَيْنِ الْعَافِيَةِ وَ الْغِنَى بَيْنَا تَرَاهُ مُعَافىً إِذْ سَقِمَ وَ غَنِيّاً إِذِ افْتَقَرَ'
quote4 = 'أَشَدُّالذُّنُوبِ مَااسْتَخَفَّ بِهِ صَاحِبُهُ'
quote5 = 'مَا أَخَذَ اللهُ عَلَى أَهْلِ الْجَهْلِ أَنْ يَتَعَلَّمُوا حَتَّى أَخَذَ عَلَى أَهْلِ الْعِلْمِ أَنْ يُعَلِّمُوا'
quote7 = 'لَيْسَ بَلَدٌ بأَحَقَّ بِكَ مِنْ بَلَدٍ خَيْرُ الْبِلاَدِ مَا حَمَلَكَ'
quote6 = 'النَّاسُ أَعْدَاءُ مَا جَهِلُوا'
quote8 = 'مَا زَنَى غَيُورٌ قَطُّ'
quote9 = 'اتَّقُوا ظُنُونَ الْمُؤْمِنِينَ فَإِنَّ اللهَ تَعَالَى جَعَلَ الْحَقَّ عَلَى أَلْسِنَتِهِمْ'
quote11 = 'إِنَّ هذِهِ الْقُلُوبَ تَمَلُّ كَمَاتَمَلُّ الْأَبْدَانُ فَابْتَغُوا لَهَا طَرَائِفَ الْحِكْمَةِ'
quote12 = 'لاَ طَاعَةَ لَمخْلُوقٍ فِي مَعْصِيَةِالْخَالِقِ'
quote13 = 'لِسَانُ الْعَاقِلِ وَرَاءَ قَلْبِهِ وَقَلْبُ الْأَحْمَقِ وَرَاءَ لِسَانِهِ'
quote14 = 'أَفْضَلُ الْأَعْمَالِ مَا أَكْرَهْتَ نَفْسَكَ عَلَيْهِ'
quote15 = 'مَا أَضْمَرَ أَحَدٌ شَيْئاً إِلاَّ ظَهَرَ فِي فَلَتَاتِ لِسَانِهِ وَ صَفَحَاتِ وَجْهِهِ'
quote16 = 'مَنْ وَضَعَ نَفْسَهُ مَوَاضِعَ التُّهَمَةِ فَلاَ يَلُومَنَّ مَنْ أَسَاءَ بِهِ الظَّنَّ'
quote17 = 'النَّاسُ أَبْنَاءُ الدُّنْيَا وَلاَ يُلْاَمُ الرَّجُلُ عَلَى حُبِّ أُمِّهِ'
quote19 = 'مَنْ كَسَاهُ الْحَيَاءُ ثَوْبَهُ لَمْ يَرَ النَّاسُ عَيْبَهُ'
quote20 = 'الْبُخْلُ جَامعٌ لِمَسَاوِىءِ الْعُيُوبِ وَ هُوَ زِمَامٌ يُقَادُ بهِ إِلَى كُلِّ سُوءٍ'
quote18 = 'الْإِسْتِغْنَاءُ عَنِ الْعُذْرِ أَعَزُّ مِنَ الصِّدْقِ بِهِ'
quote10 = 'الْعَفَافُ زِينَةُ الْفَقْرِ وَ الشُّكْرُ زِينَةُ الْغِنَى'



#text = input("Enter your text : ")
#res = parser.parse(text)


app = Flask(__name__)


resultLexer = "" 
positionLexerError=""

def p_error(p):
    global resultParser
    global positionParserError
    print("Syntax error in input!")
    positionParserError = {
        "value":  p.value,
        "length": len(p.value)
    }
    print("positionParserError = ", positionParserError)
    resultParser = "incorrect"


def is_valid_text(text):
    #lexer.input(text)
    try:
        #parser.parse(lexer=lexer)
        parser.parse(text)
        return True
    except Exception:
        return False



@app.route('/get_voice_input')
def get_voice_input():
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio, language="ar-SA")
            return jsonify({'voiceInput': text.lower()})
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Google Web Speech API request failed; {e}")
    
    return jsonify({'voiceInput': None})




@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    global resultLexer
    global positionLexerError
    resultLexer = ""
    positionLexerError = ""
    if request.method == 'POST':
        text = request.form['keyword']
        if is_valid_text(text):
            return redirect(url_for('result1'))
        else:
            result = "Invalid Text"
            return redirect(url_for('result2'))
            

    return render_template('index.html', result=result)


@app.route('/result1')
def result1():
    return render_template('index.html', message="Bravo !")


@app.route('/result2')
def result2():
    return render_template('index.html', message="Your text is not correct it contains errors")


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    #tokens = list(lexer)  # Convert the generator to a list
    resultat = None
    if request.method == 'POST':
        text = request.form['proverb']
        if is_valid_text(text):
            return redirect(url_for('result11'))
        else:
            #result = "Invalid Text"
            return redirect(url_for('result22'))


    #Collect token results
    #token_info_list = [{'type': token.type, 'value': token.value} for token in tokens]

    result = parser.parse(text)


    return render_template('index.html', resultat=resultat)


@app.route('/result11')
def result11():
    return render_template('index.html', message1="Bravo !")

@app.route('/result22')
def result22():
    return render_template('index.html', message1="Your text is not correct it contains errors")


@app.route('/verifier', methods=['GET', 'POST'])
def verifier():
    #tokens = list(lexer)  # Convert the generator to a list
    resultat1 = None
    if request.method == 'POST':
        text = request.form['frenchText']
        if is_valid_text(text):
            return redirect(url_for('result111'))
        else:
            #result = "Invalid Text"
            return redirect(url_for('result222'))


    #Collect token results
    #token_info_list = [{'type': token.type, 'value': token.value} for token in tokens]

    result = parser.parse(text)


    return render_template('index.html', resultat1=resultat1)

@app.route('/result111')
def result111():
    return render_template('index.html', message2="Proverbe correct !")

@app.route('/result222')
def result222():
    return render_template('index.html', message2="Le texte contient des erreurs !")


#ENGLISH TEXT :

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    #tokens = list(lexer)  # Convert the generator to a list
    resultat11 = None
    if request.method == 'POST':
        text = request.form['EnglishText']
        if is_valid_text(text):
            return redirect(url_for('result1111'))
        else:
            #result = "Invalid Text"
            return redirect(url_for('result2222'))


    #Collect token results
    #token_info_list = [{'type': token.type, 'value': token.value} for token in tokens]

    result = parser.parse(text)


    return render_template('index.html', resultat11=resultat11)



@app.route('/result1111')
def result1111():
    return render_template('index.html', message3="Correct Quote!")

@app.route('/result2222')
def result2222():
    return render_template('index.html', message3="Your quote contains errors !")

def reset_global_variables():
    global resultLexer
    global positionLexerError
    resultLexer = ""
    positionLexerError = ""


if __name__ == '__main__':
    app.run(debug=True)

