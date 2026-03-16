import ply.lex as lex
from pyarabic import *

import re
global resultLexer;global positionLexerError


positionLexerError,positionParserError = dict(),dict()

# List of token names.   This is always required
tokens = (
   'FI3LMADI',
   'MAF3OULBIH',
   'FI3LMADI2',
   'ISSMMAWSOUL',

   'ISSMMAJROUR2',
   'MAF3OULBIH1',
   'FI3LAMR2',
   'WAW3ATF1',
   'ISSMMAJROUR1',
   'MODAFILAYH1',
   'MODAF1',
   'FI3LAMR1',
   'NA3T2',
   'KHABAR2',
   'MOBTADAE2',
   'WAW3ATF',
   'NA3T1',
   'KHABAR1',
   'MOBTADAE1',


   '7ARFNAFY1',
   'FI3LMODARI3',
   'ISSMMAJROUR3',
   '7ARFNASSB',
   'FI3LMODARI31',
   'ISSMMAJROUR4',
   'ISSM1',
   'WAW3ATF2',
   'ISSM2',
   'ISSM3',
   'FI3LMADI3',
   'NA3T3',
   'ISSM4',
   'FI3LMADI4',
   'MA3TOUF',
   'ISSM5',
   'FI3LMADI5',
   
   'KHABAR3',
   'MODAFILAYH2',
   'FI3LNA9ISS',
   'FI3LMADI6',
   '7ARFJAR5',
   'FA3IL',

   'FI3LMADI7',
   'ISSMJALALA',
   '7ARFJAR6',
   'ISSMMAJROUR6',
   'MODAFILAYH3',
   'FI3LMODARI32',
   'HARFGHAYA',
   'FI3LMADI8',
   '7ARFJAR7',
   'ISSMMAJROUR7',
   'MODAFILAYH4',
   'FI3LMODARI33',

   'MOBTADAE3',
   'KHABAR4',
   'FI3LMODARI34',

   'ADATNAFY',
   'ISSM6',
   'ISSMMAJROUR8',
   '7ARFJARZA2ID',
   '7ARFJAR8',
   'ISSMMAJROUR9',
   'MOBTADAEMARFOU3',
   'MODAFILAYH5',
   'FI3LMADI9',

   'FI3LMADI10',
   'FI3LMODARI35',
   'DARF',

   'FI3LAMR3',
   'MAF3OULBIH2',
   'MODAFILAYH6',
   '7ARFISTI2NAF',
   'FI3LMADI11',
   'FI3LMADI12',
   'MAF3OULBIH3',
   '7ARFJAR16',
   'ISSMMAJROUR10',

   'MOBTADAE4',
   'KHABAR5',
   'MODAFILAYH7',
   'MOBTADAE5',
   'KHABAR6',
   'MODAFILAYH8',

   '7ARFTAWKID',
   'ISSMICHARA',
   'ISSM7',
   'FI3LMODARI36',
   '7ARFJAR9',
   'FA3IL1',
   'FI3LMODARI37',
   'DAMIRMOTASIL4',
   'MAF3OULBIH4',
   'MODAFILAYH9',

   '7ARFNAFY2',
   'ISSM8',
   'ISSMMAJROUR11',
   '7ARFJAR11',
   'ISSMMAJROUR12',
   'MODAFILAYH10',

   'MOBTADAE6',
   'MODAFILAYH11',
   'KHABAR7',
   'MODAFILAYH12',
   'MOBTADAE7',
   'MODAFILAYH13',
   'KHABAR8',
   'MODAFILAYH14',

   'ISSMTAFDIL',
   'MODAFILAYH15',
   'FI3LMADI13',
   'MOSTATNA',
   '7ARFJAR12',

   'FI3LMADI14',
   'FA3IL2',
   'MAF3OULBIH5',
   'MOBTADAE8',
   'FI3LMADI15',
   '7ARFJAAR',
   'ISSMMAJROUR14',
   'MODAFILAYH16',
   'MA3TOUF1',
   'MODAFILAYH17',

   'FI3LMADI16',
   'FA3IL3',
   'ISSM9',
   'MODAFILAYH18',
   '7ARFISTITNA2',
   'FI3LMODARI38',
   'FI3LMADI17',
   'JARWAMAJROUR',
   'MAF3OULBIH6',

   'MOBTADAE9',
   'KHABAR9',
   'MODAFILAYH19',
   'FI3L',
   'MAF3OULBIH7',
   'ISSMMAJROUR15',
   'MODAFILAYH20',

   'MOBTADAE10',
   '7ARFJAR13',
   'ISSMMAJROUR16',
   'KHABAR10',
   '7ARFJAR14',
   'ISSMMAJROUR17',
   'MODAFILAYH21',

   'FI3LMADI18',
   'FA3IL4',
   'MAF3OULBIH8',
   '7ARFNAFY3',
   'FI3LMADI19',
   'FA3IL5',
   'MAF3OULBIH9',

   'MOBTADAE11',
   'KHABAR11',
   'ISSMMAJROUR18',
   'MODAFILAYH22',
   'MOBTADAE12',
   'KHABAR12',
   'FA3IL6',
   'JARWAMAJROUR1',
   '7ARFJAR15',
   'ISSMMAJROUR19',
   'MODAFILAYH23',

   #ENGLISH QUOTES

   'DETERMINER',
   'ADJECTIVE',
   'CONJUNCTION',
   'VERB',
   'PRT',
   'VERB1',
   'PRONOUN',

   'NOUN1',
   'VERB2',
   'DETERMINER1',
   'ADJECTIVE1',
   'NOUN3',
   'PREPOSITION1',
   'DETERMINER2',
   'NOUN4',

   'ADJECTIVE2',
   'NOUN5',
   'VERB3',
   'ADVERB1',
   'ADVERB2',
   'ADJECTIVE3',
   'CONJUNCTION1',
   'ADJECTIVE4',
   'NOUN6',
   'VERB4',
   'ADVERB3',
   'ADJECTIVE5',

   'DETERMINER3',
   'NOUN7',
   'PREPOSITION2',
   'NOUN8',
   'VERB5',
   'DETERMINER4',
   'NOUN9',
   'PREPOSITION3',
   'DETERMINER5',
   'NOUN10',

   #FRENCH QUOTES

   'PRONOM',
   'SUJET1',
   'SUJET2',
   'VERBE',
   'ADJECTIF',
   'SUJET3',
   'ADJECTIF2',
   'COMPLEMENT2'
   )

