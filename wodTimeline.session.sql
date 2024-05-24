INSERT INTO clas_disciplina (
    nome,
    nivel,
    disciplina,
    descricao,
    sistema,
    criado_em,
    atualizado_em,
    livro_id,
    efeito
)
VALUES (
    'Potência',
    '1',
    'Potência',
    'Os vampiros dotados desta Disciplina possuem uma força sobrenatural. A Potência permite que os vampiros pulem distâncias tremendas, ergam pesos volumosos e golpeiem oponentes com uma força apavorante. Até mesmo os níveis mais baixos deste poder dotam o Membro com um poder físico além dos limites mortais. Imortais mais poderosos são conhecidos por pularem tão longe que parecem estar voando, jogarem carros como latas de refrigerante e golpearem através do concreto como se estivessem socando papelão. Enquanto as Disciplinas mentais inspiram temor, a efetividade bruta da Potência é formidável por si só. Os clãs Brujah, Giovanni, Lasombra e Nosferatu são os possuidores primários desta Disciplina. Mesmo assim, membros de outros clãs frequentemente conseguem encontrar alguém que os possa encaminhar através dos caminhos da Potência.',
    'O jogador faz todos os testes relacionados à Força normalmente, e então, adicionam um sucesso automático para cada ponto que ele possuir em Potência. Portanto, o personagem obtém sucesso na maioria das façanhas físicas praticamente sem a necessidade de um teste. Em combates com armas brancas e em brigas, os sucessos automáticos são aplicados no resultado das jogadas de dano.',
    datetime('now'),
    datetime('now'),
    '1',
    'efeito:TEXT'
);
