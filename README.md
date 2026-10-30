Ex1)
a) Quantos foram gerados, mortos e vivos?
gerou 36, morreram 6 e ficaram 30 vivos.
b) Vivos agrupados pela causa e linhas não executadas:
Linhas não executadas (3, 5, 7, 11): os testes não passaram por essas linhas port isso não sobreviveram.
c)Para cada vivo que restou, diga qual condição falhou: alcançar, infectar, propagar ou revelar
Nenhum mutante gerado é equivalente, o MS final é 100%.
d)Troque a conferência da mensagem por pytest.raises(ValueError, match=msg). O que muda?
O match obriga o teste a verificar o texto exato do erro. Isso mata os mutantes de string.

Ex2)
a) Meça a cobertura de ramos e o MS. O que os dois números dizem sobrea suíte?
A cobertura de ramos foi de 100%, mas o MS foi baixo (12 vivos na primeira execução). Isso mostra que a cobertura de código não mede a qualidade da verificação, pois o assert > 0 é fraco e aceita resultados incorretos.
b) Troque só o assert pelo valor exato, sem mudar a entrada. Quantos vivos restam?
Restaram 3.
c) Para cada vivo que restou, diga qual condição falhou: alcançar, infectar, propagar ou revelar
Falharam as condições de Infectar ou Propagar.
d) Acrescente as entradas que faltam até o MS chegar a 100%. Que tipo de preço foi preciso?
Foi preciso adicionar listas menores para cobrir os fluxos sem desconto, e um preço fracionário para matar os mutantes que afetavam a função de arredondamento.

Ex3)
a) Implemente a suíte e rode o mutmut. Liste os vivos com o mutmut show
Cobertura de ramos: 100%. MS: 50% (11 vivos). Conclusão: Cobertura de código não garante testes de qualidade.
b) Classifique cada vivo como equivalente ou não, com justificativa
Sim, 1 equivalente na função maior. Ele sobrevive porque reatribuir o valor máximo por ele mesmo não altera o resultado.
c) Mate os não equivalentes e calcule o MS antes e depois
Mortos com match="^lista vazia$" e teste de empate [30, 21, 30]. MS subiu de 50% para 100% (válido).
d) Explique por que > virar >= é equivalente numa função e não na outra
Em maior, >= reatribui o mesmo valor (equivalente). Em dia_do_maior, retorna o índice errado no empate.

Ex4)
a) Antes de rodar qualquer ferramenta, derive a suíte por valor-limite (aula 6) e implemente
Suíte criada com os limites: n=0 e 13 (inválidos), n=1 e 12 (extremos válidos), n=3 e 4 (limite dos juros).
b) Meça a cobertura de ramos e o MS dessa suíte
A cobertura de ramos é de 100% e o MS inicial deve ser próximo de 100%. (Rode pytest --cov e mutmut run para pegar os números exatos do terminal).
c) Analise cada vivo: mate-o ou justifique que é equivalente. Qual o MS final?
O único vivo é equivalente. Ele troca n <= 3 por n < 3. Para n=3, o fluxo cai no else, calculando juros = 0.02 * (3 - 3) = 0, gerando o exato mesmo resultado. MS Final: 100% (26 mortos / 26 não-equivalentes).
d) Combine à mão dois mutantes de primeira ordem que sua suíte mata, num de segunda ordem
Mutante de 2ª ordem manual: alterar n <= 3 para n < 3 E alterar o multiplicador 0.02 para 0.05 na mesma execução.
e) A suíte mata o mutante de segunda ordem? Relacione com o efeito de acoplamento e com Offutt (1992)
Sim, a suíte mata. Isso comprova o Efeito de Acoplamento (Offutt, 1992), que afirma que testes capazes de matar mutantes simples (1ª ordem) quase sempre matam os mutantes complexos criados pela união deles.