# Regular expression rules for simple tokens

######## QUOTE 1 ########
t_FI3LMADI   = r'صرعه'
t_MAF3OULBIH   = r'الحق'
t_FI3LMADI2  = r'صارع'
t_ISSMMAWSOUL  = r'من'
######## QUOTE 1 ########

######## QUOTE 2 ########
t_ISSMMAJROUR2 = r'بعقلك'
t_MAF3OULBIH1 = r'هواك'
t_FI3LAMR2 = r'قاتل'
t_WAW3ATF1 = r'و'
t_ISSMMAJROUR1 = r'بحلمك'
t_MODAFILAYH1 = r'خلقك'
t_MODAF1 = r'خلل'
t_FI3LAMR1 = r'فاستر'
t_NA3T2 = r'قاطع'
t_KHABAR2 = r'حسام'
t_MOBTADAE2 = r'العقل'
t_WAW3ATF = r'و'
t_NA3T1 = r'ساتر'
t_KHABAR1 = r'غطاء'
t_MOBTADAE1 = r'الحلم'
######## QUOTE 2 ########

######## QUOTE 3 ########
t_7ARFNAFY1 = r'لا'
t_FI3LMODARI3 = r'ينبغي'
t_ISSMMAJROUR3 = r'للعبد'
t_7ARFNASSB = r'أن'
t_FI3LMODARI31 = r'يثق'
t_ISSMMAJROUR4 = r'بخصلتين'
t_ISSM1 = r'العافية'
t_WAW3ATF2 = r'و'
t_ISSM2 = r'الغنى'
t_ISSM3 = r'بينا'
t_FI3LMADI3 = r'تراه '
t_NA3T3 = r'معافى'
t_ISSM4 = r'إذ'
t_FI3LMADI4 = r'سقم'
#WAW3ATF
t_MA3TOUF = r'غنيا'
t_ISSM5 = r'إذ'
t_FI3LMADI5 = r'افتقر'
######## QUOTE 3 ########

