;;; Brief introduction to Clojure
;;
;; Clojure is a LISP dialect that runs on the Java Virtual Machine,
;; Common Language Runtime, and JavaScript engines. Clojure treats
;; code as data, and has a stronger emphasis on pure functional
;; programming and immutable values than Common Lisp, allowing it to
;; handle concurrent processing very simply.
;;
;;; Credits:
;;
;; This file is work-through of the clojure guide from Adam Bard's
;; excellent "Lean X in Y Minutes", available from:
;;
;;     https://github.com/adambard/learnxinyminutes-docs.git
;;
;;; Code:
;;
;; Set the namespace with ns:
(ns learnclojure)

;; str creates a string from all the arguments:
(str "Hello" ", " "world!")             ; "Hello, world!"

;; Arithmetic uses Polish prefix notation:
(+ 1 1)                                 ; 2
(- 3 1)                                 ; 2
(* 5 2)                                 ; 10
(/ 10 2)                                ; 5

;; Equality tests:
(= 1 1)                                 ; true
(= 2 1)                                 ; false

;; Inverse logic:
(not true)                              ; false

;; Nesting forms:
(+ 1 (- 10 1))                          ; 10

;;; Types:

;; Clojure uses Java's object types for booleans, strings and
;; numbers. 'class' inspects them.
(class 1)                               ; java.lang.Long
(class 1.)                              ; java.lang.Double
(class "")                              ; java.lang.String
(class false)                           ; java.lang.Boolean
(class nil)                             ; nil

