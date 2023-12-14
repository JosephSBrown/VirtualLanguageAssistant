data = {"intents": [
    ##########------------------ ENGLISH SPEECH PATTERNS ----------------##################
    {
      "tag": "greeting",
      "input": [
        "hello",
        "hi there",
        "nice to meet you",
        "hi",
        "hey there",
        "hey",
        "hi there",
        "hi, nice to meet you",
        "hello there",
        "anyone there ?",
        "knock knock"
      ],
      "responses": [
        "Hi",
        "Hello, how are you?",
        "Hey, how are you?",
        "Howdy",
        "Hi, how are you?",
        "Hello <NAME>, how are you?"
      ]
    },
    {
      "tag": "goodbye",
      "input": [
        "bye",
        "bye bro",
        "adios",
        "okay bye",
        "goodbye",
        "see you later",
        "i will catch you later",
        "i will catch up later",
        "okay i will see you later",
        "I will talk to you later",
        "will text you later",
        "bye bro, I'll talk to you later",
        "Bye brother"
      ],
      "responses": [
        "okay, bye",
        "have a nice day",
        "adios",
        "goodbye",
        "see you later",
        "nice conversation. Bye",
        "okay. Have a nice day",
        "Take care",
        "we'll meet soon",
        "Yeah Sure, Will talk to you later",
        "Okay, Take care"
      ]
    },
    {
      "tag": "howami",
      "input": [
        "how are you ?",
        "I am fine , how are you ?",
        "are you fine ?",
        "how are things going on ?",
        "everything going on okay ?",
        "how's everything there ?",
        "how's everything going on ?",
        "is everything okay ?"
      ],
      "responses": [
        "Yeah , am fine",
        "Everything's going on well",
        "Doing good. Thanks you are my best friend <NAME>",
        "Things are Great",
        "Yeah Fine, nothing much going on in my life",
        "Everything's great."
      ]
    },
    {
      "tag": "whoareyou",
      "input": [
        "who are you?",
        "what are you?",
        "what is your name?",
        "are you a chatbot?",
        "what can I call you?",
        "your name ?",
        "are you a bot?",
        "how do I address you?",
        "How do I call you"
      ],
      "responses": [
        "I am <BOTNAME> Your Virtual Language Assistant",
        "I am <BOTNAME>, What Would You Like to Talk About?",
        "I am <BOTNAME>",
        "My name is <BOTNAME> and I am the Goat",
        "You can call me <BOTNAME> and I am your Virtual Assistant",
        "My name is <BOTNAME> and I am here to help you learn Languages"
      ]
    },
    {
      "tag": "whereareyou",
      "input": [
        "where are you from?",
        "which country are you from?",
        "where do you live?",
        "where are you?",
        "where do you live in?",
        "which place do you live in?",
        "where are you currently at",
        "where do you live currently?",
        "you are from where",
        "you are from?"
      ],
      "responses": [
        "I live in London, but I am Always Ready to Help You Learn",
        "I am from London",
        "I live in London Now, but I used to Live in Cambridge",
        "I was born in Peterborough but now I am Worldwide"
      ]
    },
    {
      "tag": "learn",
      "input": [
        "how can you teach me?",
        "how can I learn from you?",
        "how will I learn using you?"
      ],
      "responses": [
        "You Learn by Trying to Maintain Natural Conversation With Me",
        "We Learn together but teaching each other to speak Languages",
        "I try to teach you natural language conversations through speaking and immersion"
      ]
    },
    {
      "tag": "prerequisites",
      "input": [
        "what do I need to know to learn?",
        "do I need to know anything to start?",
        "can I start learning a language with you as a beginner?"
      ],
      "responses": [
        "It doesn't matter what level of Language Learning you are, I will help you improve judgement free",
        "Whether you're a beginner or an expert, I will always be here to help and assist you"
      ]
    },
    #################------------------ FRENCH SPEECH PATTERNS ----------------########################
    {
      "tag": "greeting-fr",
      "input": [
        "Bonjour",
        "Salut",
        "Bonsoir",
        "Enchanté",
        "Ravie de faire votre connaissance"
      ],
      "responses": [
        "Bonjour",
        "Salut",
        "Bonsoir",
        "Bonjour <NAME>",
        "Salut <NAME>",
        "Enchanté <NAME>"
      ]
    },
    {
      "tag": "goodbye-fr",
      "input": [
        "au revoir",
        "au revoir, à la prochaine",
        "À bientôt",
        "À plus tard.",
        "Au plaisir.",
        "Bonne nuit",
        "Au revoir, bonne journée",
        "Adieu",
        "Au plaisir de vous revoir",
        "Bonne continuation"
      ],
      "responses": [
        "au revoir, à la prochaine",
        "au revoir <NAME>",
        "À bientôt",
        "À plus tard.",
        "Au plaisir.",
        "au revoir",
        "Adieu <NAME>"
      ]
    },
    {
      "tag": "howami-fr",
      "input": [
        "Comment ça va?",
        "ça va?",
        "Comment allez-vous?",
        "Comment vous sentez-vous?",
        "Tout va bien?",
        "Vous vous portez bien?",
        "Vous allez bien?",
        "Comment allez-vous aujourd’hui?"
      ],
      "responses": [
        "Ça va, et toi?",
        "Ça va pas mal, merci, et toi?",
        "Je vais bien, et toi comment ça va?",
        "Ça va très bien, merci!",
        "Je passe une super journée, merci",
        "Ça farte",
        "Tout va bien",
        "Ça farte <NAME>",
        "Ça va très bien, merci <NAME>!",
        "Tout va bien <NAME>"
      ]
    },
    {
      "tag": "whoareyou-fr",
      "input": [
        "qui es-tu?",
        "qui êtes-vous?",
        "Tu es qui, toi?",
        "qui t’es?",
        "C’est qui toi?",
        "Vous êtes qui",
        "comment puis-je t'appeler?",
        "comment dois-je vous appeler?"
      ],
      "responses": [
        "Je Suis <BOTNAME>, votre assistant linguistique virtuel",
        "Je suis <BOTNAME>, De quoi aimerais-tu parler?",
        "Je suis <BOTNAME>",
        "Mon nom est <BOTNAME> et Je suis la chèvre",
        "tu peux m'appeler <BOTNAME> et je suis votre assistant linguistique virtuel",
        "Mon nom est <BOTNAME> et je suis là pour vous aider à apprendre des langues"
      ]
    },
    ###################------------------ JAPANESE SPEECH PATTERNS ----------------###########################
    {
      "tag": "greeting-jp",
      "input": [
        "こんにちは",
        "もしもし",
        "いらっしゃいませ",
        "よ",
        "おはよう ございます",
        "おはよう"
      ],
      "responses": [
        "もしもし <NAME>",
        "こんにちは",
        "こんにちは <NAME>",
        "おはよう ございます <NAME>",
        "おはよう",
        "いらっしゃいませ"
      ]
    },
    {
      "tag": "goodbye-jp",
      "input": [
        "じゃね",
        "またね",
        "じゃまた",
        "バイバイ",
        "また明日",
        "お先に失礼します",
        "また来週",
        "またあした",
        "またらいしゅう",
        "おさきにしつれいします",
        "お先に失礼します"
      ],
      "responses": [
        "じゃね",
        "またね",
        "じゃまた",
        "バイバイ",
        "お先に失礼します",
        "お先に失礼します"
      ]
    },
    {
      "tag": "howami-jp",
      "input": [
        "元気ですか？",
        "おげんきですか？",
        "お元気でしたか？",
        "お変わりありませんか",
        "げんきですか?",
        "おげんきですか？",
        "おげんきでしたか？",
        "おかわりありませんか？"
      ],
      "responses": [
        "元気です",
        "もう元気になりました",
        "健康になりました",
        "もう大丈夫です",
        "まあまあです",
        "そこそこです",
        "まずまずと言った所です",
        "良くも悪くもありません",
        "少し疲れています",
        "気分が優れません"
      ]
    }
  ]
}