######## QUOTE 4 ########
t_KHABAR3 = r'أشد'
t_MODAFILAYH2 = r'الذنوب'
t_FI3LNA9ISS = r'ما'
t_FI3LMADI6 = r'استخف'
t_7ARFJAR5 = r'به'
t_FA3IL = r'صاحبه'
######## QUOTE 4 ########

######## QUOTE 5 ########
#FI3LNA9ISS
t_FI3LMADI7 = r'أَخَذَ'
t_ISSMJALALA = r'اللهُ'
t_7ARFJAR6 = r'عَلَى'
t_ISSMMAJROUR6 = r'أَهْلِ'
t_MODAFILAYH3 = r'الْجَهْلِ'
t_FI3LMODARI32 = r'يَتَعَلَّمُوا'
t_HARFGHAYA = r'حَتَّى'
t_FI3LMADI8 = r'أَخَذَ'
t_7ARFJAR7 = r'عَلَى'
t_ISSMMAJROUR7 = r'أَهْلِ'
t_MODAFILAYH4 = r'الْعِلْمِ'
#7ARFNASSB
t_FI3LMODARI33 = r'يُعَلِّمُوا'
######## QUOTE 5 ########

######## QUOTE 6 ########
#FI3LNA9ISS
t_MOBTADAE3 = r'الناس'
t_KHABAR4 = r'اعداء'
t_FI3LMODARI34 = r'جهلوا'
######## QUOTE 6 ########

######## QUOTE 7 ########
t_ADATNAFY = r'ليس'
t_ISSM6 = r'بلد'
t_ISSMMAJROUR8 = r'بأحق'
t_7ARFJARZA2ID = r'بك'
t_7ARFJAR8 = r'من'
t_ISSMMAJROUR9 = r'بلد'
t_MOBTADAEMARFOU3 = r'خير'
t_MODAFILAYH5 = r'البلاد'
#FI3LNA9ISS
t_FI3LMADI9 = r'حملك'
######## QUOTE 7 ########

######## QUOTE 8 ########
#FI3LNA9ISS
t_FI3LMADI10 = r'زَنَى'
t_FI3LMODARI35 = r'غَيُورٌ'
t_DARF = r'قَطُّ'
######## QUOTE 8 ########

######## QUOTE 9 ########
t_FI3LAMR3 = r'اتَّقُوا'
t_MAF3OULBIH2 = r'ظُنُونَ'
t_MODAFILAYH6 = r'الْمُؤْمِنِينَ'
t_7ARFISTI2NAF = r'فَإِنَّ'
#ISSMJALALA
t_FI3LMADI11 = r'تَعَالَى'
t_FI3LMADI12 = r'جَعَلَ'
t_MAF3OULBIH3 = r'الْحَقَّ'
t_7ARFJAR16 = r'عَلَى'
t_ISSMMAJROUR10 = r'أَلْسِنَتِهِمْ'
######## QUOTE 9 ########

######## QUOTE 10 ########
t_MOBTADAE4 = r'العفاف'
t_KHABAR5 = r'زينه'
t_MODAFILAYH7 = r'الفقر'
#WAW3ATF
t_MOBTADAE5 = r'الشكر'
t_KHABAR6 = r'زينة'
t_MODAFILAYH8 = r'الغنى'
######## QUOTE 10 ########

