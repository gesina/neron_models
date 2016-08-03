# Notizen Néron-Modelle

## offene Fragen
- Warum muss ein Basiswechsel unverzweigt sein, damit er die
  Néron-Abbildungseigenschaft erhält? 
  (neron, S. 13, Prop. 1.2.2; silverman2, Prop. IV.5.2)
- Wann/wie induziert eine rationale Abbildung auf den generischen
  Fasern eine rationale Abbildung zwischen den Schemata?
  (silverman2, Cor. IV.6.3)
  -> im Affinen Fall; Separiertheit ausnutzen
- Welche Eigenschaften von arithmetischen Flächen werden benötigt?
  (Néron-Modelle aus minimalen eig., reg. Modellen,
  Weierstraßmodelle)
  regulär, nichtleere generische Faser –> flach 
  (silverman2, Cor. IV.4.4+4.3; silverman2, Cor. IV.9.1)
- Warum ist der schematische Abschluss einer abelschen Varietät im
  projektiven Raum glatt über dem generischen Punkt?
  (neron, S.19, Prop. 1.4.2)

- Warum lässt sich die Eigenschaft guter Reduktion (nach Bosch) auf
  eine Umgebung erweitern?
  (neron, S. 17f, 1.4+Thm. 1.4.3)
- Ist das projektive Schema zu einer minimalen Weierstraßgleichung mit
  der schematische Abschluss der ell. Kurve?

- Existenz von Néron-Modellen: Wie detailliert? Welche Eigenschaften?
  (silverman2, Thm. IV.6.1; neron, S. 16, Thm. 1.3.1)
- Néron-Modelle abelscher Varietäten mit guter Reduktion: Wie detailliert?
  (neron, S. 19, Prop. 1.4.2+3)




## Schritte in „Neron Models“

### $S$-Modelle 
$S$ zush. Dedekindschema.
$S$-Modell von $X/\K(S)$ = $S$-Schema $Y$ mit generischer Faser $X=Y \times_S \K(S)$

Erweiterungseigenschaft für etale Punkte in geschl. Punkt $s\in S$
= Valuative Criterion of Properness nur für Bewertungsringe, die étale
über $\O_{s,S}$ sind.
<=> $X(R') \to X_\K(\K')$ surj.
    mit $X_K=X \times_S \K$ und $K=\bigoplus \k(\eta_i)$
<=> $X(R^{sh}) \to X(\K^{sh})$ surj.
    mit Henselization $R^{sh}$ = Limes über solche über $\O_{s,S}$ étalen
    Bewertungsringe mit zugehörigen Abbildungen in algebraischen Abschluss
    von $\k(s)$.

Konstruktionsmöglichkeiten:
projektiver Fall: Chasing Denominators (=> schematischer Abschluss von
$X_\K$ im projektiven Raum)

Weitere Einschränkungen:
Beschränktheit: Erhalte für $g\in X_K(K')$ mit $K,K'$ Bewertungskörper
eine Norm $|g(x)|$ in Punkten $x\in X_K(K')$, in denen $g$ definiert
ist ($g(x)=\bar{g_x}\in \O_{X_K,x}/\m_x=\K\subset\K' $).
Beschränkte Mengen des $\A_\K^n(\K')$: Teilmengen, auf denen die
Koordinatenfunktionen beschränkt sind.
Beschränkte Mengen von $X_\K(\K')$: Endliche Überdeckung durch
geschlossene Immersionen $X_\K\to\A_\K^n$, die die Menge auf eine
beschränkte Menge in $\A_\K^n(\K')$ schicken.
- erhalten unter Morphismen
- eigentlich => beschränkt

$R$-Modell $X$ von $X_\K$ ($\K$ diskreter Bewertungskörper mit
Bewertungsring $R$) mit Erweiterungseigenschaft für étale Punkte
<=> $X_\K(\K^{sh})$ beschränkt in $X_\K$ ($\K^{sh}$ strikte
Henselisierung)
(i.A. nicht separiert)
