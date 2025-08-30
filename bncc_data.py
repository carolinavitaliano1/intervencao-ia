# bncc_data.py
# Este arquivo contém a estrutura completa da BNCC para Educação Infantil, Ensino Fundamental e Ensino Médio.

BNCC_DATABASE = {
    "Educação Infantil": {
        "Bebês (zero a 1 ano e 6 meses)": {
            "O eu, o outro e o nós": [{"codigo": "EI01EO01", "descricao": "Perceber que suas ações têm efeitos nas outras crianças e nos adultos."}],
            "Corpo, gestos e movimentos": [{"codigo": "EI01CG02", "descricao": "Experimentar as possibilidades corporais nas brincadeiras e interações em ambientes acolhedores e desafiantes."}],
            "Traços, sons, cores e formas": [{"codigo": "EI01TS01", "descricao": "Explorar sons produzidos com o próprio corpo e com objetos do ambiente."}],
            "Escuta, fala, pensamento e imaginação": [{"codigo": "EI01EF01", "descricao": "Reconhecer quando é chamado por seu nome e reconhecer os nomes de pessoas com quem convive."}],
            "Espaços, tempos, quantidades, relações e transformações": [{"codigo": "EI01ET01", "descricao": "Explorar e descobrir as propriedades de objetos e materiais (odor, cor, sabor, temperatura)."}],
        },
        "Crianças bem pequenas (1 ano e 7 meses a 3 anos e 11 meses)": {
            "O eu, o outro e o nós": [{"codigo": "EI02EO04", "descricao": "Comunicar-se com outras crianças e adultos, utilizando diferentes linguagens (oral, corporal, etc.)."}],
            "Corpo, gestos e movimentos": [{"codigo": "EI02CG01", "descricao": "Apropriar-se de gestos e movimentos de sua cultura no cuidado de si e nos jogos e brincadeiras."}],
            "Traços, sons, cores e formas": [{"codigo": "EI02TS02", "descricao": "Utilizar materiais variados com possibilidades de manipulação (argila, massa de modelar), explorando cores, texturas, superfícies, etc."}],
            "Escuta, fala, pensamento e imaginação": [{"codigo": "EI02EF04", "descricao": "Formular e responder perguntas, desenvolvendo a curiosidade sobre o mundo."}],
            "Espaços, tempos, quantidades, relações e transformações": [{"codigo": "EI02ET05", "descricao": "Classificar objetos, considerando determinado atributo (tamanho, peso, cor, forma etc.)."}],
        },
        "Crianças pequenas (4 anos a 5 anos e 11 meses)": {
            "O eu, o outro e o nós": [{"codigo": "EI03EO03", "descricao": "Ampliar as relações interpessoais, desenvolvendo atitudes de participação e cooperação."}],
            "Corpo, gestos e movimentos": [{"codigo": "EI03CG02", "descricao": "Criar com o corpo formas diversificadas de expressão de sentimentos, sensações e emoções."}],
            "Traços, sons, cores e formas": [{"codigo": "EI03TS02", "descricao": "Expressar-se livremente por meio de desenho, pintura, colagem, dobradura e escultura."}],
            "Escuta, fala, pensamento e imaginação": [{"codigo": "EI03EF01", "descricao": "Expressar ideias, desejos e sentimentos sobre suas vivências, por meio da linguagem oral e escrita (escrita espontânea)."}],
            "Espaços, tempos, quantidades, relações e transformações": [{"codigo": "EI03ET07", "descricao": "Relacionar números às suas respectivas quantidades e identificar o antes, o depois e o entre em uma sequência."}],
        }
    },
    "Ensino Fundamental": {
        "1º Ano": {"Língua Portuguesa": [{"codigo": "EF15LP01", "descricao": "Identificar a função social de textos que circulam em campo da vida social dos quais participa cotidianamente."}], "Matemática": [{"codigo": "EF01MA01", "descricao": "Utilizar números naturais como indicador de quantidade ou de ordem em diferentes situações cotidianas."}]},
        "2º Ano": {"Língua Portuguesa": [{"codigo": "EF12LP01", "descricao": "Ler palavras novas com precisão na decodificação."}], "Matemática": [{"codigo": "EF02MA06", "descricao": "Resolver e elaborar problemas de adição e de subtração."}]},
        "3º Ano": {"Língua Portuguesa": [{"codigo": "EF35LP03", "descricao": "Identificar a ideia central do texto, demonstrando compreensão global."}], "Matemática": [{"codigo": "EF03MA07", "descricao": "Resolver e elaborar problemas de multiplicação."}], "Ciências": [{"codigo": "EF03CI04", "descricao": "Identificar características sobre o modo de vida dos animais."}]},
        "4º Ano": {"Língua Portuguesa": [{"codigo": "EF35LP09", "descricao": "Organizar o texto em unidades de sentido, dividindo-o em parágrafos."}], "Matemática": [{"codigo": "EF04MA06", "descricao": "Resolver e elaborar problemas envolvendo diferentes significados da multiplicação."}]},
        "5º Ano": {"Língua Portuguesa": [{"codigo": "EF05LP03", "descricao": "Localizar e inferir informações em textos de diferentes gêneros."}], "Matemática": [{"codigo": "EF05MA08", "descricao": "Resolver e elaborar problemas de multiplicação e divisão com números naturais e racionais."}]},
        "6º Ano": {"Língua Portuguesa": [{"codigo": "EF67LP14", "descricao": "Diferenciar, em textos, fatos de opiniões."}], "Matemática": [{"codigo": "EF06MA13", "descricao": "Resolver e elaborar problemas que envolvam porcentagens."}], "História": [{"codigo": "EF06HI03", "descricao": "Identificar as hipóteses científicas sobre o surgimento da espécie humana."}]},
        "7º Ano": {"Matemática": [{"codigo": "EF07MA17", "descricao": "Resolver e elaborar problemas que envolvam variação de proporcionalidade direta e inversa."}], "Geografia": [{"codigo": "EF07GE01", "descricao": "Avaliar ideias e estereótipos acerca das paisagens e da formação territorial do Brasil."}]},
        "8º Ano": {"Matemática": [{"codigo": "EF08MA07", "descricao": "Resolver e elaborar problemas que possam ser representados por sistemas de equações de 1º grau."}], "Ciências": [{"codigo": "EF08CI01", "descricao": "Identificar e classificar diferentes fontes de energia (renováveis e não renováveis)."}]},
        "9º Ano": {"Língua Portuguesa": [{"codigo": "EF89LP04", "descricao": "Identificar e avaliar teses/opiniões/posicionamentos explícitos e implícitos em textos argumentativos."}], "Matemática": [{"codigo": "EF09MA05", "descricao": "Resolver e elaborar problemas que envolvam porcentagens (juros simples e compostos, acréscimos e decréscimos)."}]}
    },
    "Ensino Médio": {
        "Linguagens e suas Tecnologias": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Compreender o funcionamento das diferentes linguagens e práticas culturais (artísticas, corporais e verbais) e mobilizar esses conhecimentos na recepção e produção de discursos nos diferentes campos de atuação social."},
                {"codigo": 2, "descricao": "Compreender os processos identitários, conflitos e relações de poder que permeiam as práticas sociais de linguagem, respeitando as diversidades e a pluralidade de ideias e posições."},
                {"codigo": 7, "descricao": "Mobilizar práticas de linguagem no universo digital, considerando as dimensões técnicas, críticas, criativas, éticas e estéticas, para expandir as formas de produzir sentidos."}
            ],
            "Habilidades": [
                {"codigo": "EM13LGG101", "descricao": "Compreender e analisar processos de produção e circulação de discursos, nas diferentes linguagens, para fazer escolhas fundamentadas em função de interesses pessoais e coletivos."},
                {"codigo": "EM13LGG102", "descricao": "Analisar visões de mundo, conflitos de interesse, preconceitos e ideologias presentes nos discursos veiculados nas diferentes mídias."},
                {"codigo": "EM13LGG201", "descricao": "Utilizar as diversas linguagens (artísticas, corporais e verbais) em diferentes contextos, valorizando-as como fenômeno social, cultural, histórico, variável, heterogêneo e sensível aos contextos de uso."},
                {"codigo": "EM13LGG301", "descricao": "Participar de processos de produção individual e colaborativa em diferentes linguagens (artísticas, corporais e verbais), levando em conta suas formas e seus funcionamentos."},
                {"codigo": "EM13LP01", "descricao": "Relacionar o texto com suas condições de produção e seu contexto sócio-histórico de circulação (leitor/audiência previstos, objetivos, pontos de vista e perspectivas, etc.)."}
            ]
        },
        "Matemática e suas Tecnologias": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Utilizar estratégias, conceitos e procedimentos matemáticos para interpretar situações em diversos contextos, sejam atividades cotidianas, sejam fatos das Ciências da Natureza e Humanas."},
                {"codigo": 2, "descricao": "Propor ou participar de ações para investigar desafios do mundo contemporâneo e tomar decisões éticas e socialmente responsáveis, com base na análise de problemas sociais."},
                {"codigo": 3, "descricao": "Utilizar estratégias, conceitos, definições e procedimentos matemáticos para interpretar, construir modelos e resolver problemas em diversos contextos."}
            ],
            "Habilidades": [
                {"codigo": "EM13MAT101", "descricao": "Interpretar criticamente situações econômicas, sociais e fatos relativos às Ciências da Natureza que envolvam a variação de grandezas."},
                {"codigo": "EM13MAT202", "descricao": "Analisar e comparar situações que envolvam juros simples e compostos, com o uso de planilhas eletrônicas ou aplicativos."},
                {"codigo": "EM13MAT301", "descricao": "Resolver e elaborar problemas do cotidiano, da Matemática e de outras áreas do conhecimento, que envolvem equações lineares e sistemas lineares."},
                {"codigo": "EM13MAT401", "descricao": "Converter representações algébricas de funções polinomiais de 1º e 2º graus para representações geométricas no plano cartesiano."}
            ]
        },
        "Ciências da Natureza e suas Tecnologias": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Analisar fenômenos naturais e processos tecnológicos, com base nas interações e relações entre matéria e energia, para propor ações individuais e coletivas que aperfeiçoem processos produtivos."},
                {"codigo": 2, "descricao": "Analisar e utilizar interpretações sobre a dinâmica da Vida, da Terra e do Cosmos para elaborar argumentos, realizar previsões sobre o funcionamento e a evolução dos seres vivos e do Universo."},
                {"codigo": 3, "descricao": "Investigar situações-problema e avaliar aplicações do conhecimento científico e tecnológico e suas implicações no mundo."}
            ],
            "Habilidades": [
                {"codigo": "EM13CNT101", "descricao": "Analisar e representar, com ou sem o uso de dispositivos e de aplicativos digitais, as transformações e conservações em sistemas que envolvam quantidade de matéria, de energia e de movimento."},
                {"codigo": "EM13CNT202", "descricao": "Analisar as diversas formas de manifestação da vida em seus diferentes níveis de organização, bem como as condições ambientais favoráveis e os fatores limitantes a elas."},
                {"codigo": "EM13CNT301", "descricao": "Construir questões, elaborar hipóteses, previsões e estimativas, empregar instrumentos de medição e representar e interpretar modelos explicativos para investigar e analisar fenômenos naturais."}
            ]
        },
        "Ciências Humanas e Sociais Aplicadas": {
            "Competências Específicas": [
                {"codigo": 1, "descricao": "Analisar processos políticos, econômicos, sociais, ambientais e culturais nos âmbitos local, regional, nacional e mundial em diferentes tempos."},
                {"codigo": 2, "descricao": "Analisar a formação de territórios e fronteiras em diferentes tempos e espaços, mediante a compreensão das relações de poder que determinam as territorialidades."},
                {"codigo": 6, "descricao": "Participar do debate público de forma crítica, respeitando diferentes posições e fazendo escolhas alinhadas ao exercício da cidadania e ao seu projeto de vida."}
            ],
            "Habilidades": [
                {"codigo": "EM13CHS101", "descricao": "Identificar, analisar e comparar diferentes fontes e narrativas expressas em diversas linguagens, com vistas à compreensão de ideias filosóficas e de processos e eventos históricos, geográficos, políticos, etc."},
                {"codigo": "EM13CHS201", "descricao": "Analisar e caracterizar as dinâmicas das populações, das mercadorias e do capital nos diversos continentes, com destaque para a mobilidade e a fixação de pessoas, grupos humanos e povos."},
                {"codigo": "EM13CHS601", "descricao": "Identificar e analisar as demandas e os protagonismos políticos, sociais e culturais dos povos indígenas e das populações afrodescendentes no Brasil contemporâneo."}
            ]
        }
    }
}