######## QUOTE 11 ########
t_7ARFTAWKID = r'إِنَّ'
t_ISSMICHARA = r'هذِهِ'
t_ISSM7 = r'الْقُلُوبَ'
t_FI3LMODARI36 = r'تَمَلُّ'
t_7ARFJAR9 = r'كَمَا'
t_FA3IL1 = r'الْأَبْدَانُ'
t_FI3LMODARI37 = r'فَابْتَغُوا'
t_DAMIRMOTASIL4 = r'لَهَا'
t_MAF3OULBIH4 = r'طَرَائِفَ'
t_MODAFILAYH9 = r'الْحِكْمَةِ'
######## QUOTE 11 ########

######## QUOTE 12 ########
t_7ARFNAFY2 = r'لاَ'
t_ISSM8 = r'طَاعَةَ'
t_ISSMMAJROUR11 = r'لَمخْلُوقٍ'
t_7ARFJAR11 = r'فِي'
t_ISSMMAJROUR12 = r'مَعْصِيَةِ'
t_MODAFILAYH10 = r'الْخَالِقِ'
######## QUOTE 12 ########

######## QUOTE 13 ########
t_MOBTADAE6 = r'لسان'
t_MODAFILAYH11 = r'العاقل'
t_KHABAR7 = r'وراء'
t_MODAFILAYH12 = r'قلبه'
#WAW3ATF
t_MOBTADAE7 = r'قلب'
t_MODAFILAYH13 = r'الأَحمق'
t_KHABAR8 = r'وراء'
t_MODAFILAYH14 = r'لسانه'
######## QUOTE 13 ########

######## QUOTE 14 ########
t_ISSMTAFDIL = r'أفضل'
t_MODAFILAYH15 = r'الأعمال'
#FI3LNA9ISS
t_FI3LMADI13 = r'أكرهت'
t_MOSTATNA = r'نفسك'
t_7ARFJAR12 = r'عليه'
######## QUOTE 14 ########

######## QUOTE 15 ########
#FI3LNA9ISS
t_FI3LMADI14 = r'أضمر'
t_FA3IL2 = r'أحد'
t_MAF3OULBIH5 = r'شيئا'
t_MOBTADAE8 = r'إلا'
t_FI3LMADI15 = r'ظهر'
t_7ARFJAAR = r'في'
t_ISSMMAJROUR14 = r'فلتات'
t_MODAFILAYH16 = r'لسانه'
t_MA3TOUF1 = r'صفحات'
t_MODAFILAYH17 = r'وجهه'
######## QUOTE 15 ########

######## QUOTE 16 ########
#ISSMMAWSOUL
t_FI3LMADI16 = r'وَضَعَ'
t_FA3IL3 = r'نَفْسَهُ'
t_ISSM9 = r'مَوَاضِعَ'
t_MODAFILAYH18 = r'التُّهَمَةِ'
t_7ARFISTITNA2 = r'فَلاَ'
t_FI3LMODARI38 = r'يَلُومَنَّ'
#ISSMMAWSOUL
t_FI3LMADI17 = r'أَسَاءَ'
t_JARWAMAJROUR = r'بِهِ'
t_MAF3OULBIH6 = r'الظَّنَّ'
######## QUOTE 16 ########

######## QUOTE 17 ########
t_MOBTADAE9 = r'النَّاسُ'
t_KHABAR9 = r'أَبْنَاءُ'
t_MODAFILAYH19 = r'الدُّنْيَا'
#WAW3ATF
#7ARFNAFY2
t_FI3L = r'يُلْاَمُ'
t_MAF3OULBIH7 = r'الرَّجُلُ'
#7ARFJAR16
t_ISSMMAJROUR15 = r'حُبِّ'
t_MODAFILAYH20 = r'أُمِّهِ'
######## QUOTE 17 ########

######## QUOTE 18 ########
t_MOBTADAE10 = r'الإستغناء'
t_7ARFJAR13 = r'عن'
t_ISSMMAJROUR16 = r'العذر'
t_KHABAR10 = r'أعز'
t_7ARFJAR14 = r'من'
t_ISSMMAJROUR17 = r'الصدق'
t_MODAFILAYH21 = r'به'
######## QUOTE 18 ########

