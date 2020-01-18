# Anagramas
Digite um anagrama para encontrar palavras correspondentes na língua portuguesa.

------

#### Exemplos de busca por anagramas

Busca | Resultados | Anagramas
--------- | ------ | ------
amor      | 5 anagramas | amor, moar, ramo, roma, romã
cão       | 6 anagramas | aço, caó, cão, coã, oca, ocá
coar      | 13 anagramas | acor, açor, ácor, acro, arco, caro, etc
marco     | 7 anagramas | carmo, macro, macrô, marco, etc
aleator   | 0 anagramas | Não foram encontrados anagramas correspondentes... 

------

### Como o algoritmo funciona

O algoritmo é muito simples!<br>
As palavras <i>marca</i> e <i>carma</i> são anagramas, ordenadas de forma alfabética se tornam iguais:

Palavra   | Chave ordenada
---------  | ------ 
marca      | aacmr
carma      | aacmr 

Ou seja, cria-se um dicionário tratando as palavras que são anagramas pertencendo a mesma chave e na busca por um anagrama, o algoritmo se torna extremamente rápido por procurar apenas pelo seu anagrama ordenado.


### Contribuições

Contribuições são sempre muito bem vindas!


![](https://media0.giphy.com/media/l0HlHFRbmaZtBRhXG/giphy.gif)
