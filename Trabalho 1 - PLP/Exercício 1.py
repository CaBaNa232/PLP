//Substituir NIL por () 

(defun substitui (elemento1 elemento2 lista) 
(cond ((null lista) nil)
((equal elemento1 (car lista))
(cons elemento2 (substitui elemento1 elemento2
(cdr lista))))
(t (cons (car lista) (substitui elemento1 elemento2
(cdr lista)))))
)

//Remove os parenteses

(defun squash (lista)
(cond ((null lista) nil)
((atom lista) (list lista))
(t (append (squash (car lista)) (squash (cdr lista)))))
)


(defun apaga (elemento lista)
(cond ((null lista) nil)
((equal elemento (car lista))
(apaga elemento (cdr lista)))
(t (cons (car lista) (apaga elemento (cdr lista)))))
)


(defun count_list (lista) 
    (cond ((null lista) nil)(
    (write(cons(car lista)(count (car lista) lista)))
    (count_list (apaga (car lista) lista)))
))


(count_list (squash (substitui NIL "()" `(a b z x 4.6 (a x) () (5 z x) ()))))) //dEU CERTO