######## QUOTE 19 ########
#ISSMMAWSOUL
t_FI3LMADI18 = r'كَسَاهُ'
t_FA3IL4 = r'الْحَيَاءُ'
t_MAF3OULBIH8 = r'ثَوْبَهُ'
t_7ARFNAFY3 = r'لَمْ'
t_FI3LMADI19 = r'يَرَ'
t_FA3IL5 = r'النَّاسُ'
t_MAF3OULBIH9 = r'عَيْبَهُ'
######## QUOTE 19 ########

######## QUOTE 20 ########
t_MOBTADAE11 = r'الْبُخْلُ'
t_KHABAR11 = r'جَامعٌ'
t_ISSMMAJROUR18 = r'لِمَسَاوِىءِ'
t_MODAFILAYH22 = r'الْعُيُوبِ'
#WAW3ATF
t_MOBTADAE12 = r'هُوَ'
t_KHABAR12 = r'زِمَامٌ'
t_FA3IL6 = r'يُقَادُ'
t_JARWAMAJROUR1 = r'بهِ'
t_7ARFJAR15 = r'إِلَى'
t_ISSMMAJROUR19 = r'كُلِّ'
t_MODAFILAYH23 = r'سُوءٍ'
######## QUOTE 20 ########

######## ENGLISH QUOTES #########
t_DETERMINER = r'The'
t_ADJECTIVE = r'best'
t_CONJUNCTION = r'revenge'
t_VERB = r'is'
t_PRT = r'to'
t_VERB1 = r'improve'
t_PRONOUN = r'yourself'


t_NOUN1 = r'Silence'
t_VERB2 = r'is'
t_DETERMINER1 = r'the'
t_ADJECTIVE1 = r'best'
t_NOUN3 = r'reply'
t_PREPOSITION1 = r'to'
t_DETERMINER2 = r'a'
t_NOUN4 = r'fool'


t_ADJECTIVE2 = r'Beautiful'
t_NOUN5 = r'people'
t_VERB3 = r'are'
t_ADVERB1 = r'not'
t_ADVERB2 = r'always'
t_ADJECTIVE3 = r'good'
t_CONJUNCTION1 = r'but'
t_ADJECTIVE4 = r'good'
t_NOUN6 = r'people'
t_VERB4 = r'are'
t_ADVERB3 = r'always'
t_ADJECTIVE5 = r'beautiful'


t_DETERMINER3 = r'The'
t_NOUN7 = r'word'
t_PREPOSITION2 = r'of'
t_NOUN8 = r'God'
t_VERB5 = r'is'
t_DETERMINER4 = r'the'
t_NOUN9 = r'medicine'
t_PREPOSITION3 = r'of'
t_DETERMINER5 = r'the'
t_NOUN10 = r'heart'

##FRENCH QUOTE #######

t_PRONOM = r'un'
t_SUJET1 = r'beau'
t_SUJET2 = r'caractère'
t_VERBE = r'est'
t_ADJECTIF = r'meilleur'
t_SUJET3 = r'qun'
t_ADJECTIF2 = r'beau'
t_COMPLEMENT2 = r'corps'



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
#def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    #t.lexer.skip(1)


resultLexer = "" 
positionLexerError=""

def t_error(t):
    global resultLexer
    global positionLexerError
    print("Illegal character '%s'" % t.value)
    #t.lexer.skip(len(t.value))
    
    positionLexerError = {
        "value":  t.value,
        "length": len(t.value)
    }
    print("positionLexerError = ",positionLexerError)
    resultLexer = "incorrect"



# Build the lexer
#path = 'NahjulBalagha.txt'

# Open the file in binary mode for reading
#file = open(path, 'rb')
#data = file.read()
#text = data.decode('utf-8')
# Now you can create a lexer and input the text

quote1 = 'من صارع الحق صرعه'

lexer = lex.lex()

lexer.input(quote1)

# Readlines should not be used here, as the content is already read above
# If you need lines, you can split the text into lines using text.split('\n')


# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)