;; Quoted lists are not evaluated:
'(+ 1 2)                                ; (+ 1 2)
(eval '(+ 1 2))                         ; 3

;;; Collections and Sequences:

;; Lists are linked-list data structures:
(class '(1 2 3))                        ; clojure.lang.PersistentList
(class (list 1 2 3))                    ; clojure.lang.PersistentList

;; Vectors are array-backed:
(class [1 2 3])                         ; clojure.lang.PersistentVector

;; Collections are groups of data:
(coll? (list 1 2 3))                    ; true
(coll? [1 2 3])                         ; true

;; Sequences are abstract descriptions of lists of data:
(seq? (list 1 2 3))                     ; true
(seq? [1 2 3])                          ; false

;; Sequences only need to define an entry (like Python's
;; iterators). Sequences can be lazy and can define infinite series:
(range 5)                               ; (0 1 2 3 4)
(range)                                 ; (0 1 2 3 4 5 ...)
(take 5 (range))                        ; (0 1 2 3 4)

;; Cons adds an item to the beginning of a collection:
(cons 5 '(1 2 3))                       ; (0 1 2 3)
(cons 0 [1 2 3])                        ; (0 1 2 3)

;; Conj will add an item to a collection in the most efficient way,
;; depending on the type:
(conj [1 2 3] 4)                        ; [1 2 3 4]
(conf '(1 2 3) 4)                       ; (4 1 2 3)

;; Concatenate lists and vectors:
(concat [1 2] '(3 4))                   ; (1 2 3 4)

;; Use map and filter to interact with collections:
(map inc [1 2 3])                       ; (2 3 4)
(filter even? (range 10))               ; (0 2 4 6 8)

;; Use reduce to reduce them:
(reduce + (map inc (range 10)))         ; (+ 1 2 3..10) = 55

;; Reduce can take an initial-value argument too:
(reduce conj [] '(1 2 3))               ; [1 2 3]

;;; Functions:

;; Use fn to create new functions. A function returns its last
;; statement. Wrap it in parens to eval:
(fn [] "Hello, world!")
((fn [] "Hello, world!"))               ; "Hello, world!"

;; Variables are defined useing def:
(def x 5)

;; Assign a function to a var:
(def hello-world (fn [] "Hello World"))

;; Syntactic sugar for this is provided by defn:
(defn hello-world [] "Hello World")

;; [] is a list of arguments:
(defn hello [name] (str "Hello, " name))

;; Multi-variadic functions:
(defn hello
  ([] "Hello")
  ([name] (str "Hello, " name)))

;; Pack extra arguments up in a seq for you:
(defn argc [& args]
  (str "You passed " (count args) " args: " args))

;; Variable number of args:
(defn hello-count [name & args]
  (str "Hello " name ", you passed " (count args) " extra args: " args))

;;; Maps:

;; Hash maps and array maps share an interface. Hash maps have faster
;; lookups, but don't retrain key order:
(class {:a 1, :b 2, :c 3})           ; clojure.lang.PersistentArrayMap
(class (hash-map :a 1, :b 2, :c 4))  ; clojure.lang.PersistentHashmap

;; Arraymaps will automatically become hashmaps through most
;; operations. Maps can use any hashable type as a key, but usually
;; keywords are best. Keywords are like strings with some efficiency
;; bonuses:
(class :a)                              ; clojure.lang.Keyword

(def stringmap {"a" 1, "b" 2, "c" 3})
(def keymap {:a 1, :b 2, :c 3})

;; Commas are treated as whitespace and do nothing, they only provide
;; visual cues to help delimit things.

;; Retrieve values from a map by calling it as a function:
(stringmap "a")                         ; 1
(keymap :a)                             ; 1

;; Keywords can be used to retrieve their value from a map (note:
;; doesn't work on strings):
(:a keymap)                             ; 1

;; Use assoc to add new keys:
(assoc keymap :d 4)                     ; {:a 1, :c 3, :b 2, :d 4}

;; Use dissoc to remove keys:
(dissoc keymap :a :b)                   ; {:c 3}

;; Clojure types are immutable, so the original keymap isn't affected:
keymap                                  ; {:a 1, :c 3, :b 2}

;;; Sets:

(class #{1 2 3})                        ; clojure.lang.PersistentHashSet
(set [1 2 3 1 2 3 3 2 1 3 2 1])         ; #{1 2 3}

;; Add a member with conf:
(conj #{1 2 3} 4)                       ; #{1 2 3 4}

;; Remove a member with disj:
(disj #{1 2 3} 1)                       ; #{2 3}

;; Test for existence by using the set as a function
(#{1 2 3} 2)                            ; 2
(#{1 2 3} 4)                            ; nil

;;; Useful forms:

;; Logic constructs in clojure are macros:
(if false "a" "b")                      ; "b"
(if false "a")                          ; nil

;; Use let to create temporary bindings:
(let [a 1 b 2] (> a b))                 ; false

;; Group statements with do:
(do (print "Hello") "World")            ; "Word" (prints "Hello")

;; Functions and let have implicit do statements.

;;; Modules:

;; Use "use" to get all functions from a module:
(use 'clojure.set)

;; So now we can use set operations:
(intersection #{1 2 3} #{2 3 4})        ; #{2 3}
(difference #{1 2 3} #{2 3 4})          ; #{1}

;; Subsets of functions can be imported:
(use '[clojure.set :only [intersection]])

;; Require imports a module:
(require 'clojure.string)

;; Use / to call functions from a module:
(clojure.string/blank? "")              ; true

;; Modules can be renamed on import:
(require '[clojure.string :as str])

;; #"" denotes a regular expression literal:
(str/replace "This is a test." #"[a-o]" str/uppercase) ; "THIs Is A tEst."

;; You can use require from a namespace:
(ns test
  (:require
   [clojure.string :as str]
   [clojure.set :as set]))

;;; Java:

;; Use import to load a java module:
(import java.util.Date)

;; You can import from ns of course:
(ns test
  (:import java.util.Data
           java.util.Calendar))

;; Use the class names with a "." at the end to make a new instance
(Date.)

;; Use . to call methods:
(. (Date.) getTime)                     ; 1388586305434

;; Or, use the ".method" shorthand:
(.getTime (Date.))                      ; 1388586305436

;; Use / to call static methods:
(System/currentTimeMillis)              ; 1388586387776

;; Use doto to make dealing with mutable classes more tolerable:
(import java.util.Calendar)
(doto (Calendar/getInstance) (.set 2000 1 1 0 0 0) .getTime)

;;; STM - Software Transactional Memory:
;; The mechanism clojure uses to handle persistent state.

;; An item is the simplest construct. Pass it an initial value:
(def my-atom (atom {}))

; Update an atom with swap!, which takes a function and calls it with
; the current value of the atom as the first argument, and any
; trailing arguments as the second
(swap! my-atom assoc :a 1)              ; {:a 1}
(swap! my-atom assoc :b 2)              ; {:b 2, :a 1}

;; Use @ to dereference an atom and get its value:
@my-atom                                ; {:b 2, :a 1}

(def counter (atom 0))

(def inc-counter (fn [] (swap! counter inc)))
(inc-counter)                           ; 1
(inc-counter)                           ; 2
(inc-counter)                           ; 3
