(define fact
  (lambda (n)
    (if (= n 0)
        1
        (* (fact (- n 1)) n)
    )
  )
)

(fact 0)
(fact 1)
(fact 2)
(fact 3)

(define fib
  (lambda (n)
    (if (<= n 1)
        n
        (+ (fib (- n 1)) (fib (- n 2)))
        )
    )
  )

(fib 0)
(fib 1)
(fib 2)
(fib 3)
