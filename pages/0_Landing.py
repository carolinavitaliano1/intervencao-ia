<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduInclusiva - Gestão de Aprendizagem Inclusiva</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; }
        .gradient-bg { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .card-hover { transition: all 0.3s ease; }
        .card-hover:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
        .tab-active { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .timeline-item { position: relative; }
        .timeline-item::before { 
            content: ''; 
            position: absolute; 
            left: 15px; 
            top: 40px; 
            bottom: -20px; 
            width: 2px; 
            background: #e5e7eb; 
        }
        .timeline-item:last-child::before { display: none; }
        .fade-in { animation: fadeIn 0.5s ease-in; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .nav-active { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .page-content { display: none; }
        .page-content.active { display: block; }
        .pei-tab-content { display: none; }
        .pei-tab-content.active { display: block; }
        .student-tab-content { display: none; }
        .student-tab-content.active { display: block; }
        .goal-card { transition: all 0.3s ease; border-left: 4px solid transparent; }
        .goal-card.short-term { border-left-color: #10b981; }
        .goal-card.medium-term { border-left-color: #f59e0b; }
        .goal-card.long-term { border-left-color: #8b5cf6; }
        .goal-card:hover { transform: translateX(4px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .progress-ring { transform: rotate(-90deg); }
        .ai-generating { animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .roadmap-item { transition: all 0.3s ease; }
        .roadmap-item:hover { transform: scale(1.02); }
        .roadmap-completed { background: linear-gradient(135deg, #10b981, #059669); }
        .roadmap-in-progress { background: linear-gradient(135deg, #f59e0b, #d97706); }
        .roadmap-planned { background: linear-gradient(135deg, #6b7280, #4b5563); }
        .feature-card { border: 2px solid transparent; transition: all 0.3s ease; }
        .feature-card:hover { border-color: #667eea; transform: translateY(-2px); }
        .priority-high { border-left: 4px solid #ef4444; }
        .priority-medium { border-left: 4px solid #f59e0b; }
        .priority-low { border-left: 4px solid #10b981; }
        .bncc-skill { cursor: pointer; transition: all 0.3s ease; }
        .bncc-skill:hover { background-color: #dbeafe; }
        .bncc-skill.selected { background-color: #3b82f6; color: white; }
    </style>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <header class="gradient-bg text-white shadow-lg">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-white rounded-lg flex items-center justify-center">
                        <span class="text-2xl">🎓</span>
                    </div>
                    <div>
                        <h1 class="text-2xl font-bold">EduInclusiva</h1>
                        <p class="text-sm opacity-90">Gestão de Aprendizagem Inclusiva</p>
                    </div>
                </div>
                <div class="flex items-center space-x-4">
                    <button class="bg-white bg-opacity-20 px-4 py-2 rounded-lg hover:bg-opacity-30 transition-all">
                        <span class="mr-2">🔔</span>
                        Notificações
                    </button>
                    <div class="flex items-center space-x-2">
                        <div class="w-8 h-8 bg-white bg-opacity-20 rounded-full flex items-center justify-center">
                            <span class="text-sm">👩‍🏫</span>
                        </div>
                        <span class="text-sm">Dra. Maria Silva</span>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <div class="flex">
        <!-- Sidebar -->
        <aside class="w-64 bg-white shadow-lg min-h-screen">
            <nav class="p-6">
                <ul class="space-y-2">
                    <li><a href="#" onclick="showPage('dashboard')" id="nav-dashboard" class="nav-active flex items-center space-x-3 p-3 rounded-lg font-medium">
                        <span>📊</span><span>Dashboard</span>
                    </a></li>
                    <li><a href="#" onclick="showPage('alunos')" id="nav-alunos" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>👥</span><span>Alunos</span>
                    </a></li>
                    <li><a href="#" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>📋</span><span>Prontuários</span>
                    </a></li>
                    <li><a href="#" onclick="showPage('pei')" id="nav-pei" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>🎯</span><span>PEIs</span>
                    </a></li>
                    <li><a href="#" onclick="showPage('pedagogico')" id="nav-pedagogico" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>🧠</span><span>Pedagógico IA</span>
                    </a></li>
                    <li><a href="#" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>📚</span><span>Atividades</span>
                    </a></li>
                    <li><a href="#" onclick="showPage('colaboracao')" id="nav-colaboracao" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>👥</span><span>Colaboração</span>
                    </a></li>
                    <li><a href="#" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>📈</span><span>Relatórios</span>
                    </a></li>
                    <li><a href="#" onclick="showPage('roadmap')" id="nav-roadmap" class="flex items-center space-x-3 p-3 rounded-lg hover:bg-gray-50 text-gray-700">
                        <span>🚀</span><span>Roadmap MVP</span>
                    </a></li>
                </ul>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="flex-1">
            <!-- Dashboard Page -->
            <div id="page-dashboard" class="page-content active p-8">
                <!-- Stats Cards -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                    <div class="bg-white p-6 rounded-xl shadow-sm card-hover">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-500 text-sm">Total de Alunos</p>
                                <p class="text-3xl font-bold text-gray-800">1,247</p>
                            </div>
                            <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                                <span class="text-2xl">👥</span>
                            </div>
                        </div>
                        <div class="mt-4 flex items-center text-green-600 text-sm">
                            <span class="mr-1">↗️</span>
                            <span>+12% este mês</span>
                        </div>
                    </div>

                    <div class="bg-white p-6 rounded-xl shadow-sm card-hover">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-500 text-sm">PEIs Ativos</p>
                                <p class="text-3xl font-bold text-gray-800">342</p>
                            </div>
                            <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
                                <span class="text-2xl">🎯</span>
                            </div>
                        </div>
                        <div class="mt-4 flex items-center text-green-600 text-sm">
                            <span class="mr-1">↗️</span>
                            <span>+8% este mês</span>
                        </div>
                    </div>

                    <div class="bg-white p-6 rounded-xl shadow-sm card-hover">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-500 text-sm">Atividades Realizadas</p>
                                <p class="text-3xl font-bold text-gray-800">2,156</p>
                            </div>
                            <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
                                <span class="text-2xl">📚</span>
                            </div>
                        </div>
                        <div class="mt-4 flex items-center text-green-600 text-sm">
                            <span class="mr-1">↗️</span>
                            <span>+23% este mês</span>
                        </div>
                    </div>

                    <div class="bg-white p-6 rounded-xl shadow-sm card-hover">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-gray-500 text-sm">Taxa de Evolução</p>
                                <p class="text-3xl font-bold text-gray-800">87%</p>
                            </div>
                            <div class="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center">
                                <span class="text-2xl">📈</span>
                            </div>
                        </div>
                        <div class="mt-4 flex items-center text-green-600 text-sm">
                            <span class="mr-1">↗️</span>
                            <span>+5% este mês</span>
                        </div>
                    </div>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
                    <!-- Gráfico de Evolução -->
                    <div class="bg-white p-6 rounded-xl shadow-sm">
                        <h3 class="text-lg font-semibold mb-4">Evolução dos Alunos</h3>
                        <canvas id="evolutionChart" width="400" height="200"></canvas>
                    </div>

                    <!-- Alunos Recentes -->
                    <div class="bg-white p-6 rounded-xl shadow-sm">
                        <h3 class="text-lg font-semibold mb-4">Alunos Recentes</h3>
                        <div class="space-y-4">
                            <div class="flex items-center space-x-4 p-3 hover:bg-gray-50 rounded-lg cursor-pointer" onclick="showStudentProfile()">
                                <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                                    <span class="text-sm font-medium">JS</span>
                                </div>
                                <div class="flex-1">
                                    <p class="font-medium">João Silva</p>
                                    <p class="text-sm text-gray-500">TEA - Nível 1</p>
                                </div>
                                <span class="text-green-600 text-sm">Ativo</span>
                            </div>
                            <div class="flex items-center space-x-4 p-3 hover:bg-gray-50 rounded-lg cursor-pointer" onclick="showStudentProfile()">
                                <div class="w-10 h-10 bg-pink-100 rounded-full flex items-center justify-center">
                                    <span class="text-sm font-medium">MS</span>
                                </div>
                                <div class="flex-1">
                                    <p class="font-medium">Maria Santos</p>
                                    <p class="text-sm text-gray-500">TDAH</p>
                                </div>
                                <span class="text-green-600 text-sm">Ativo</span>
                            </div>
                            <div class="flex items-center space-x-4 p-3 hover:bg-gray-50 rounded-lg cursor-pointer" onclick="showStudentProfile()">
                                <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
                                    <span class="text-sm font-medium">PC</span>
                                </div>
                                <div class="flex-1">
                                    <p class="font-medium">Pedro Costa</p>
                                    <p class="text-sm text-gray-500">Dislexia</p>
                                </div>
                                <span class="text-yellow-600 text-sm">Em avaliação</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Ações Rápidas -->
                <div class="bg-white p-6 rounded-xl shadow-sm mb-8">
                    <h3 class="text-lg font-semibold mb-4">Ações Rápidas</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                        <button class="p-4 border-2 border-dashed border-gray-300 rounded-lg hover:border-blue-400 hover:bg-blue-50 transition-all text-center">
                            <div class="text-2xl mb-2">➕</div>
                            <p class="text-sm font-medium">Novo Aluno</p>
                        </button>
                        <button onclick="showPage('pei')" class="p-4 border-2 border-dashed border-gray-300 rounded-lg hover:border-green-400 hover:bg-green-50 transition-all text-center">
                            <div class="text-2xl mb-2">📋</div>
                            <p class="text-sm font-medium">Criar PEI</p>
                        </button>
                        <button onclick="showPage('pedagogico')" class="p-4 border-2 border-dashed border-gray-300 rounded-lg hover:border-purple-400 hover:bg-purple-50 transition-all text-center">
                            <div class="text-2xl mb-2">🧠</div>
                            <p class="text-sm font-medium">Pedagógico IA</p>
                        </button>
                        <button class="p-4 border-2 border-dashed border-gray-300 rounded-lg hover:border-orange-400 hover:bg-orange-50 transition-all text-center">
                            <div class="text-2xl mb-2">📊</div>
                            <p class="text-sm font-medium">Gerar Relatório</p>
                        </button>
                    </div>
                </div>

                <!-- Notificações Recentes -->
                <div class="bg-white p-6 rounded-xl shadow-sm">
                    <h3 class="text-lg font-semibold mb-4">Notificações Recentes</h3>
                    <div class="space-y-3">
                        <div class="flex items-start space-x-3 p-3 bg-blue-50 rounded-lg">
                            <span class="text-blue-600">ℹ️</span>
                            <div>
                                <p class="text-sm font-medium">Novo PEI criado para João Silva</p>
                                <p class="text-xs text-gray-500">Há 2 horas</p>
                            </div>
                        </div>
                        <div class="flex items-start space-x-3 p-3 bg-green-50 rounded-lg">
                            <span class="text-green-600">✅</span>
                            <div>
                                <p class="text-sm font-medium">Atividade concluída por Maria Santos</p>
                                <p class="text-xs text-gray-500">Há 4 horas</p>
                            </div>
                        </div>
                        <div class="flex items-start space-x-3 p-3 bg-yellow-50 rounded-lg">
                            <span class="text-yellow-600">⚠️</span>
                            <div>
                                <p class="text-sm font-medium">Revisão de PEI agendada para Pedro Costa</p>
                                <p class="text-xs text-gray-500">Amanhã às 14h</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Pedagógico IA Page -->
            <div id="page-pedagogico" class="page-content p-8">
                <!-- Header -->
                <div class="gradient-bg text-white p-6 rounded-xl mb-8">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <div class="w-12 h-12 bg-white rounded-lg flex items-center justify-center">
                                <span class="text-2xl">🧠</span>
                            </div>
                            <div>
                                <h1 class="text-3xl font-bold">Pedagógico Inteligente</h1>
                                <p class="text-lg opacity-90">Geração de Atividades com IA baseada na BNCC</p>
                            </div>
                        </div>
                        <div class="flex items-center space-x-4">
                            <button onclick="showTemplateQuick()" class="bg-white bg-opacity-20 px-6 py-3 rounded-lg hover:bg-opacity-30 transition-all font-medium">
                                <span class="mr-2">⚡</span>Templates Rápidos
                            </button>
                            <button onclick="showActivityHistory()" class="bg-white text-purple-600 px-6 py-3 rounded-lg hover:bg-gray-100 transition-all font-medium">
                                <span class="mr-2">📚</span>Histórico
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Main Form -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    <!-- Form Section -->
                    <div class="lg:col-span-2">
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <h3 class="text-xl font-semibold mb-6 flex items-center">
                                <span class="mr-2">📝</span>Configuração da Atividade
                            </h3>

                            <form id="pedagogicoForm" class="space-y-6">
                                <!-- Seleção do Aluno -->
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">Aluno</label>
                                    <select id="alunoSelect" class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                                        <option value="">Selecione um aluno</option>
                                        <option value="joao-silva">João Silva Santos - TEA Nível 1 (3º Ano)</option>
                                        <option value="maria-santos">Maria Santos - TDAH (4º Ano)</option>
                                        <option value="pedro-costa">Pedro Costa - Dislexia (2º Ano)</option>
                                    </select>
                                </div>

                                <!-- Busca BNCC -->
                                <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
                                    <h4 class="font-semibold text-blue-800 mb-4 flex items-center">
                                        <span class="mr-2">🎯</span>Busca BNCC por Habilidade/Ano
                                    </h4>
                                    
                                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
                                        <div>
                                            <label class="block text-sm font-medium text-blue-700 mb-2">Ano Escolar</label>
                                            <select id="anoSelect" onchange="loadBNCCSkills()" class="w-full border border-blue-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-500">
                                                <option value="">Selecione o ano</option>
                                                <option value="1">1º Ano</option>
                                                <option value="2">2º Ano</option>
                                                <option value="3">3º Ano</option>
                                                <option value="4">4º Ano</option>
                                                <option value="5">5º Ano</option>
                                                <option value="6">6º Ano</option>
                                                <option value="7">7º Ano</option>
                                                <option value="8">8º Ano</option>
                                                <option value="9">9º Ano</option>
                                            </select>
                                        </div>
                                        <div>
                                            <label class="block text-sm font-medium text-blue-700 mb-2">Disciplina</label>
                                            <select id="disciplinaSelect" onchange="loadBNCCSkills()" class="w-full border border-blue-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-500">
                                                <option value="">Selecione a disciplina</option>
                                                <option value="portugues">Língua Portuguesa</option>
                                                <option value="matematica">Matemática</option>
                                                <option value="ciencias">Ciências</option>
                                                <option value="historia">História</option>
                                                <option value="geografia">Geografia</option>
                                                <option value="arte">Arte</option>
                                                <option value="educacao-fisica">Educação Física</option>
                                            </select>
                                        </div>
                                    </div>

                                    <div>
                                        <label class="block text-sm font-medium text-blue-700 mb-2">Habilidade BNCC Selecionada</label>
                                        <div id="bnccSkillsContainer" class="min-h-[100px] border border-blue-300 rounded-lg p-3 bg-white">
                                            <p class="text-gray-500 text-center py-8">Selecione o ano e disciplina para ver as habilidades disponíveis</p>
                                        </div>
                                        <input type="hidden" id="selectedBNCC" name="selectedBNCC">
                                    </div>
                                </div>

                                <!-- Campos Específicos -->
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">Transtorno em Questão</label>
                                        <select id="transtornoSelect" class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500">
                                            <option value="">Selecione o transtorno</option>
                                            <option value="tea">TEA - Transtorno do Espectro Autista</option>
                                            <option value="tdah">TDAH - Déficit de Atenção e Hiperatividade</option>
                                            <option value="dislexia">Dislexia</option>
                                            <option value="di">Deficiência Intelectual</option>
                                            <option value="down">Síndrome de Down</option>
                                            <option value="outros">Outros</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-2">Escolaridade Atual</label>
                                        <select id="escolaridadeSelect" class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500">
                                            <option value="">Nível de desenvolvimento</option>
                                            <option value="pre-silabico">Pré-silábico</option>
                                            <option value="silabico">Silábico</option>
                                            <option value="silabico-alfabetico">Silábico-alfabético</option>
                                            <option value="alfabetico">Alfabético</option>
                                            <option value="adequado">Adequado para a idade</option>
                                            <option value="acima">Acima da média</option>
                                        </select>
                                    </div>
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">Pontos Fortes do Aluno</label>
                                    <textarea id="pontosFortesText" rows="3" class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="Ex: Excelente memória visual, interesse por dinossauros, habilidade com números..."></textarea>
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">Observações do Dia</label>
                                    <textarea id="observacoesDiaText" rows="3" class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="Ex: Hoje está mais agitado, teve dificuldade com barulho, mostrou interesse em atividade de arte..."></textarea>
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">Reforçadores (Motivadores)</label>
                                    <textarea id="reforcadoresText" rows="2" class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="Ex: Dinossauros, música, jogos no tablet, elogios verbais, adesivos..."></textarea>
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">Áreas a Trabalhar</label>
                                    <textarea id="areasTrabalharText" rows="3" class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:ring-2 focus:ring-blue-500" placeholder="Ex: Comunicação verbal, interação social, coordenação motora fina, atenção sustentada..."></textarea>
                                </div>

                                <!-- Tipo de Atividade -->
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-3">Formato da Atividade</label>
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                                        <label class="flex items-center p-4 border-2 border-gray-200 rounded-lg cursor-pointer hover:border-blue-400 transition-all">
                                            <input type="radio" name="tipoAtividade" value="ficha" class="mr-3">
                                            <div>
                                                <div class="font-medium">📄 Ficha de Atividade</div>
                                                <div class="text-sm text-gray-500">Exercícios estruturados</div>
                                            </div>
                                        </label>
                                        <label class="flex items-center p-4 border-2 border-gray-200 rounded-lg cursor-pointer hover:border-blue-400 transition-all">
                                            <input type="radio" name="tipoAtividade" value="jogo" class="mr-3">
                                            <div>
                                                <div class="font-medium">🎮 Jogo/Dinâmica</div>
                                                <div class="text-sm text-gray-500">Atividade lúdica</div>
                                            </div>
                                        </label>
                                        <label class="flex items-center p-4 border-2 border-gray-200 rounded-lg cursor-pointer hover:border-blue-400 transition-all">
                                            <input type="radio" name="tipoAtividade" value="roteiro" class="mr-3">
                                            <div>
                                                <div class="font-medium">🏠 Roteiro Família</div>
                                                <div class="text-sm text-gray-500">Orientações para casa</div>
                                            </div>
                                        </label>
                                    </div>
                                </div>

                                <!-- Botão Principal -->
                                <div class="text-center pt-6">
                                    <button type="button" onclick="generateActivity()" class="bg-gradient-to-r from-purple-600 to-blue-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:from-purple-700 hover:to-blue-700 transition-all transform hover:scale-105 shadow-lg">
                                        <span class="mr-3">🤖</span>Gerar/Adaptar Atividade com IA
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>

                    <!-- Sidebar -->
                    <div class="space-y-6">
                        <!-- Templates Rápidos -->
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <h3 class="text-lg font-semibold mb-4 flex items-center">
                                <span class="mr-2">⚡</span>Templates Rápidos
                            </h3>
                            <div class="space-y-3">
                                <button onclick="loadTemplate('tea')" class="w-full bg-blue-50 border border-blue-200 text-blue-800 p-3 rounded-lg hover:bg-blue-100 transition-all text-left">
                                    <div class="font-medium">🧩 TEA - Comunicação</div>
                                    <div class="text-sm opacity-75">Atividades de interação social</div>
                                </button>
                                <button onclick="loadTemplate('tdah')" class="w-full bg-orange-50 border border-orange-200 text-orange-800 p-3 rounded-lg hover:bg-orange-100 transition-all text-left">
                                    <div class="font-medium">⚡ TDAH - Atenção</div>
                                    <div class="text-sm opacity-75">Foco e concentração</div>
                                </button>
                                <button onclick="loadTemplate('dislexia')" class="w-full bg-green-50 border border-green-200 text-green-800 p-3 rounded-lg hover:bg-green-100 transition-all text-left">
                                    <div class="font-medium">📖 Dislexia - Leitura</div>
                                    <div class="text-sm opacity-75">Processamento fonológico</div>
                                </button>
                            </div>
                        </div>

                        <!-- Estatísticas -->
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <h3 class="text-lg font-semibold mb-4 flex items-center">
                                <span class="mr-2">📊</span>Estatísticas
                            </h3>
                            <div class="space-y-3">
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-600">Atividades Geradas</span>
                                    <span class="text-2xl font-bold text-blue-600">127</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-600">Esta Semana</span>
                                    <span class="text-2xl font-bold text-green-600">23</span>
                                </div>
                                <div class="flex items-center justify-between">
                                    <span class="text-gray-600">Mais Usada</span>
                                    <span class="text-sm font-medium text-purple-600">Ficha TEA</span>
                                </div>
                            </div>
                        </div>

                        <!-- Atividades Recentes -->
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <h3 class="text-lg font-semibold mb-4 flex items-center">
                                <span class="mr-2">🕒</span>Recentes
                            </h3>
                            <div class="space-y-3">
                                <div class="border border-gray-200 rounded-lg p-3 hover:bg-gray-50 cursor-pointer">
                                    <div class="font-medium text-sm">Matemática - Números</div>
                                    <div class="text-xs text-gray-500">João Silva • Hoje</div>
                                </div>
                                <div class="border border-gray-200 rounded-lg p-3 hover:bg-gray-50 cursor-pointer">
                                    <div class="font-medium text-sm">Português - Alfabeto</div>
                                    <div class="text-xs text-gray-500">Maria Santos • Ontem</div>
                                </div>
                                <div class="border border-gray-200 rounded-lg p-3 hover:bg-gray-50 cursor-pointer">
                                    <div class="font-medium text-sm">Ciências - Animais</div>
                                    <div class="text-xs text-gray-500">Pedro Costa • 2 dias</div>
                                </div>
                            </div>
                        </div>

                        <!-- Dicas -->
                        <div class="bg-gradient-to-br from-yellow-50 to-orange-50 border border-yellow-200 rounded-xl p-6">
                            <h3 class="text-lg font-semibold mb-3 flex items-center text-orange-800">
                                <span class="mr-2">💡</span>Dica Inteligente
                            </h3>
                            <p class="text-orange-700 text-sm">
                                Para melhores resultados, seja específico nos pontos fortes e reforçadores. 
                                A IA usa essas informações para personalizar as atividades!
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Other pages would continue here... -->
            <div id="page-alunos" class="page-content">
                <div class="p-8">
                    <h2 class="text-2xl font-bold mb-6">Gestão de Alunos</h2>
                    <p class="text-gray-600">Módulo de alunos em desenvolvimento...</p>
                </div>
            </div>

            <div id="page-pei" class="page-content">
                <div class="p-8">
                    <h2 class="text-2xl font-bold mb-6">Planos Educacionais Individualizados</h2>
                    <p class="text-gray-600">Módulo de PEIs em desenvolvimento...</p>
                </div>
            </div>

            <!-- Colaboração Multidisciplinar Page -->
            <div id="page-colaboracao" class="page-content p-8">
                <!-- Header -->
                <div class="gradient-bg text-white p-6 rounded-xl mb-8">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <div class="w-12 h-12 bg-white rounded-lg flex items-center justify-center">
                                <span class="text-2xl">👥</span>
                            </div>
                            <div>
                                <h1 class="text-3xl font-bold">Colaboração Multidisciplinar</h1>
                                <p class="text-lg opacity-90">Comunicação integrada entre profissionais</p>
                            </div>
                        </div>
                        <div class="flex items-center space-x-4">
                            <button onclick="scheduleNewMeeting()" class="bg-white bg-opacity-20 px-6 py-3 rounded-lg hover:bg-opacity-30 transition-all font-medium">
                                <span class="mr-2">📅</span>Nova Reunião
                            </button>
                            <button onclick="showNotifications()" class="bg-white text-purple-600 px-6 py-3 rounded-lg hover:bg-gray-100 transition-all font-medium relative">
                                <span class="mr-2">🔔</span>Notificações
                                <span class="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">3</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Main Layout -->
                <div class="grid grid-cols-1 lg:grid-cols-4 gap-8">
                    <!-- Chat Section -->
                    <div class="lg:col-span-2">
                        <div class="bg-white rounded-xl shadow-sm h-[600px] flex flex-col">
                            <!-- Chat Header -->
                            <div class="p-4 border-b border-gray-200">
                                <div class="flex items-center justify-between">
                                    <div class="flex items-center space-x-3">
                                        <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                                            <span class="text-sm font-medium">JS</span>
                                        </div>
                                        <div>
                                            <h3 class="font-semibold">João Silva Santos</h3>
                                            <p class="text-sm text-gray-500">Equipe: 5 profissionais online</p>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <button onclick="showTeamMembers()" class="text-gray-400 hover:text-gray-600">
                                            <span class="text-lg">👥</span>
                                        </button>
                                        <button onclick="showChatHistory()" class="text-gray-400 hover:text-gray-600">
                                            <span class="text-lg">📋</span>
                                        </button>
                                    </div>
                                </div>
                            </div>

                            <!-- Chat Messages -->
                            <div id="chatMessages" class="flex-1 overflow-y-auto p-4 space-y-4">
                                <!-- Message 1 -->
                                <div class="flex items-start space-x-3">
                                    <div class="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center flex-shrink-0">
                                        <span class="text-xs font-medium">PS</span>
                                    </div>
                                    <div class="flex-1">
                                        <div class="flex items-center space-x-2 mb-1">
                                            <span class="font-medium text-sm">Dra. Paula Santos</span>
                                            <span class="text-xs text-gray-500">Psicóloga</span>
                                            <span class="text-xs text-gray-400">09:15</span>
                                        </div>
                                        <div class="bg-gray-100 rounded-lg p-3">
                                            <p class="text-sm">Bom dia equipe! Observei que o João teve uma melhora significativa na interação social durante nossa sessão de ontem. Ele iniciou conversas espontâneas pela primeira vez. 🎉</p>
                                        </div>
                                        <div class="flex items-center space-x-4 mt-2">
                                            <button class="text-xs text-gray-500 hover:text-blue-600">👍 2</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Responder</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Comentar no registro</button>
                                        </div>
                                    </div>
                                </div>

                                <!-- Message 2 -->
                                <div class="flex items-start space-x-3">
                                    <div class="w-8 h-8 bg-purple-100 rounded-full flex items-center justify-center flex-shrink-0">
                                        <span class="text-xs font-medium">MS</span>
                                    </div>
                                    <div class="flex-1">
                                        <div class="flex items-center space-x-2 mb-1">
                                            <span class="font-medium text-sm">Dra. Maria Silva</span>
                                            <span class="text-xs text-gray-500">Pedagoga</span>
                                            <span class="text-xs text-gray-400">09:32</span>
                                        </div>
                                        <div class="bg-gray-100 rounded-lg p-3">
                                            <p class="text-sm">Excelente notícia <span class="text-blue-600 font-medium">@Paula Santos</span>! Isso alinha com o que observei em sala. Ele está mais participativo nas atividades em grupo. Vou ajustar o PEI para incluir mais oportunidades de interação.</p>
                                        </div>
                                        <div class="flex items-center space-x-4 mt-2">
                                            <button class="text-xs text-gray-500 hover:text-blue-600">👍 1</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Responder</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Adicionar ao PEI</button>
                                        </div>
                                    </div>
                                </div>

                                <!-- Message 3 -->
                                <div class="flex items-start space-x-3">
                                    <div class="w-8 h-8 bg-orange-100 rounded-full flex items-center justify-center flex-shrink-0">
                                        <span class="text-xs font-medium">CF</span>
                                    </div>
                                    <div class="flex-1">
                                        <div class="flex items-center space-x-2 mb-1">
                                            <span class="font-medium text-sm">Carlos Ferreira</span>
                                            <span class="text-xs text-gray-500">Fonoaudiólogo</span>
                                            <span class="text-xs text-gray-400">10:15</span>
                                        </div>
                                        <div class="bg-gray-100 rounded-lg p-3">
                                            <p class="text-sm">Perfeito timing! Estou trabalhando comunicação funcional com ele. Podemos agendar uma reunião para alinhar estratégias? Tenho algumas sugestões de atividades que podem potencializar esse progresso.</p>
                                        </div>
                                        <div class="bg-blue-50 border border-blue-200 rounded-lg p-2 mt-2">
                                            <div class="flex items-center space-x-2">
                                                <span class="text-blue-600 text-sm">📅</span>
                                                <span class="text-sm text-blue-800">Proposta de reunião: Sexta, 14h - Estratégias de Comunicação</span>
                                            </div>
                                            <div class="flex space-x-2 mt-2">
                                                <button class="bg-blue-600 text-white px-3 py-1 rounded text-xs hover:bg-blue-700">Aceitar</button>
                                                <button class="bg-gray-200 text-gray-700 px-3 py-1 rounded text-xs hover:bg-gray-300">Propor outro horário</button>
                                            </div>
                                        </div>
                                        <div class="flex items-center space-x-4 mt-2">
                                            <button class="text-xs text-gray-500 hover:text-blue-600">👍</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Responder</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Ver agenda</button>
                                        </div>
                                    </div>
                                </div>

                                <!-- System Message -->
                                <div class="flex justify-center">
                                    <div class="bg-yellow-50 border border-yellow-200 rounded-lg px-4 py-2">
                                        <p class="text-xs text-yellow-800">
                                            <span class="mr-1">📝</span>
                                            <strong>Dra. Maria Silva</strong> adicionou uma anotação ao registro de João Silva
                                            <button class="text-yellow-600 underline ml-1">Ver anotação</button>
                                        </p>
                                    </div>
                                </div>

                                <!-- Message 4 -->
                                <div class="flex items-start space-x-3">
                                    <div class="w-8 h-8 bg-pink-100 rounded-full flex items-center justify-center flex-shrink-0">
                                        <span class="text-xs font-medium">AS</span>
                                    </div>
                                    <div class="flex-1">
                                        <div class="flex items-center space-x-2 mb-1">
                                            <span class="font-medium text-sm">Ana Silva</span>
                                            <span class="text-xs text-gray-500">Terapeuta Ocupacional</span>
                                            <span class="text-xs text-gray-400">11:20</span>
                                        </div>
                                        <div class="bg-gray-100 rounded-lg p-3">
                                            <p class="text-sm">Ótimas observações pessoal! Na TO também notei melhora na coordenação motora fina. Ele conseguiu completar atividades de recorte que antes eram desafiadoras. Vou documentar isso no prontuário.</p>
                                        </div>
                                        <div class="bg-green-50 border border-green-200 rounded-lg p-2 mt-2">
                                            <div class="flex items-center space-x-2">
                                                <span class="text-green-600 text-sm">📊</span>
                                                <span class="text-sm text-green-800">Progresso registrado: Coordenação motora fina +15%</span>
                                            </div>
                                        </div>
                                        <div class="flex items-center space-x-4 mt-2">
                                            <button class="text-xs text-gray-500 hover:text-blue-600">👍 3</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Responder</button>
                                            <button class="text-xs text-gray-500 hover:text-blue-600">Ver prontuário</button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Chat Input -->
                            <div class="p-4 border-t border-gray-200">
                                <div class="flex items-center space-x-3">
                                    <div class="flex-1">
                                        <div class="relative">
                                            <input type="text" id="chatInput" placeholder="Digite sua mensagem... Use @ para mencionar alguém" class="w-full border border-gray-300 rounded-lg px-4 py-3 pr-12 focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                                            <button onclick="sendMessage()" class="absolute right-2 top-1/2 transform -translate-y-1/2 text-blue-600 hover:text-blue-700">
                                                <span class="text-xl">📤</span>
                                            </button>
                                        </div>
                                    </div>
                                    <button onclick="attachFile()" class="text-gray-400 hover:text-gray-600">
                                        <span class="text-xl">📎</span>
                                    </button>
                                    <button onclick="recordAudio()" class="text-gray-400 hover:text-gray-600">
                                        <span class="text-xl">🎤</span>
                                    </button>
                                </div>
                                <div class="flex items-center space-x-4 mt-2 text-xs text-gray-500">
                                    <button onclick="mentionUser()" class="hover:text-blue-600">@ Mencionar</button>
                                    <button onclick="addToRecord()" class="hover:text-blue-600">📝 Adicionar ao registro</button>
                                    <button onclick="scheduleFromChat()" class="hover:text-blue-600">📅 Agendar reunião</button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Sidebar -->
                    <div class="lg:col-span-2 space-y-6">
                        <!-- Team Members -->
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <h3 class="text-lg font-semibold mb-4 flex items-center">
                                <span class="mr-2">👥</span>Equipe Multidisciplinar
                            </h3>
                            <div class="space-y-3">
                                <div class="flex items-center justify-between p-3 bg-green-50 border border-green-200 rounded-lg">
                                    <div class="flex items-center space-x-3">
                                        <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
                                            <span class="text-sm font-medium">PS</span>
                                        </div>
                                        <div>
                                            <p class="font-medium text-sm">Dra. Paula Santos</p>
                                            <p class="text-xs text-gray-500">Psicóloga • Coordenadora</p>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                                        <span class="text-xs text-green-600">Online</span>
                                    </div>
                                </div>

                                <div class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg">
                                    <div class="flex items-center space-x-3">
                                        <div class="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center">
                                            <span class="text-sm font-medium">MS</span>
                                        </div>
                                        <div>
                                            <p class="font-medium text-sm">Dra. Maria Silva</p>
                                            <p class="text-xs text-gray-500">Pedagoga</p>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                                        <span class="text-xs text-green-600">Online</span>
                                    </div>
                                </div>

                                <div class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg">
                                    <div class="flex items-center space-x-3">
                                        <div class="w-10 h-10 bg-orange-100 rounded-full flex items-center justify-center">
                                            <span class="text-sm font-medium">CF</span>
                                        </div>
                                        <div>
                                            <p class="font-medium text-sm">Carlos Ferreira</p>
                                            <p class="text-xs text-gray-500">Fonoaudiólogo</p>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                                        <span class="text-xs text-green-600">Online</span>
                                    </div>
                                </div>

                                <div class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg">
                                    <div class="flex items-center space-x-3">
                                        <div class="w-10 h-10 bg-pink-100 rounded-full flex items-center justify-center">
                                            <span class="text-sm font-medium">AS</span>
                                        </div>
                                        <div>
                                            <p class="font-medium text-sm">Ana Silva</p>
                                            <p class="text-xs text-gray-500">Terapeuta Ocupacional</p>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2 h-2 bg-green-500 rounded-full"></span>
                                        <span class="text-xs text-green-600">Online</span>
                                    </div>
                                </div>

                                <div class="flex items-center justify-between p-3 hover:bg-gray-50 rounded-lg">
                                    <div class="flex items-center space-x-3">
                                        <div class="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                                            <span class="text-sm font-medium">RF</span>
                                        </div>
                                        <div>
                                            <p class="font-medium text-sm">Dr. Roberto Farias</p>
                                            <p class="text-xs text-gray-500">Neurologista</p>
                                        </div>
                                    </div>
                                    <div class="flex items-center space-x-2">
                                        <span class="w-2 h-2 bg-yellow-500 rounded-full"></span>
                                        <span class="text-xs text-yellow-600">Ausente</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Próximas Reuniões -->
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <h3 class="text-lg font-semibold mb-4 flex items-center">
                                <span class="mr-2">📅</span>Próximas Reuniões
                            </h3>
                            <div class="space-y-3">
                                <div class="border border-blue-200 bg-blue-50 rounded-lg p-4">
                                    <div class="flex items-center justify-between mb-2">
                                        <h4 class="font-medium text-blue-800">Revisão de PEI - João Silva</h4>
                                        <span class="text-xs text-blue-600 bg-blue-100 px-2 py-1 rounded">Hoje</span>
                                    </div>
                                    <p class="text-sm text-blue-700 mb-2">14:00 - 15:00 • Sala de Reuniões Virtual</p>
                                    <div class="flex items-center space-x-2 mb-3">
                                        <div class="flex -space-x-1">
                                            <div class="w-6 h-6 bg-green-100 rounded-full border-2 border-white flex items-center justify-center">
                                                <span class="text-xs">PS</span>
                                            </div>
                                            <div class="w-6 h-6 bg-purple-100 rounded-full border-2 border-white flex items-center justify-center">
                                                <span class="text-xs">MS</span>
                                            </div>
                                            <div class="w-6 h-6 bg-orange-100 rounded-full border-2 border-white flex items-center justify-center">
                                                <span class="text-xs">CF</span>
                                            </div>
                                        </div>
                                        <span class="text-xs text-blue-600">+2 participantes</span>
                                    </div>
                                    <div class="flex space-x-2">
                                        <button class="bg-blue-600 text-white px-3 py-1 rounded text-xs hover:bg-blue-700">Entrar</button>
                                        <button class="bg-blue-100 text-blue-600 px-3 py-1 rounded text-xs hover:bg-blue-200">Ver agenda</button>
                                    </div>
                                </div>

                                <div class="border border-gray-200 rounded-lg p-4">
                                    <div class="flex items-center justify-between mb-2">
                                        <h4 class="font-medium">Estratégias de Comunicação</h4>
                                        <span class="text-xs text-gray-600 bg-gray-100 px-2 py-1 rounded">Sexta</span>
                                    </div>
                                    <p class="text-sm text-gray-600 mb-2">14:00 - 15:00 • Proposta de Carlos Ferreira</p>
                                    <div class="flex items-center space-x-2 mb-3">
                                        <div class="flex -space-x-1">
                                            <div class="w-6 h-6 bg-orange-100 rounded-full border-2 border-white flex items-center justify-center">
                                                <span class="text-xs">CF</span>
                                            </div>
                                            <div class="w-6 h-6 bg-purple-100 rounded-full border-2 border-white flex items-center justify-center">
                                                <span class="text-xs">MS</span>
                                            </div>
                                        </div>
                                        <span class="text-xs text-gray-500">Aguardando confirmação</span>
                                    </div>
                                    <div class="flex space-x-2">
                                        <button class="bg-green-600 text-white px-3 py-1 rounded text-xs hover:bg-green-700">Aceitar</button>
                                        <button class="bg-gray-200 text-gray-700 px-3 py-1 rounded text-xs hover:bg-gray-300">Reagendar</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Anotações Compartilhadas -->
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="text-lg font-semibold flex items-center">
                                    <span class="mr-2">📝</span>Anotações Compartilhadas
                                </h3>
                                <button onclick="addSharedNote()" class="text-blue-600 hover:text-blue-700 text-sm">
                                    + Nova anotação
                                </button>
                            </div>
                            <div class="space-y-3">
                                <div class="border border-green-200 bg-green-50 rounded-lg p-3">
                                    <div class="flex items-center justify-between mb-2">
                                        <div class="flex items-center space-x-2">
                                            <span class="text-green-600 text-sm">📊</span>
                                            <span class="font-medium text-sm">Progresso Semanal</span>
                                        </div>
                                        <span class="text-xs text-green-600">Dra. Paula Santos</span>
                                    </div>
                                    <p class="text-sm text-green-700">João demonstrou melhora significativa na interação social. Recomendo manter estratégias atuais e incluir mais atividades em grupo.</p>
                                    <div class="flex items-center space-x-3 mt-2 text-xs text-green-600">
                                        <span>Hoje, 09:30</span>
                                        <button class="hover:underline">Comentar</button>
                                        <button class="hover:underline">Adicionar ao PEI</button>
                                    </div>
                                </div>

                                <div class="border border-blue-200 bg-blue-50 rounded-lg p-3">
                                    <div class="flex items-center justify-between mb-2">
                                        <div class="flex items-center space-x-2">
                                            <span class="text-blue-600 text-sm">🎯</span>
                                            <span class="font-medium text-sm">Objetivos Revisados</span>
                                        </div>
                                        <span class="text-xs text-blue-600">Dra. Maria Silva</span>
                                    </div>
                                    <p class="text-sm text-blue-700">Ajustei os objetivos do PEI baseado no progresso observado. Foco agora em comunicação funcional e autonomia.</p>
                                    <div class="flex items-center space-x-3 mt-2 text-xs text-blue-600">
                                        <span>Ontem, 16:45</span>
                                        <button class="hover:underline">Ver PEI</button>
                                        <button class="hover:underline">Comentar</button>
                                    </div>
                                </div>

                                <div class="border border-orange-200 bg-orange-50 rounded-lg p-3">
                                    <div class="flex items-center justify-between mb-2">
                                        <div class="flex items-center space-x-2">
                                            <span class="text-orange-600 text-sm">🗣️</span>
                                            <span class="font-medium text-sm">Estratégias de Fala</span>
                                        </div>
                                        <span class="text-xs text-orange-600">Carlos Ferreira</span>
                                    </div>
                                    <p class="text-sm text-orange-700">Implementar técnicas de comunicação alternativa. João responde bem a pictogramas e gestos.</p>
                                    <div class="flex items-center space-x-3 mt-2 text-xs text-orange-600">
                                        <span>2 dias atrás</span>
                                        <button class="hover:underline">Ver técnicas</button>
                                        <button class="hover:underline">Comentar</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Permissões e Acesso -->
                        <div class="bg-white rounded-xl shadow-sm p-6">
                            <h3 class="text-lg font-semibold mb-4 flex items-center">
                                <span class="mr-2">🔐</span>Controle de Acesso
                            </h3>
                            <div class="space-y-3">
                                <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                                    <div>
                                        <p class="font-medium text-sm">Coordenador</p>
                                        <p class="text-xs text-gray-500">Acesso total • Pode editar PEIs</p>
                                    </div>
                                    <span class="text-green-600 text-sm">Dra. Paula Santos</span>
                                </div>
                                <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                                    <div>
                                        <p class="font-medium text-sm">Profissionais</p>
                                        <p class="text-xs text-gray-500">Leitura e comentários</p>
                                    </div>
                                    <span class="text-blue-600 text-sm">4 membros</span>
                                </div>
                                <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                                    <div>
                                        <p class="font-medium text-sm">Família</p>
                                        <p class="text-xs text-gray-500">Visualização limitada</p>
                                    </div>
                                    <span class="text-purple-600 text-sm">2 responsáveis</span>
                                </div>
                            </div>
                            <button onclick="managePermissions()" class="w-full mt-4 bg-gray-100 text-gray-700 py-2 rounded-lg hover:bg-gray-200 transition-all text-sm">
                                Gerenciar Permissões
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <div id="page-roadmap" class="page-content">
                <div class="p-8">
                    <h2 class="text-2xl font-bold mb-6">Roadmap MVP</h2>
                    <p class="text-gray-600">Roadmap do produto em desenvolvimento...</p>
                </div>
            </div>
        </main>
    </div>

    <!-- Modal para Atividade Gerada -->
    <div id="activityModal" class="fixed inset-0 bg-black bg-opacity-50 hidden z-50">
        <div class="flex items-center justify-center min-h-screen p-4">
            <div class="bg-white rounded-xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
                <div class="p-6 border-b border-gray-200">
                    <div class="flex items-center justify-between">
                        <h3 class="text-xl font-semibold flex items-center">
                            <span class="mr-2">🤖</span>Atividade Gerada pela IA
                        </h3>
                        <button onclick="closeActivityModal()" class="text-gray-400 hover:text-gray-600">
                            <span class="text-2xl">×</span>
                        </button>
                    </div>
                </div>
                <div id="activityContent" class="p-6">
                    <!-- Conteúdo da atividade será inserido aqui -->
                </div>
                <div class="p-6 border-t border-gray-200 flex justify-between">
                    <div class="flex space-x-3">
                        <button onclick="saveActivity()" class="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-all">
                            <span class="mr-2">💾</span>Salvar
                        </button>
                        <button onclick="editActivity()" class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-all">
                            <span class="mr-2">✏️</span>Editar
                        </button>
                        <button onclick="printActivity()" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition-all">
                            <span class="mr-2">🖨️</span>Imprimir
                        </button>
                    </div>
                    <button onclick="generateNewActivity()" class="bg-orange-600 text-white px-4 py-2 rounded-lg hover:bg-orange-700 transition-all">
                        <span class="mr-2">🔄</span>Gerar Nova
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Navigation Functions
        function showPage(pageId) {
            // Hide all pages
            document.querySelectorAll('.page-content').forEach(page => {
                page.classList.remove('active');
            });
            
            // Remove active class from all nav items
            document.querySelectorAll('nav a').forEach(nav => {
                nav.classList.remove('nav-active');
                nav.classList.add('text-gray-700');
            });
            
            // Show selected page
            document.getElementById('page-' + pageId).classList.add('active');
            
            // Add active class to selected nav item
            const navItem = document.getElementById('nav-' + pageId);
            if (navItem) {
                navItem.classList.add('nav-active');
                navItem.classList.remove('text-gray-700');
            }
        }

        // BNCC Skills Database (simplified)
        const bnccSkills = {
            '3': {
                'matematica': [
                    { code: 'EF03MA01', description: 'Ler, escrever e comparar números naturais até a ordem de unidade de milhar' },
                    { code: 'EF03MA02', description: 'Identificar características do sistema de numeração decimal' },
                    { code: 'EF03MA03', description: 'Construir e utilizar fatos básicos da adição e da subtração' },
                    { code: 'EF03MA04', description: 'Estabelecer a relação entre números naturais e pontos da reta numérica' }
                ],
                'portugues': [
                    { code: 'EF03LP01', description: 'Ler e escrever palavras com correspondências regulares contextuais' },
                    { code: 'EF03LP02', description: 'Ler e escrever corretamente palavras com sílabas CV, V, CVC, CCV' },
                    { code: 'EF03LP03', description: 'Ler e escrever corretamente palavras com os dígrafos lh, nh, ch' }
                ]
            },
            '4': {
                'matematica': [
                    { code: 'EF04MA01', description: 'Ler, escrever e ordenar números naturais até a ordem de dezenas de milhar' },
                    { code: 'EF04MA02', description: 'Mostrar, por decomposição e composição, que todo número natural pode ser escrito por meio de adições e multiplicações por potências de dez' }
                ],
                'portugues': [
                    { code: 'EF04LP01', description: 'Grafar palavras utilizando regras de correspondência fonema-grafema regulares' },
                    { code: 'EF04LP02', description: 'Ler e escrever, corretamente, palavras com sílabas VV e CVV em casos nos quais a combinação VV (ditongo) é reduzida na língua oral' }
                ]
            },
            '2': {
                'matematica': [
                    { code: 'EF02MA01', description: 'Comparar e ordenar números naturais (até a ordem de centenas) pela compreensão de características do sistema de numeração decimal' },
                    { code: 'EF02MA02', description: 'Fazer estimativas por meio de estratégias diversas a respeito da quantidade de objetos de coleções' }
                ],
                'portugues': [
                    { code: 'EF02LP01', description: 'Utilizar, ao produzir o texto, grafia correta de palavras conhecidas ou com estruturas silábicas já dominadas' },
                    { code: 'EF02LP02', description: 'Segmentar palavras em sílabas e remover e substituir sílabas iniciais, mediais ou finais para criar novas palavras' }
                ]
            }
        };

        // Load BNCC Skills
        function loadBNCCSkills() {
            const ano = document.getElementById('anoSelect').value;
            const disciplina = document.getElementById('disciplinaSelect').value;
            const container = document.getElementById('bnccSkillsContainer');
            
            if (!ano || !disciplina) {
                container.innerHTML = '<p class="text-gray-500 text-center py-8">Selecione o ano e disciplina para ver as habilidades disponíveis</p>';
                return;
            }
            
            const skills = bnccSkills[ano]?.[disciplina] || [];
            
            if (skills.length === 0) {
                container.innerHTML = '<p class="text-gray-500 text-center py-8">Nenhuma habilidade encontrada para esta combinação</p>';
                return;
            }
            
            let html = '<div class="space-y-2">';
            skills.forEach(skill => {
                html += `
                    <div class="bncc-skill border border-gray-200 rounded-lg p-3 hover:bg-blue-50" onclick="selectBNCCSkill('${skill.code}', '${skill.description}')">
                        <div class="font-medium text-blue-800">${skill.code}</div>
                        <div class="text-sm text-gray-600">${skill.description}</div>
                    </div>
                `;
            });
            html += '</div>';
            
            container.innerHTML = html;
        }

        // Select BNCC Skill
        function selectBNCCSkill(code, description) {
            // Remove previous selection
            document.querySelectorAll('.bncc-skill').forEach(skill => {
                skill.classList.remove('selected');
            });
            
            // Add selection to clicked item
            event.currentTarget.classList.add('selected');
            
            // Store selected skill
            document.getElementById('selectedBNCC').value = `${code}: ${description}`;
        }

        // Load Template
        function loadTemplate(type) {
            const templates = {
                'tea': {
                    transtorno: 'tea',
                    escolaridade: 'adequado',
                    pontosFortes: 'Excelente memória visual, interesse por dinossauros, boa coordenação motora grossa',
                    observacoes: 'Hoje está mais calmo, demonstrou interesse em atividades com imagens',
                    reforcadores: 'Dinossauros, música clássica, elogios verbais, tempo no tablet',
                    areasTrabalhar: 'Comunicação verbal, interação social, tolerância a mudanças, atenção compartilhada'
                },
                'tdah': {
                    transtorno: 'tdah',
                    escolaridade: 'adequado',
                    pontosFortes: 'Criatividade, energia, pensamento rápido, habilidade com tecnologia',
                    observacoes: 'Hoje está mais agitado, teve dificuldade para se concentrar nas primeiras atividades',
                    reforcadores: 'Jogos, movimento, música, recompensas imediatas, atividades práticas',
                    areasTrabalhar: 'Atenção sustentada, organização, controle de impulsos, seguir instruções'
                },
                'dislexia': {
                    transtorno: 'dislexia',
                    escolaridade: 'silabico-alfabetico',
                    pontosFortes: 'Boa compreensão oral, criatividade, habilidades visuais, raciocínio lógico',
                    observacoes: 'Mostrou frustração com atividades de leitura, mas participou bem de atividades orais',
                    reforcadores: 'Histórias em áudio, jogos visuais, atividades artísticas, reconhecimento do esforço',
                    areasTrabalhar: 'Consciência fonológica, decodificação, fluência de leitura, autoestima acadêmica'
                }
            };
            
            const template = templates[type];
            if (template) {
                document.getElementById('transtornoSelect').value = template.transtorno;
                document.getElementById('escolaridadeSelect').value = template.escolaridade;
                document.getElementById('pontosFortesText').value = template.pontosFortes;
                document.getElementById('observacoesDiaText').value = template.observacoes;
                document.getElementById('reforcadoresText').value = template.reforcadores;
                document.getElementById('areasTrabalharText').value = template.areasTrabalhar;
            }
        }

        // Generate Activity with AI
        function generateActivity() {
            const formData = {
                aluno: document.getElementById('alunoSelect').value,
                bncc: document.getElementById('selectedBNCC').value,
                transtorno: document.getElementById('transtornoSelect').value,
                escolaridade: document.getElementById('escolaridadeSelect').value,
                pontosFortes: document.getElementById('pontosFortesText').value,
                observacoes: document.getElementById('observacoesDiaText').value,
                reforcadores: document.getElementById('reforcadoresText').value,
                areasTrabalhar: document.getElementById('areasTrabalharText').value,
                tipoAtividade: document.querySelector('input[name="tipoAtividade"]:checked')?.value
            };
            
            // Validation
            if (!formData.aluno || !formData.bncc || !formData.transtorno || !formData.tipoAtividade) {
                alert('Por favor, preencha todos os campos obrigatórios: Aluno, Habilidade BNCC, Transtorno e Tipo de Atividade.');
                return;
            }
            
            // Show loading
            const button = event.target;
            const originalText = button.innerHTML;
            button.innerHTML = '<span class="mr-3 ai-generating">🤖</span>Gerando com IA...';
            button.disabled = true;
            
            // Simulate AI processing
            setTimeout(() => {
                showGeneratedActivity(formData);
                button.innerHTML = originalText;
                button.disabled = false;
            }, 3000);
        }

        // Show Generated Activity
        function showGeneratedActivity(formData) {
            const activityTypes = {
                'ficha': generateFichaActivity(formData),
                'jogo': generateJogoActivity(formData),
                'roteiro': generateRoteiroActivity(formData)
            };
            
            const content = activityTypes[formData.tipoAtividade];
            document.getElementById('activityContent').innerHTML = content;
            document.getElementById('activityModal').classList.remove('hidden');
        }

        // Generate Ficha Activity
        function generateFichaActivity(data) {
            return `
                <div class="space-y-6">
                    <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
                        <h4 class="font-semibold text-blue-800 mb-2">📄 Ficha de Atividade Personalizada</h4>
                        <p class="text-blue-700 text-sm">Gerada pela IA com base no perfil do aluno e habilidade BNCC selecionada</p>
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4 text-sm">
                        <div><strong>Aluno:</strong> ${data.aluno.split(' - ')[0]}</div>
                        <div><strong>Data:</strong> ${new Date().toLocaleDateString('pt-BR')}</div>
                        <div><strong>Habilidade BNCC:</strong> ${data.bncc.split(':')[0]}</div>
                        <div><strong>Transtorno:</strong> ${data.transtorno.toUpperCase()}</div>
                    </div>
                    
                    <div class="bg-green-50 border border-green-200 rounded-lg p-4">
                        <h5 class="font-semibold text-green-800 mb-3">🎯 Objetivo da Atividade</h5>
                        <p class="text-green-700">Desenvolver habilidades de ${data.bncc.split(':')[1]} considerando as características do ${data.transtorno.toUpperCase()} e utilizando os pontos fortes identificados: ${data.pontosFortes.substring(0, 100)}...</p>
                    </div>
                    
                    <div class="space-y-4">
                        <h5 class="font-semibold text-gray-800">📝 Atividades Propostas</h5>
                        
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h6 class="font-medium mb-2">1. Atividade de Aquecimento (5 min)</h6>
                            <p class="text-gray-700 mb-2">Começar com uma atividade relacionada aos interesses do aluno (${data.reforcadores.split(',')[0]}) para engajamento inicial.</p>
                            <div class="bg-yellow-100 border-l-4 border-yellow-500 p-2 text-sm">
                                <strong>Adaptação TEA:</strong> Usar suporte visual e rotina estruturada
                            </div>
                        </div>
                        
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h6 class="font-medium mb-2">2. Atividade Principal (15 min)</h6>
                            <p class="text-gray-700 mb-2">Exercícios práticos focados na habilidade BNCC ${data.bncc.split(':')[0]}, adaptados para o nível ${data.escolaridade}.</p>
                            <ul class="list-disc list-inside text-gray-600 text-sm space-y-1">
                                <li>Usar materiais visuais e concretos</li>
                                <li>Dividir em etapas pequenas e claras</li>
                                <li>Oferecer pausas quando necessário</li>
                                <li>Incorporar elementos de ${data.reforcadores.split(',')[0]}</li>
                            </ul>
                        </div>
                        
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h6 class="font-medium mb-2">3. Atividade de Consolidação (10 min)</h6>
                            <p class="text-gray-700 mb-2">Revisão lúdica do conteúdo trabalhado com foco nas áreas a desenvolver: ${data.areasTrabalhar.substring(0, 50)}...</p>
                        </div>
                    </div>
                    
                    <div class="bg-purple-50 border border-purple-200 rounded-lg p-4">
                        <h5 class="font-semibold text-purple-800 mb-3">🎁 Estratégias de Reforço</h5>
                        <div class="grid grid-cols-2 gap-3 text-sm">
                            <div>
                                <strong>Reforçadores Identificados:</strong>
                                <ul class="list-disc list-inside text-purple-700 mt-1">
                                    ${data.reforcadores.split(',').slice(0, 3).map(r => `<li>${r.trim()}</li>`).join('')}
                                </ul>
                            </div>
                            <div>
                                <strong>Estratégias de Apoio:</strong>
                                <ul class="list-disc list-inside text-purple-700 mt-1">
                                    <li>Elogios específicos</li>
                                    <li>Pausas programadas</li>
                                    <li>Suporte visual</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-orange-50 border border-orange-200 rounded-lg p-4">
                        <h5 class="font-semibold text-orange-800 mb-3">📊 Critérios de Avaliação</h5>
                        <div class="space-y-2 text-sm">
                            <div class="flex items-center space-x-2">
                                <input type="checkbox" class="rounded">
                                <span>Participou da atividade de forma engajada</span>
                            </div>
                            <div class="flex items-center space-x-2">
                                <input type="checkbox" class="rounded">
                                <span>Demonstrou compreensão do conceito trabalhado</span>
                            </div>
                            <div class="flex items-center space-x-2">
                                <input type="checkbox" class="rounded">
                                <span>Utilizou estratégias de autorregulação quando necessário</span>
                            </div>
                            <div class="flex items-center space-x-2">
                                <input type="checkbox" class="rounded">
                                <span>Mostrou progresso nas áreas trabalhadas</span>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }

        // Generate Jogo Activity
        function generateJogoActivity(data) {
            return `
                <div class="space-y-6">
                    <div class="bg-green-50 border border-green-200 rounded-lg p-4">
                        <h4 class="font-semibold text-green-800 mb-2">🎮 Jogo/Dinâmica Personalizada</h4>
                        <p class="text-green-700 text-sm">Atividade lúdica adaptada para ${data.transtorno.toUpperCase()} com foco na habilidade BNCC</p>
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4 text-sm">
                        <div><strong>Aluno:</strong> ${data.aluno.split(' - ')[0]}</div>
                        <div><strong>Duração:</strong> 20-30 minutos</div>
                        <div><strong>Participantes:</strong> Individual ou pequeno grupo</div>
                        <div><strong>Materiais:</strong> Visuais e manipuláveis</div>
                    </div>
                    
                    <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
                        <h5 class="font-semibold text-blue-800 mb-3">🎯 "Aventura dos ${data.reforcadores.split(',')[0].trim()}"</h5>
                        <p class="text-blue-700">Jogo temático baseado nos interesses do aluno para trabalhar ${data.bncc.split(':')[1]}</p>
                    </div>
                    
                    <div class="space-y-4">
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h6 class="font-medium mb-2 flex items-center">
                                <span class="mr-2">📋</span>Preparação do Jogo
                            </h6>
                            <ul class="list-disc list-inside text-gray-700 space-y-1">
                                <li>Preparar cartas/fichas com imagens de ${data.reforcadores.split(',')[0].trim()}</li>
                                <li>Criar tabuleiro visual com etapas claras</li>
                                <li>Organizar materiais manipuláveis</li>
                                <li>Estabelecer regras simples e visuais</li>
                            </ul>
                        </div>
                        
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h6 class="font-medium mb-2 flex items-center">
                                <span class="mr-2">🎲</span>Como Jogar
                            </h6>
                            <div class="space-y-3">
                                <div class="border-l-4 border-green-500 pl-3">
                                    <strong>Etapa 1:</strong> Apresentação do jogo com suporte visual
                                    <p class="text-sm text-gray-600">Explicar regras usando imagens e demonstração prática</p>
                                </div>
                                <div class="border-l-4 border-blue-500 pl-3">
                                    <strong>Etapa 2:</strong> Jogada colaborativa inicial
                                    <p class="text-sm text-gray-600">Jogar junto para modelar comportamentos esperados</p>
                                </div>
                                <div class="border-l-4 border-purple-500 pl-3">
                                    <strong>Etapa 3:</strong> Jogo independente com apoio
                                    <p class="text-sm text-gray-600">Permitir autonomia com suporte quando necessário</p>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-gray-50 rounded-lg p-4">
                            <h6 class="font-medium mb-2 flex items-center">
                                <span class="mr-2">⭐</span>Adaptações Específicas
                            </h6>
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                                <div class="bg-yellow-100 p-3 rounded">
                                    <strong class="text-yellow-800">Para TEA:</strong>
                                    <ul class="text-sm text-yellow-700 mt-1">
                                        <li>• Rotina visual clara</li>
                                        <li>• Pausas programadas</li>
                                        <li>• Redução de estímulos</li>
                                    </ul>
                                </div>
                                <div class="bg-orange-100 p-3 rounded">
                                    <strong class="text-orange-800">Considerando:</strong>
                                    <ul class="text-sm text-orange-700 mt-1">
                                        <li>• ${data.observacoes.substring(0, 30)}...</li>
                                        <li>• Pontos fortes identificados</li>
                                        <li>• Áreas de desenvolvimento</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-purple-50 border border-purple-200 rounded-lg p-4">
                        <h5 class="font-semibold text-purple-800 mb-3">🏆 Sistema de Recompensas</h5>
                        <div class="grid grid-cols-3 gap-3 text-sm">
                            <div class="text-center">
                                <div class="text-2xl mb-1">🥉</div>
                                <div class="font-medium">Participação</div>
                                <div class="text-xs text-gray-600">Elogio verbal</div>
                            </div>
                            <div class="text-center">
                                <div class="text-2xl mb-1">🥈</div>
                                <div class="font-medium">Progresso</div>
                                <div class="text-xs text-gray-600">Adesivo especial</div>
                            </div>
                            <div class="text-center">
                                <div class="text-2xl mb-1">🥇</div>
                                <div class="font-medium">Excelência</div>
                                <div class="text-xs text-gray-600">Tempo extra com ${data.reforcadores.split(',')[0].trim()}</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-red-50 border border-red-200 rounded-lg p-4">
                        <h5 class="font-semibold text-red-800 mb-3">⚠️ Pontos de Atenção</h5>
                        <ul class="list-disc list-inside text-red-700 text-sm space-y-1">
                            <li>Observar sinais de sobrecarga sensorial</li>
                            <li>Estar preparado para pausas não programadas</li>
                            <li>Manter flexibilidade nas regras se necessário</li>
                            <li>Focar no processo, não apenas no resultado</li>
                        </ul>
                    </div>
                </div>
            `;
        }

        // Generate Roteiro Activity
        function generateRoteiroActivity(data) {
            return `
                <div class="space-y-6">
                    <div class="bg-orange-50 border border-orange-200 rounded-lg p-4">
                        <h4 class="font-semibold text-orange-800 mb-2">🏠 Roteiro para Família</h4>
                        <p class="text-orange-700 text-sm">Orientações detalhadas para continuidade do trabalho em casa</p>
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4 text-sm bg-gray-50 p-4 rounded-lg">
                        <div><strong>Aluno:</strong> ${data.aluno.split(' - ')[0]}</div>
                        <div><strong>Período:</strong> Próximas 2 semanas</div>
                        <div><strong>Habilidade Trabalhada:</strong> ${data.bncc.split(':')[0]}</div>
                        <div><strong>Frequência Sugerida:</strong> 3-4x por semana</div>
                    </div>
                    
                    <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
                        <h5 class="font-semibold text-blue-800 mb-3">👨‍👩‍👧‍👦 Orientações Gerais para a Família</h5>
                        <div class="space-y-2 text-blue-700">
                            <p>• <strong>Ambiente:</strong> Escolha um local calmo, bem iluminado e livre de distrações</p>
                            <p>• <strong>Horário:</strong> Estabeleça uma rotina, preferencialmente no mesmo horário</p>
                            <p>• <strong>Duração:</strong> Sessões de 15-20 minutos para manter o engajamento</p>
                            <p>• <strong>Atitude:</strong> Mantenha paciência e celebre pequenos progressos</p>
                        </div>
                    </div>
                    
                    <div class="space-y-4">
                        <h5 class="font-semibold text-gray-800">📅 Cronograma Semanal</h5>
                        
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div class="bg-green-50 border border-green-200 rounded-lg p-4">
                                <h6 class="font-medium text-green-800 mb-2">Segunda e Quarta</h6>
                                <div class="text-sm text-green-700 space-y-1">
                                    <p><strong>Atividade Principal:</strong> Trabalhar conceitos da BNCC ${data.bncc.split(':')[0]}</p>
                                    <p><strong>Material:</strong> Papel, lápis, objetos concretos</p>
                                    <p><strong>Tempo:</strong> 15-20 minutos</p>
                                </div>
                            </div>
                            
                            <div class="bg-purple-50 border border-purple-200 rounded-lg p-4">
                                <h6 class="font-medium text-purple-800 mb-2">Terça e Quinta</h6>
                                <div class="text-sm text-purple-700 space-y-1">
                                    <p><strong>Atividade Lúdica:</strong> Jogos relacionados ao tema</p>
                                    <p><strong>Material:</strong> Jogos, cartas, ${data.reforcadores.split(',')[0].trim()}</p>
                                    <p><strong>Tempo:</strong> 20-25 minutos</p>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                            <h6 class="font-medium text-yellow-800 mb-2">Sexta (Revisão)</h6>
                            <div class="text-sm text-yellow-700">
                                <p><strong>Atividade de Consolidação:</strong> Revisar o que foi aprendido durante a semana de forma divertida</p>
                                <p><strong>Sugestão:</strong> Criar um "show and tell" onde a criança ensina o que aprendeu</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-gray-50 rounded-lg p-4">
                        <h5 class="font-semibold text-gray-800 mb-3">🎯 Atividades Específicas Sugeridas</h5>
                        <div class="space-y-3">
                            <div class="border-l-4 border-blue-500 pl-3">
                                <strong>Atividade 1: Exploração com ${data.reforcadores.split(',')[0].trim()}</strong>
                                <p class="text-sm text-gray-600 mt-1">Use o interesse da criança por ${data.reforcadores.split(',')[0].trim()} para trabalhar os conceitos da habilidade BNCC. Exemplo: contar, classificar, ordenar usando elementos temáticos.</p>
                            </div>
                            
                            <div class="border-l-4 border-green-500 pl-3">
                                <strong>Atividade 2: Rotina Visual</strong>
                                <p class="text-sm text-gray-600 mt-1">Crie uma sequência visual das atividades do dia, ajudando na organização e reduzindo ansiedade. Use imagens claras e simples.</p>
                            </div>
                            
                            <div class="border-l-4 border-purple-500 pl-3">
                                <strong>Atividade 3: Comunicação Funcional</strong>
                                <p class="text-sm text-gray-600 mt-1">Trabalhe ${data.areasTrabalhar.split(',')[0].trim()} através de situações práticas do dia a dia, sempre respeitando o ritmo da criança.</p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-red-50 border border-red-200 rounded-lg p-4">
                        <h5 class="font-semibold text-red-800 mb-3">🚨 Sinais de Alerta - Quando Pausar</h5>
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-red-700">
                            <div>
                                <strong>Sinais de Sobrecarga:</strong>
                                <ul class="list-disc list-inside mt-1">
                                    <li>Agitação excessiva</li>
                                    <li>Recusa em participar</li>
                                    <li>Comportamentos repetitivos</li>
                                </ul>
                            </div>
                            <div>
                                <strong>O que fazer:</strong>
                                <ul class="list-disc list-inside mt-1">
                                    <li>Fazer uma pausa</li>
                                    <li>Oferecer atividade calmante</li>
                                    <li>Retomar quando estiver pronto</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-green-50 border border-green-200 rounded-lg p-4">
                        <h5 class="font-semibold text-green-800 mb-3">📝 Registro de Progresso</h5>
                        <p class="text-green-700 text-sm mb-3">Mantenha um registro simples do progresso diário:</p>
                        <div class="bg-white p-3 rounded border">
                            <div class="grid grid-cols-4 gap-2 text-xs font-medium text-gray-600 mb-2">
                                <div>Data</div>
                                <div>Atividade</div>
                                <div>Participação</div>
                                <div>Observações</div>
                            </div>
                            <div class="space-y-1 text-xs">
                                <div class="grid grid-cols-4 gap-2 py-1 border-b">
                                    <div>__/__</div>
                                    <div>_________</div>
                                    <div>😊 😐 😞</div>
                                    <div>_________</div>
                                </div>
                                <div class="grid grid-cols-4 gap-2 py-1 border-b">
                                    <div>__/__</div>
                                    <div>_________</div>
                                    <div>😊 😐 😞</div>
                                    <div>_________</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
                        <h5 class="font-semibold text-blue-800 mb-3">📞 Contato com a Escola</h5>
                        <div class="text-blue-700 text-sm space-y-1">
                            <p><strong>Professora:</strong> Dra. Maria Silva</p>
                            <p><strong>Email:</strong> maria.silva@escola.edu.br</p>
                            <p><strong>Telefone:</strong> (11) 99999-9999</p>
                            <p><strong>Horário de contato:</strong> Segunda a sexta, 7h às 17h</p>
                            <p class="mt-2 font-medium">Não hesite em entrar em contato para dúvidas ou compartilhar observações!</p>
                        </div>
                    </div>
                </div>
            `;
        }

        // Modal Functions
        function closeActivityModal() {
            document.getElementById('activityModal').classList.add('hidden');
        }

        function saveActivity() {
            alert('Atividade salva com sucesso! 💾');
            closeActivityModal();
        }

        function editActivity() {
            alert('Abrindo editor de atividades... ✏️');
        }

        function printActivity() {
            window.print();
        }

        function generateNewActivity() {
            closeActivityModal();
            generateActivity();
        }

        // Initialize Charts
        function initializeCharts() {
            // Evolution Chart
            const ctx = document.getElementById('evolutionChart');
            if (ctx) {
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
                        datasets: [{
                            label: 'Progresso Geral',
                            data: [65, 70, 75, 78, 82, 87],
                            borderColor: '#667eea',
                            backgroundColor: 'rgba(102, 126, 234, 0.1)',
                            tension: 0.4
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                display: false
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                max: 100
                            }
                        }
                    }
                });
            }
        }

        // Initialize when page loads
        document.addEventListener('DOMContentLoaded', function() {
            initializeCharts();
        });

        // Placeholder functions for other features
        function showStudentProfile() {
            showPage('alunos');
        }

        function showTemplateQuick() {
            alert('Abrindo templates rápidos... ⚡');
        }

        function showActivityHistory() {
            alert('Abrindo histórico de atividades... 📚');
        }

        // Collaboration Functions
        function scheduleNewMeeting() {
            alert('Abrindo agendador de reuniões... 📅\n\nFuncionalidades:\n• Selecionar participantes\n• Definir data/hora\n• Adicionar agenda\n• Enviar convites automáticos');
        }

        function showNotifications() {
            alert('Central de Notificações 🔔\n\n• 3 novas mensões\n• 2 reuniões agendadas\n• 1 anotação compartilhada\n• 5 comentários em registros');
        }

        function sendMessage() {
            const input = document.getElementById('chatInput');
            const message = input.value.trim();
            
            if (message) {
                // Simulate sending message
                const chatContainer = document.getElementById('chatMessages');
                const newMessage = document.createElement('div');
                newMessage.className = 'flex items-start space-x-3';
                newMessage.innerHTML = `
                    <div class="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center flex-shrink-0">
                        <span class="text-xs font-medium">MS</span>
                    </div>
                    <div class="flex-1">
                        <div class="flex items-center space-x-2 mb-1">
                            <span class="font-medium text-sm">Dra. Maria Silva</span>
                            <span class="text-xs text-gray-500">Pedagoga</span>
                            <span class="text-xs text-gray-400">Agora</span>
                        </div>
                        <div class="bg-blue-100 rounded-lg p-3">
                            <p class="text-sm">${message}</p>
                        </div>
                        <div class="flex items-center space-x-4 mt-2">
                            <button class="text-xs text-gray-500 hover:text-blue-600">👍</button>
                            <button class="text-xs text-gray-500 hover:text-blue-600">Responder</button>
                            <button class="text-xs text-gray-500 hover:text-blue-600">Adicionar ao registro</button>
                        </div>
                    </div>
                `;
                
                chatContainer.appendChild(newMessage);
                chatContainer.scrollTop = chatContainer.scrollHeight;
                input.value = '';
            }
        }

        function attachFile() {
            alert('Anexar arquivo 📎\n\nTipos suportados:\n• Documentos (PDF, DOC)\n• Imagens (JPG, PNG)\n• Áudios (MP3, WAV)\n• Vídeos (MP4, AVI)');
        }

        function recordAudio() {
            alert('Gravação de áudio 🎤\n\nFuncionalidade em desenvolvimento...\n• Gravar mensagem de voz\n• Transcrição automática\n• Anexar ao chat');
        }

        function mentionUser() {
            const input = document.getElementById('chatInput');
            input.value += '@';
            input.focus();
            
            // Show mention dropdown (simulated)
            setTimeout(() => {
                alert('Selecione um profissional:\n\n• @Paula Santos (Psicóloga)\n• @Carlos Ferreira (Fonoaudiólogo)\n• @Ana Silva (Terapeuta Ocupacional)\n• @Roberto Farias (Neurologista)');
            }, 100);
        }

        function addToRecord() {
            alert('Adicionar ao registro 📝\n\nEsta mensagem será:\n• Anexada ao prontuário do aluno\n• Marcada com timestamp\n• Vinculada ao profissional\n• Disponível para relatórios');
        }

        function scheduleFromChat() {
            alert('Agendar reunião 📅\n\nCriando reunião baseada na conversa atual:\n• Participantes: Equipe ativa\n• Tópico: Discussão em andamento\n• Sugestão de horário automática');
        }

        function showTeamMembers() {
            alert('Membros da Equipe 👥\n\n✅ Online: 4 profissionais\n⚠️ Ausente: 1 profissional\n📊 Última atividade: Há 2 min\n🔔 Notificações ativas');
        }

        function showChatHistory() {
            alert('Histórico do Chat 📋\n\nFuncionalidades:\n• Buscar mensagens\n• Filtrar por profissional\n• Exportar conversas\n• Ver anexos compartilhados');
        }

        function addSharedNote() {
            alert('Nova Anotação Compartilhada 📝\n\nCampos disponíveis:\n• Título da anotação\n• Conteúdo detalhado\n• Tags e categorias\n• Permissões de acesso\n• Vinculação ao PEI');
        }

        function managePermissions() {
            alert('Gerenciar Permissões 🔐\n\nNíveis de acesso:\n• Coordenador: Acesso total\n• Profissionais: Leitura/comentários\n• Família: Visualização limitada\n• Estagiários: Apenas observação');
        }

        // Chat input enter key support
        document.addEventListener('DOMContentLoaded', function() {
            const chatInput = document.getElementById('chatInput');
            if (chatInput) {
                chatInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        sendMessage();
                    }
                });
            }
        });
    </script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'97af604f00b0e10b',t:'MTc1NzE3NjQ5MS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
