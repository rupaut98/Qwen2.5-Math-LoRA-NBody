
# Central configurations of the 4 -body problem with masses $m_{1}=m_{2}>m_{3}=m_{4}=m>0$ and $m$ small 

#### Abstract

In this paper we give a complete description of the families of central configurations of the planar 4-body problem with two pairs of equals masses and two equal masses sufficiently small. In particular, we give an analytical proof that this particular 4 -body problem has exactly 34 different classes of central configurations. Moreover for this problem we prove the following two conjectures: There is a unique convex planar central configuration of the 4-body problem for each ordering of the masses in the boundary of its convex hull, which appears in . We also prove the conjecture: There is a unique convex planar central configuration having two pairs of equal masses located at the adjacent vertices of the configuration and it is an isosceles trapezoid. Finally, the families of central configurations of this 4-body problem are numerically continued to the 4 -body problem with four equal masses.

# 1. Introduction and statement of the main results 

We consider the planar $N$-body problem

$$
m_{k} \tilde{\mathbf{q}}_{k}=-\sum_{\substack{j=1 \\ j \neq k}}^{N} G m_{k} m_{j} \frac{\mathbf{q}_{k}-\mathbf{q}_{j}}{\left|\mathbf{q}_{k}-\mathbf{q}_{j}\right|^{3}}
$$

$k=1, \ldots, N$, where $\mathbf{q}_{k} \in \mathbb{R}^{2}$ is the position vector of the punctual mass $m_{k}$ in an inertial coordinate system and $G$ is the gravitational constant which can be taken equal to one by choosing conveniently the unit of time. The configuration space of the planar $N$-body problem is

$$
\mathcal{E}=\left\{\left(\mathbf{q}_{1}, \ldots, \mathbf{q}_{N}\right) \in \mathbb{R}^{2 N}: \mathbf{q}_{k} \neq \mathbf{q}_{j}, \text { for } k \neq j\right\}
$$

Given $m_{1}, \ldots, m_{N}$ a configuration $\left(\mathbf{q}_{1}, \ldots, \mathbf{q}_{N}\right) \in \mathcal{E}$ is central if the acceleration vector for each body is a common scalar multiple of its position vector (with respect to the center of mass). That is, if there exists a positive constant $\lambda$ such that

$$
\tilde{\mathbf{q}}_{k}=-\lambda\left(\mathbf{q}_{k}-\mathbf{c m}\right)
$$

for $k=1, \ldots, N$, where $\mathbf{c m}$ is the position vector of the center of mass of the system, which is given by

$$
\mathbf{c m}=\frac{\sum_{k=1}^{N} m_{k} \mathbf{q}_{k}}{\sum_{k=1}^{N} m_{k}}
$$

The configuration $\left(\mathbf{q}_{1}, \ldots, \mathbf{q}_{N}\right) \in \mathcal{E}$ of the $N$-body problem with positive masses $m_{1}, \ldots, m_{N}$ is central if the exists $\lambda$ such that $\left(\lambda, \mathbf{q}_{1}, \ldots, \mathbf{q}_{N}\right)$ is a solution of the system

$$
\lambda\left(\mathbf{q}_{k}-\mathbf{c m}\right)=\sum_{\substack{j=1 \\ j \neq k}}^{N} m_{j} \frac{\mathbf{q}_{k}-\mathbf{q}_{j}}{\left|\mathbf{q}_{k}-\mathbf{q}_{j}\right|^{3}}
$$

for $k=1, \ldots, N$.
We say that two planar central configurations belong to the same class if there exists a rotation of $S O(2)$ and a homothecy of $\mathbb{R}^{2}$ with respect to the center of mass which transform one into the other.

The set of planar central configurations of the $N$-body problem is completely known only for $N=2,3$. For $N=2$ there is a unique class of central

configurations. For $N=3$ there are exactly five classes of central configurations for each choice of three positive masses, the three classes of collinear central configurations found in 1767 by Euler  and the two classes of equilateral triangle central configurations found in 1772 by Lagrange .

The are some partial results on the problem of finding the exact number of classes of central configurations of the $N$-body problem when $N>3$. In 1910 Moulton  showed that there exists exactly $n!/ 2$ classes of collinear central configurations for a given set of positive masses, one for each possible ordering of the masses. Palmore in  obtained a lower bound of the number of planar non-collinear central configurations. Pedersen  numerically and Gannaway  and Arenstorf  numerically and analytically obtained the number of central configurations of the 4 -body problem when one of the masses is sufficiently small. Later on Barros and Leandro in  and  completed the study of the central configurations of the 4 -body problem when one of the masses is sufficiently small showing that in the triangle of masses there is a simple closed bifurcation curve such that outside it there is 8 classes of central configurations, on the bifurcation curve 9 and in the region limited by this curve 10. Xia in  studied the number of central configurations for all $N$ when some of the masses are sufficiently small.

Simó in  gave a numerical study for the number of central configurations for $N=4$ and arbitrary masses. Hampton and Moeckel , by a computer assisted proof, proved the finiteness of the number of central configurations for $N=4$ and any choice of the masses. Albouy and Kaloshin  proved analytically the finiteness of the number of classes of central configurations for $N=4$ for any choice of the masses and for $N=5$ for almost all choice of the masses. The question about the finiteness of the number of classes of central configurations remains open for $N>4$.

Although the set of all planar central configurations of the 4-body problem is not completely known, we can find in the literature several papers that provide the existence and classification of central configurations of the 4 -body problem in some particular cases.

Definition 1. Assume that $\mathbf{q}=\left(\mathbf{q}_{1}, \mathbf{q}_{2}, \mathbf{q}_{3}, \mathbf{q}_{4}\right)$ is a central configuration of the planar 4-body problem.
(i) $\mathbf{q}$ is convex if none of the bodies is located in the interior of the triangle formed by the others,
(ii) $\mathbf{q}$ is concave if one of the bodies is in the interior of the triangle formed by the others,

(iii) $\mathbf{q}$ is a kite central configuration if it has an axis of symmetry passing through two non-adjacent bodies,
(iv) $\mathbf{q}$ is a rhombus if it is convex and the four exterior edges are equal to each other.

Under the assumption that every central configuration of the 4-body problem has an axis of symmetry when the four masses are equal, Llibre in  characterized the planar central configurations of the 4 -body problem with equal masses by studying the intersection points of two planar curves. Later on Albouy in $$ provided a complete analytic proof of the central configurations of the 4 -body problem with equal masses.

Bernat et al. in  characterized the kite planar non-collinear classes of central configurations having some symmetry for the 4 -body problem with three equal masses, see also Leandro . The characterization of the convex central configurations with an axis of symmetry and the concave central configurations of the 4 -body problem when the masses satisfy that $m_{1}=m_{2} \neq m_{3}=m_{4}$ is done in Álvarez and Llibre .

MacMillan and Bartky in  proved that for any four positive masses and any assigned order, there is a convex planar central configuration of the 4-body problem with that order (see Xia  for a simpler proof). Albouy and Fu in  (see also stated the following conjecture, well known in the central configuration community.

Conjecture 1. There is a unique convex planar central configuration of the 4-body problem for each ordering of the masses in the boundary of its convex hull.

MacMillan and Bartky also proved that there is a unique isosceles trapezoid central configuration of the 4-body when two pairs of equal masses are located at adjacent vertices. This result has been reproved recently by Xie in .

The following subconjecture of Conjecture 1 is well known between people working on central configurations.

Conjecture 2. There is a unique convex planar central configuration having two pairs of equal masses located at the adjacent vertices of the configuration and it is an isosceles trapezoid.

Long and Sun in  proved that any convex non-collinear central configurations with two equal masses $m_{1}=m_{2}<m_{3}=m_{4}$ located at the

opposite vertices of a quadrilateral and such that the diagonal corresponding to the mass $m_{1}$ is not shorter than the one corresponding to the mass $m_{3}$, must posses a symmetry and therefore must be a rhombus. PérezChavela and Santoprete in  extended this result to the case where two of the masses are equal and at most, only one of the remaining mass is larger than the equal masses. In particular, they proved that there exist exactly one convex non-collinear central configuration when the opposite masses are equal and it is a rhombus. Albouy et. al. in  proved that in the planar 4-body problem a convex central configuration is symmetric with respect to one diagonal if and only if the masses of the two particles on the other diagonal are equal. If these two masses are unequal, then the less massive one is closer to the former diagonal.

In this paper we give a complete description of the central configurations of the 4 -body problem when $m_{1}=m_{2}>m_{3}=m_{4}=m>0$ and $m$ is sufficiently small. In particular, we prove Conjectures 1 and 2 under these assumptions on the masses.

The existence of the central configurations of the 4-body problem when $m_{1}=m_{2}>m_{3}=m_{4}=m>0$ and $m$ sufficiently small is established analytically by Xia in . More precisely, Xia shows that the five relative equilibria of the restricted 3-body problem (i.e. the two equilateral triangle solutions and the three collinear solutions), can be continued to $5 \times 4$ classes of central configurations of the 4 -body problem with two small masses which are away from each other and to $2 \times 4+3 \times 2=14$ classes of central configurations with two small masses close to each other. We note that in Xia results the two small masses do not need to be equal. Xia results agree with the ones obtained numerically by Simó in .

The work of Xia does not provide the geometrical shape of the central configurations, which is our main objective.

Theorem 2. Let $m_{1}=m_{2}=1, m_{3}=m_{4}=m, \mathbf{q}_{1}=(-1,0), \mathbf{q}_{2}=(1,0)$, $\mathbf{q}_{3}=\left(x_{3}, y_{3}\right)$ and $\mathbf{q}_{4}=\left(x_{4}, y_{4}\right)$ be the positions of the masses $m_{1}, m_{2}$, $m_{3}$ and $m_{4}$ respectively. Let $\mathbf{s}=\left(x_{3}, y_{3}, x_{4}, y_{4}\right)$. Without loss of generality we assume that $x_{3}, y_{3} \geqslant 0$, and that two planar central configurations are equivalent if one can be obtained from the other by doing either a rotation in dimension three or by interchanging the names of the masses $m_{3}$ and $m_{4}$. Then the following statements hold.
(a) For $m=0$ we have the following classes of non-equivalent planar central configurations.
(a.1) Five different non-equivalent classes of non-collision central con-

figurations given by the positions $\mathbf{s}_{1}=(0, \sqrt{3}, 0,0), \mathbf{s}_{2}=(0, \sqrt{3}, 0$, $-\sqrt{3}), \mathbf{s}_{3}=(\alpha, 0,0,0), \mathbf{s}_{4}=(\alpha, 0,-\alpha, 0)$, and $\mathbf{s}_{5}=(0, \sqrt{3}, \alpha, 0)$ where $\alpha=2.39681 \ldots$ is the unique real root of the equation $x^{5}-2 x^{3}-8 x^{2}+x-8=0$. See Figure 1. We note that the central configurations given by $\mathbf{s}_{3}$ and $\mathbf{s}_{4}$ are collinear.
(a.2) Three different classes of non-equivalent collision central configurations given by the positions $\mathbf{s c}_{1}=(0,0,0,0), \mathbf{s c}_{2}=(0, \sqrt{3}, 0$, $\sqrt{3}$ ), and $\mathbf{s c}_{3}=(\alpha, 0, \alpha, 0)$. See Figure 2.
(b) The central configuration for $m=0$ given by $\mathbf{s}_{1}=(0, \sqrt{3}, 0,0)$ can be continued to a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of concave kite central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =x_{4}(m)=0 \\
y_{3}(m) & =\sqrt{3}+\frac{16(1-3 \sqrt{3})}{27} m+O\left(m^{2}\right) \\
y_{4}(m) & =\frac{8-3 \sqrt{3}}{42} m+O\left(m^{2}\right)
\end{aligned}
$$

(c) The central configuration for $m=0$ given by $\mathbf{s}_{2}=(0, \sqrt{3}, 0,-\sqrt{3})$ can be continued to a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of convex kite central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =x_{4}(m)=0 \\
y_{3}(m) & =\sqrt{3}+\frac{4}{27}(1-3 \sqrt{3}) m+O\left(m^{2}\right) \\
y_{4}(m) & =-y_{3}(m)
\end{aligned}
$$

(d) The central configuration for $m=0$ given by $\mathbf{s}_{3}=(\alpha, 0,0,0)$ can be continued to a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of collinear central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =\alpha-\frac{4\left(\alpha^{2}-1\right)\left(\alpha^{7}-2 \alpha^{5}-4 \alpha^{4}+\alpha^{3}+\alpha^{2}-1\right)}{\alpha^{2}\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)} m+O\left(m^{2}\right) \\
& =2.39681 \cdots-1.36514 \ldots m+O\left(m^{2}\right) \\
x_{4}(m) & =\frac{4\left(3 \alpha^{2}-1\right)}{17 \alpha^{2}\left(\alpha^{2}-1\right)^{2}} m+O\left(m^{2}\right)=0.0295360 \ldots m+O\left(m^{2}\right) \\
y_{3}(m) & =y_{4}(m)=0
\end{aligned}
$$

(e) The central configuration for $m=0$ given by $\mathbf{s}_{4}=(\alpha, 0,-\alpha, 0)$ can be continued to a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of collinear central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =\alpha+\frac{\left(\alpha^{2}-1\right)\left(17 \alpha^{4}-2 \alpha^{2}+1\right)}{\alpha^{2}\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)} m+O\left(m^{2}\right) \\
& =2.39681 \cdots+1.02836 \ldots m+O\left(m^{2}\right) \\
x_{4}(m) & =-x_{3}(m) \\
y_{3}(m) & =y_{4}(m)=0
\end{aligned}
$$

(f) The central configuration for $m=0$ given by $\mathbf{s}_{5}=(0, \sqrt{3}, \alpha, 0)$ can be continued to a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of nonsymmetric central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =\frac{16}{3}\left(\frac{\alpha^{2}+1}{\left(\alpha^{2}-1\right)^{2}}-\frac{\alpha}{\left(\alpha^{2}+3\right)^{3 / 2}}\right) m+O\left(m^{2}\right) \\
& =1.10354 \ldots m+O\left(m^{2}\right) \\
x_{4}(m) & =\alpha+\frac{\frac{\alpha}{\left(\alpha^{2}+3\right)^{3 / 2}}-\frac{\alpha}{8}+\frac{3 \alpha^{2}+1}{\left(\alpha^{2}-1\right)^{2}}}{\frac{4 \alpha\left(\alpha^{2}+3\right)}{\left(\alpha^{2}-1\right)^{3}}+\frac{1}{4}} m+O\left(m^{2}\right) \\
& =2.39681 \cdots+0.582716 \ldots m+O\left(m^{2}\right) \\
y_{3}(m) & =\sqrt{3}+\frac{16}{3 \sqrt{3}}\left(\frac{2 \alpha}{\left(\alpha^{2}-1\right)^{2}}+\frac{1}{\left(\alpha^{2}+3\right)^{3 / 2}}\right) m+O\left(m^{2}\right) \\
& =1.73205 \cdots+0.774741 \ldots m+O\left(m^{2}\right) \\
y_{4}(m) & =-\frac{\sqrt{3}\left(\frac{1}{8}-\frac{1}{\left(\alpha^{2}+3\right)^{3 / 2}}\right)}{\frac{2 \alpha\left(\alpha^{2}+3\right)}{\left(\alpha^{2}-1\right)^{3}}-\frac{1}{4}} m+O\left(m^{2}\right) \\
& =-1.04970 \ldots m+O\left(m^{2}\right)
\end{aligned}
$$

(g) The central configuration for $m=0$ given by $\mathbf{s c}_{1}=(0,0,0,0)$ can be continued to a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of collinear central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =\frac{1}{17^{1 / 3}} m^{1 / 3}-\frac{32}{867} m+O\left(m^{4 / 3}\right) \\
x_{4}(m) & =-x_{3}(m) \\
y_{3}(m) & =y_{4}(m)=0
\end{aligned}
$$

(h) The central configuration for $m=0$ given by $\mathbf{s c}_{2}=(0, \sqrt{3}, 0, \sqrt{3})$ can be continued to
(h.1) a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of concave kite central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =x_{4}(m)=0 \\
y_{3}(m) & =\sqrt{3}+\frac{2^{2 / 3}}{3^{2 / 3}} m^{1 / 3}+\frac{1}{12^{5 / 6}} m^{2 / 3}+\frac{1}{81} m+O\left(m^{4 / 3}\right) \\
y_{4}(m) & =\sqrt{3}-\frac{2^{2 / 3}}{3^{2 / 3}} m^{1 / 3}+\frac{1}{12^{5 / 6}} m^{2 / 3}-\frac{1}{81} m+O\left(m^{4 / 3}\right)
\end{aligned}
$$

(h.2) a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of isosceles trapezoid central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m) & =\frac{2^{2 / 3}}{3^{1 / 3}} m^{1 / 3}+\frac{5}{27} m+O\left(m^{4 / 3}\right) \\
x_{4}(m) & =-x_{3}(m) \\
y_{3}(m) & =\sqrt{3}+\frac{1}{2^{5 / 3} 3^{7 / 6}} m^{2 / 3}+O\left(m^{4 / 3}\right) \\
y_{4}(m) & =y_{3}(m)
\end{aligned}
$$

(i) The central configuration for $m=0$ given by $\mathbf{s c}_{3}=(\alpha, 0, \alpha, 0)$ can be continued to a unique family $\left(x_{3}(m), y_{3}(m), x_{4}(m), y_{4}(m)\right)$ of collinear central configurations for $m>0$ small where

$$
\begin{aligned}
x_{3}(m)= & \alpha+\overline{x_{31}} m^{1 / 3}+\overline{x_{32}} m^{2 / 3}+\overline{x_{33}} m+O\left(m^{4 / 3}\right) \\
= & 2.39681 \cdots+0.622799 \ldots m^{1 / 3}+0.303818 \ldots m^{2 / 3}+ \\
& 1.60489 \ldots m+O\left(m^{4 / 3}\right) \\
x_{4}(m)= & \alpha-\overline{x_{31}} m^{1 / 3}+\overline{x_{32}} m^{2 / 3}+\overline{x_{43}} m+O\left(m^{4 / 3}\right) \\
= & 2.39681 \cdots-0.622799 \ldots m^{1 / 3}+0.303818 \ldots m^{2 / 3}+ \\
& 1.52572 \ldots m+O\left(m^{4 / 3}\right) \\
y_{3}(m)= & y_{4}(m)=0
\end{aligned}
$$

$$
\begin{aligned}
\overline{x_{31}}= & \frac{\alpha^{2}-1}{\sqrt{\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1}} \\
\overline{x_{32}}= & \frac{24\left(\alpha^{6}+5 \alpha^{4}-5 \alpha^{2}-1\right)}{\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)^{5 / 3}} \\
\overline{x_{33}}= & \frac{8}{3}\left(9 \alpha^{16}-60 \alpha^{14}+284 \alpha^{13}+168 \alpha^{12}-216 \alpha^{11}+2132 \alpha^{10}-\right. \\
& 1708 \alpha^{9}+13314 \alpha^{8}+3312 \alpha^{7}+13004 \alpha^{6}-1788 \alpha^{5}- \\
& 20896 \alpha^{4}-152 \alpha^{3}-7524 \alpha^{2}+268 \alpha-147\right) /\left(\alpha^{6}-3 \alpha^{4}+\right. \\
& 16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1)^{3} \\
\overline{x_{43}}= & -\overline{x_{33}}+\frac{16\left(3 \alpha^{4}-2 \alpha^{2}-1\right)}{\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1}
\end{aligned}
$$

(j) The central configurations described in statements (b)-(i) are all the families of non-equivalent central configurations defined for $m>0$ sufficiently small.

Note that Theorem 2 provides all classes of equivalent central configurations of the 4-body problem with two pairs of equal masses and two equal masses sufficiently small. Recall that two planar central configurations are

equivalent if one can be obtained from the other by doing either a rotation in dimension three or by interchanging the names of the masses $m_{3}$ and $m_{4}$. If we do not take into account this equivalence relation, then Theorem 2 provides that the 34 classes of central configurations predicted in  and  are the unique central configuration classes for the 4-body problem here studied. In particular, Theorem 2 describes the geometrical shape of these 34 classes of central configurations. See for more details Figure 3.

From Theorem 2 we get the following result.
Corollary 3. The following statements hold for the 4-body problem with two pairs of equal masses and two equal masses sufficiently small.
(a) It has exactly 34 classes of central configurations.
(b) It has exactly one convex central configuration for each ordering of the masses in the boundary of its convex hull (i.e. Conjecture 1 holds).
(c) It has exactly one convex central configuration having two pairs of equal masses located at the adjacent vertices of the configuration and it is an isosceles trapezoid (i.e. Conjecture 2 holds).

# 2. Equations for the central configurations 

The center of mass of the central configurations studied in Theorem 2 is

$$
\mathbf{c m}=\left(\frac{m\left(x_{3}+x_{4}\right)}{2(m+1)}, \frac{m\left(y_{3}+y_{4}\right)}{2(m+1)}\right)
$$

and equations (1) become

$$
e_{i}=0, \quad \text { for } i=1, \ldots, 8
$$

The classes of planar central configurations that emanate from the five central configurations of the restricted 3-body problem to the four body problem with $m_{1}=m_{2}$ and $m_{3}=m_{4}$ small. The direction of the arrows indicates how the position of the masses $m_{3}$ and $m_{4}$ changes when $m_{3}=m_{4}>0$ and small.

where

$$
\begin{aligned}
e_{1} & =-\frac{1}{4}-\frac{m\left(x_{3}+1\right)}{r_{13}^{3}}-\frac{m\left(x_{4}+1\right)}{r_{14}^{3}}+\left(1+\frac{m\left(x_{3}+x_{4}\right)}{2(m+1)}\right) \lambda \\
e_{2} & =\frac{1}{4}-\frac{m\left(x_{3}-1\right)}{r_{23}^{3}}-\frac{m\left(x_{4}-1\right)}{r_{24}^{3}}-\left(1-\frac{m\left(x_{3}+x_{4}\right)}{2(m+1)}\right) \lambda \\
e_{3} & =\frac{x_{3}+1}{r_{13}^{3}}+\frac{x_{3}-1}{r_{23}^{3}}+\frac{m\left(x_{3}-x_{4}\right)}{r_{34}^{3}}-\left(x_{3}-\frac{m\left(x_{3}+x_{4}\right)}{2(m+1)}\right) \lambda \\
e_{4} & =\frac{x_{4}+1}{r_{14}^{3}}+\frac{x_{4}-1}{r_{24}^{3}}+\frac{m\left(x_{4}-x_{3}\right)}{r_{34}^{3}}-\left(x_{4}-\frac{m\left(x_{3}+x_{4}\right)}{2(m+1)}\right) \lambda \\
e_{5} & =m\left(-\frac{y_{3}}{r_{13}^{3}}-\frac{y_{4}}{r_{14}^{3}}+\frac{\lambda\left(y_{3}+y_{4}\right)}{2(m+1)}\right) \\
e_{6} & =m\left(-\frac{y_{3}}{r_{23}^{3}}-\frac{y_{4}}{r_{24}^{3}}+\frac{\lambda\left(y_{3}+y_{4}\right)}{2(m+1)}\right) \\
e_{7} & =\frac{y_{3}}{r_{13}^{3}}+\frac{y_{3}}{r_{23}^{3}}+\frac{m\left(y_{3}-y_{4}\right)}{r_{34}^{3}}-\left(y_{3}-\frac{m\left(y_{3}+y_{4}\right)}{2(m+1)}\right) \lambda \\
e_{8} & =\frac{y_{4}}{r_{14}^{3}}+\frac{y_{4}}{r_{24}^{3}}+\frac{m\left(y_{4}-y_{3}\right)}{r_{34}^{3}}-\left(y_{4}-\frac{m\left(y_{3}+y_{4}\right)}{2(m+1)}\right) \lambda
\end{aligned}
$$

and

$$
\begin{array}{ll}
r_{13}=\sqrt{\left(x_{3}+1\right)^{2}+y_{3}^{2}}, & r_{14}=\sqrt{\left(x_{4}+1\right)^{2}+y_{4}^{2}} \\
r_{23}=\sqrt{\left(x_{3}-1\right)^{2}+y_{3}^{2}}, & r_{24}=\sqrt{\left(x_{4}-1\right)^{2}+y_{4}^{2}} \\
r_{34}=\sqrt{\left(x_{3}-x_{4}\right)^{2}+\left(y_{3}-y_{4}\right)^{2}} .
\end{array}
$$

Notice that equations (2) are not defined at the binary colülisions between the masses. That is, when either $r_{13}=0, r_{14}=0, r_{23}=0, r_{24}=0$ or $r_{34}=0$.

Clearly the eight equations (2) are not all independent. It is not difficult to prove that

$$
\begin{aligned}
& e_{1}+e_{2}+m e_{3}+m e_{4}=0 \\
& e_{5}+e_{6}+m e_{7}+m e_{8}=0
\end{aligned}
$$

By defining

$$
\begin{array}{lll}
E_{1}=e_{1}-e_{2}, & E_{2}=e_{3}-e_{2}, & E_{3}=e_{4}-e_{2} \\
E_{4}=e_{5}-e_{6}, & E_{5}=e_{7}-e_{6}, & E_{6}=e_{8}-e_{6}
\end{array}
$$

system (2) taking into account (3) is equivalent to system

$$
E_{i}=0, \quad \text { for } i=1, \ldots, 6
$$

By isolating $\lambda$ from equation $E_{1}=0$ and substituting it into the other equations of (4) we get system

$$
F_{i}=0, \quad \text { for } i=1, \ldots, 5
$$

where

$$
\begin{aligned}
F_{1}= & \frac{x_{3}-1}{r_{23}^{3}}-\frac{x_{3}}{4}+\frac{x_{3}+1}{r_{13}^{3}}+m\left(-\frac{x_{3}^{2}-1}{2 r_{13}^{3}}+\frac{x_{3}^{2}-1}{2 r_{23}^{3}}+\frac{x_{3}-x_{4}}{r_{34}^{3}}+\right. \\
& \left.\frac{\left(x_{3}+1\right)\left(x_{4}-1\right)}{2 r_{24}^{3}}-\frac{\left(x_{3}-1\right)\left(x_{4}+1\right)}{2 r_{14}^{3}}\right) \\
F_{2}= & \frac{x_{4}-1}{r_{24}^{3}}-\frac{x_{4}}{4}+\frac{x_{4}+1}{r_{14}^{3}}+m\left(-\frac{\left(x_{3}+1\right)\left(x_{4}-1\right)}{2 r_{13}^{3}}+\right. \\
& \left.\frac{\left(x_{3}-1\right)\left(x_{4}+1\right)}{2 r_{23}^{3}}+\frac{x_{4}-x_{3}}{r_{34}^{3}}-\frac{x_{4}^{2}-1}{2 r_{14}^{3}}+\frac{x_{4}^{2}-1}{2 r_{24}^{3}}\right) \\
F_{3}= & m\left(-\frac{y_{3}}{r_{13}^{3}}+\frac{y_{3}}{r_{23}^{3}}+\frac{y_{4}}{r_{24}^{3}}-\frac{y_{4}}{r_{14}^{3}}\right) \\
F_{4}= & \frac{y_{3}}{r_{13}^{3}}+\frac{y_{3}}{r_{23}^{3}}-\frac{y_{3}}{4}+m\left(-\frac{\left(x_{3}+1\right) y_{3}}{2 r_{13}^{3}}+\frac{\left(x_{3}+1\right) y_{3}}{2 r_{23}^{3}}-\frac{\left(x_{4}+1\right) y_{3}}{2 r_{14}^{3}}+\right. \\
& \left.\frac{y_{3}-y_{4}}{r_{34}^{3}}+\frac{\left(x_{4}-1\right) y_{3}+2 y_{4}}{2 r_{24}^{3}}\right) \\
F_{5}= & \frac{y_{4}}{r_{14}^{3}}+\frac{y_{4}}{r_{24}^{3}}-\frac{y_{4}}{4}+m\left(-\frac{\left(x_{3}+1\right) y_{4}}{2 r_{13}^{3}}-\frac{\left(x_{4}+1\right) y_{4}}{2 r_{14}^{3}}+\frac{\left(x_{4}+1\right) y_{4}}{2 r_{24}^{3}}+\right. \\
& \left.\frac{y_{4}-y_{3}}{r_{34}^{3}}+\frac{2 y_{3}+\left(x_{3}-1\right) y_{4}}{2 r_{23}^{3}}\right)
\end{aligned}
$$

# 3. Central configurations with $m=0$ 

When $m=0$ system (5) is equivalent to system

$$
\begin{array}{ll}
G\left(x_{3}, y_{3}\right)=0, & G\left(x_{4}, y_{4}\right)=0 \\
H\left(x_{3}, y_{3}\right)=0, & H\left(x_{4}, y_{4}\right)=0
\end{array}
$$

where

$$
\begin{aligned}
& G(x, y)=\frac{x-1}{\left((x-1)^{2}+y^{2}\right)^{3 / 2}}+\frac{x+1}{\left((x+1)^{2}+y^{2}\right)^{3 / 2}}-\frac{x}{4} \\
& H(x, y)=\frac{y}{\left((x-1)^{2}+y^{2}\right)^{3 / 2}}+\frac{y}{\left((x+1)^{2}+y^{2}\right)^{3 / 2}}-\frac{y}{4}
\end{aligned}
$$

Clearly $\left(x_{3}, y_{3}, x_{4}, y_{4}\right)$ is a solution of (6) if and only if $\left(x_{3}, y_{3}\right)$ (respectively, $\left.\left(x_{4}, y_{4}\right)\right)$ is a solution of

$$
G(x, y)=0, \quad H(x, y)=0
$$

Solving system (7) we find the following solutions

$$
\begin{array}{ll}
(x, y)=(0,0), & (x, y)=(0, \sqrt{3}), \quad(x, y)=(0,-\sqrt{3}) \\
(x, y)=(-\alpha, 0), & (x, y)=(\alpha, 0)
\end{array}
$$

where $\alpha=2.39681 \ldots$ is the unique real root of the equation $x^{5}-2 x^{3}-$ $8 x^{2}+x-8=0$.

We note that the five solutions of (7) that we have found correspond to the five relative equilibria of the restricted 3-body problem; the two equilateral triangle solutions and the three collinear solutions.

Since we have assumed that $x_{3}, y_{3} \geqslant 0$, the solutions of (6) satisfying

these conditions are

$$
\begin{array}{ll}
C_{1}: & \left(x_{3}, y_{3}\right)=(0,0), \quad\left(x_{4}, y_{4}\right)=(0,0), \\
C_{2}: & \left(x_{3}, y_{3}\right)=(0,0), \quad\left(x_{4}, y_{4}\right)=(0, \sqrt{3}), \\
C_{3}: & \left(x_{3}, y_{3}\right)=(0,0), \quad\left(x_{4}, y_{4}\right)=(0,-\sqrt{3}), \\
C_{4}: & \left(x_{3}, y_{3}\right)=(0,0), \quad\left(x_{4}, y_{4}\right)=(-\alpha, 0), \\
C_{5}: & \left(x_{3}, y_{3}\right)=(0,0), \quad\left(x_{4}, y_{4}\right)=(\alpha, 0), \\
C_{6}: & \left(x_{3}, y_{3}\right)=(0, \sqrt{3}), \quad\left(x_{4}, y_{4}\right)=(0,0), \\
C_{7}: & \left(x_{3}, y_{3}\right)=(0, \sqrt{3}), \quad\left(x_{4}, y_{4}\right)=(0, \sqrt{3}), \\
C_{8}: & \left(x_{3}, y_{3}\right)=(0, \sqrt{3}), \quad\left(x_{4}, y_{4}\right)=(0,-\sqrt{3}), \\
C_{9}: & \left(x_{3}, y_{3}\right)=(0, \sqrt{3}), \quad\left(x_{4}, y_{4}\right)=(-\alpha, 0), \\
C_{10}: & \left(x_{3}, y_{3}\right)=(0, \sqrt{3}), \quad\left(x_{4}, y_{4}\right)=(\alpha, 0), \\
C_{11}: & \left(x_{3}, y_{3}\right)=(\alpha, 0), \quad\left(x_{4}, y_{4}\right)=(0,0), \\
C_{12}: & \left(x_{3}, y_{3}\right)=(\alpha, 0), \quad\left(x_{4}, y_{4}\right)=(0, \sqrt{3}), \\
C_{13}: & \left(x_{3}, y_{3}\right)=(\alpha, 0), \quad\left(x_{4}, y_{4}\right)=(0,-\sqrt{3}), \\
C_{14}: & \left(x_{3}, y_{3}\right)=(\alpha, 0), \quad\left(x_{4}, y_{4}\right)=(-\alpha, 0), \\
C_{15}: & \left(x_{3}, y_{3}\right)=(\alpha, 0), \quad\left(x_{4}, y_{4}\right)=(\alpha, 0) .
\end{array}
$$

Notice that the solutions $C_{1}, C_{7}$, and $C_{15}$ correspond to central configurations where $m_{3}$ and $m_{4}$ are colliding.

The central configuration given by $C_{3}$ can be obtained from the one given by $C_{2}$ after doing a rotation of 180 degrees around the $x$-axis. The central configuration given by $C_{4}$ (respectively $C_{9}$ ) can be obtained from the one given by $C_{5}$ (respectively $C_{10}$ ) after doing a rotation of 180 degrees around the $y$-axis. The central configurations given by $C_{2}, C_{5}$ and $C_{12}$ can be obtained from the ones given by $C_{6}, C_{11}$ and $C_{10}$, respectively, after interchanging the names of the masses $m_{3}$ and $m_{4}$. The central configuration given by $C_{13}$ can be obtained from the one given by $C_{10}$ after doing a rotation of 180 degrees around the $x$-axis and interchanging the names of the masses $m_{3}$ and $m_{4}$.

Assuming that two different central configurations are equivalent if one can be obtained from the other one by doing either a rotation in dimension three or by interchanging the names of the masses $m_{3}$ and $m_{4}$, we have that for $m=0$ there are five non-equivalent classes of non-collision central configurations $C_{6}, C_{8}, C_{10}, C_{11}$ and $C_{14}$, and three non-equivalent classes of collision central configurations $C_{1}, C_{7}$ and $C_{15}$. This proves statement (a) of Theorem 2 .

# 4. Central configurations with $x_{3}=0$ and $x_{4}=0$ for $m>0$ small 

In this section we consider the kite central configurations; i.e, central configurations such that $x_{3}=0$ and $x_{4}=0$. More precisely, we will find the analytic expression of the kite central configurations of the 4 -body problem when $m_{1}=m_{2}=1$ and $m_{3}=m_{4}=m>0$ small that emanate from the central configurations with $m=0$ and $x_{3}=x_{4}=0$.

Without loss of generality we can assume that $y_{3} \geqslant 0$ and $y_{3} \geqslant y_{4}$. Under these conditions the first three equations of (5) are always satisfied and the last two equations become

$$
\begin{aligned}
& \widetilde{F}_{4}=m\left(\frac{y_{4}-y_{3}}{\left(y_{4}^{2}+1\right)^{3 / 2}}+\frac{1}{\left(y_{3}-y_{4}\right)^{2}}\right)+\frac{2 y_{3}}{\left(y_{3}^{2}+1\right)^{3 / 2}}-\frac{y_{3}}{4}=0 \\
& \widetilde{F}_{5}=m\left(\frac{y_{3}-y_{4}}{\left(y_{3}^{2}+1\right)^{3 / 2}}-\frac{1}{\left(y_{3}-y_{4}\right)^{2}}\right)+\frac{2 y_{4}}{\left(y_{4}^{2}+1\right)^{3 / 2}}-\frac{y_{4}}{4}=0
\end{aligned}
$$

Let $\mathbf{t}=\left(y_{3}, y_{4}\right)$. The solutions of (8) that provide non-equivalent noncollision kite central configurations with $m=0$ are $\mathbf{t}_{1}=(\sqrt{3}, 0)$ and $\mathbf{t}_{2}=$ $(\sqrt{3},-\sqrt{3})$. They correspond to the components $y_{3}$ and $y_{4}$ of the solutions $\mathbf{s}_{1}$ and $\mathbf{s}_{2}$ given in Theorem 2(a.1). The solutions that provide non-equivalent collision kite central configurations with $m=0$ are $\mathbf{t c}_{1}=(0,0)$ and $\mathbf{t c}_{2}=$ $(\sqrt{3}, \sqrt{3})$. They correspond to the components $y_{3}$ and $y_{4}$ of the solutions $\mathbf{s c}_{1}$ and $\mathbf{s c}_{2}$ given in Theorem 2(a.2).

In our analysis the central configurations with $x_{3}=x_{4}=0$ and $y_{4}=-y_{3}$ will play an important role. So first we analyze them.

### 4.1. Central configurations with $x_{3}=x_{4}=0$ and $y_{4}=-y_{3}$

When $y_{4}=-y_{3}$ system (8) is equivalent to equation

$$
\frac{2 y_{3}}{\left(y_{3}^{2}+1\right)^{3 / 2}}-\frac{y_{3}}{4}+m\left(\frac{1}{4 y_{3}^{2}}-\frac{2 y_{3}}{\left(y_{3}^{2}+1\right)^{3 / 2}}\right)=0
$$

By solving this equation with respect to $m$ we get

$$
m=f\left(y_{3}\right)=-\frac{\frac{2 y_{3}}{\left(y_{3}^{2}+1\right)^{3 / 2}}-\frac{y_{3}}{4}}{\frac{1}{4 y_{3}^{2}}-\frac{2 y_{3}}{\left(y_{3}^{2}+1\right)^{3 / 2}}}
$$

It is not difficult to see that the numerator of $m$ equals zero when $y_{3}=0$ and $y_{3}= \pm \sqrt{3}$, and the denominator of $m$ equals zero when $y_{3}=1 / \sqrt{3}$.


The graph of the function $f(y)$ for $y \geqslant 0$.

Then analyzing the sign of $m$ for $y_{3} \geqslant 0$ we have that $m>0$ for $y_{3} \in$ $(1 / \sqrt{3}, \sqrt{3}), m=0$ for $y_{3}=0$ and $y_{3}=\sqrt{3}$, and $m<0$ for $y_{3} \in(0,1 / \sqrt{3}) \cup$ $(\sqrt{3},+\infty)$. Furthermore we can prove easily that $f\left(y_{3}\right)$ is decreasing for all $y_{3} \in(1 / \sqrt{3}, \sqrt{3}), f(\sqrt{3})=0$ and $\lim _{y_{3} \rightarrow(1 / \sqrt{3})^{+}}=+\infty$ (see Figure 4). This proves the following lemma.

Lemma 4. There exists a unique family of kite central configurations with $y_{4}=-y_{3}$ and $y_{3} \geqslant 0$ defined for all $m \geqslant 0$. This family is given by $y_{3}=y_{3}(m)=f^{-1}(m)$, and it satisfies that $y_{3} \in(1 / \sqrt{3}, \sqrt{3}]$, and that $y_{3} \rightarrow \sqrt{3}$ when $m \rightarrow 0$, and $y_{3} \rightarrow 1 / \sqrt{3}$ when $m \rightarrow+\infty$.
4.2. Central configurations with $m>0$ small emanating from the solutions $\mathbf{t}_{1}$ and $\mathbf{t}_{2}$
Notice that system (8) is analytic with respect to all its variables except at the points corresponding to binary collisions between the masses. Therefore it is analytic in a neighborhood of the solutions $\mathbf{t}_{1}$ and $\mathbf{t}_{2}$.

Let

$$
D=\left|\begin{array}{ll}
\frac{\partial \widetilde{F}_{4}}{\partial y_{3}} & \frac{\partial \widetilde{F}_{4}}{\partial y_{4}} \\
\frac{\partial \widetilde{F}_{5}}{\partial y_{3}} & \frac{\partial \widetilde{F}_{5}}{\partial y_{4}}
\end{array}\right|
$$

It is easy to check that

$$
\left.D\right|_{m=0, \mathbf{t}=\mathbf{t}_{1}}=-\frac{63}{64} \neq 0,\left.\quad D\right|_{m=0, \mathbf{t}=\mathbf{t}_{2}}=\frac{81}{256} \neq 0
$$

Therefore from the Implicit Function Theorem we can find unique analytic functions $y_{3}^{i}(m)$ and $y_{4}^{i}(m)$ satisfying system (8) and $\left(y_{3}^{i}(0), y_{4}^{i}(0)\right)=\mathbf{t}_{i}$ for $i=1,2$ which are defined in a sufficiently small neighborhood $U$ of $m=0$.

Next we analyze the functions $y_{3}^{i}(m)$ and $y_{4}^{i}(m)$. Let $\mathbf{t}^{i}(m)=\left(y_{3}^{i}(m)\right.$, $\left.y_{4}^{i}(m)\right)$ with

$$
y_{3}^{i}(m)=\sum_{k=0}^{\infty} y_{3 k}^{i} m^{k}, \quad y_{4}^{i}(m)=\sum_{k=0}^{\infty} y_{4 k}^{i} m^{k}
$$

and $\left(y_{30}^{i}, y_{40}^{i}\right)=\mathbf{t}_{i}$; and let

$$
\left.\widetilde{F}_{4}\right|_{\mathbf{t}=\mathbf{t}^{i}(m)}=\sum_{k=0}^{\infty} d_{4 k}^{i} m^{k},\left.\quad \widetilde{F}_{5}\right|_{\mathbf{t}=\mathbf{t}^{i}(m)}=\sum_{k=0}^{\infty} d_{5 k}^{i} m^{k}
$$

be the expansion in power series of $m$ of the functions $\widetilde{F}_{4}$ and $\widetilde{F}_{5}$ evaluated at $\mathbf{t}=\mathbf{t}^{i}(m)$. Clearly $\mathbf{t}^{i}(m)$ is a solution of system (8) if and only if $d_{4 k}^{i}=0$ and $d_{5 k}^{i}=0$ for all $k \in \mathbb{N} \cup\{0\}$. Moreover since $\left(y_{30}^{i}, y_{40}^{i}\right)$ is a solution of system (8) for $m=0$, the terms of order 0 of the power series expansions (9) are zero; that is, $d_{40}^{i}=0$ and $d_{50}^{i}=0$.

Case $i=1$. By computing the terms of order 1 of the power series expansions (9) we get

$$
d_{41}^{1}=\frac{1}{48}\left(-27 y_{31}-48 \sqrt{3}+16\right), \quad d_{51}^{1}=\frac{1}{24}\left(42 y_{41}+3 \sqrt{3}-8\right)
$$

We equate these terms to zero and we obtain

$$
y_{31}=\frac{16(1-3 \sqrt{3})}{27}, \quad y_{41}=\frac{8-3 \sqrt{3}}{42}
$$

We substitute the values of $y_{31}$ and $y_{41}$ into the expression of $\mathbf{t}^{1}(m)$, and then we compute the terms of order 2 of the power series expansions (9) obtaining

$$
d_{42}^{1}=\frac{-15309 y_{32}+62824 \sqrt{3}+7920}{27216}, \quad d_{52}^{1}=\frac{47628 y_{42}+10235 \sqrt{3}-34128}{27216}
$$

By equating these terms to zero we get

$$
y_{32}=\frac{8(990+7853 \sqrt{3})}{15309}, \quad y_{42}=\frac{34128-10235 \sqrt{3}}{47628}
$$

In short,

$$
\begin{aligned}
& y_{3}^{1}(m)=\sqrt{3}+\frac{16(1-3 \sqrt{3})}{27} m+\frac{8(990+7853 \sqrt{3})}{15309} m^{2}+O\left(m^{3}\right) \\
& y_{4}^{1}(m)=\frac{8-3 \sqrt{3}}{42} m+\frac{34128-10235 \sqrt{3}}{47628} m^{2}+O\left(m^{3}\right)
\end{aligned}
$$

Case $i=2$. Proceeding as in the case $i=1$ we get

$$
\begin{aligned}
& y_{3}^{2}(m)=\sqrt{3}+\frac{4}{27}(1-3 \sqrt{3}) m+\frac{4(90-101 \sqrt{3})}{2187} m^{2}+O\left(m^{3}\right) \\
& y_{4}^{2}(m)=-\sqrt{3}-\frac{4}{27}(1-3 \sqrt{3}) m-\frac{4(90-101 \sqrt{3})}{2187} m^{2}+O\left(m^{3}\right)
\end{aligned}
$$

By observing the first terms of the expansion of $y_{3}^{2}(m)$ and $y_{4}^{2}(m)$ in power series of $m$ we claim that the solution $\mathbf{t}^{2}(m)$ satisfies that $y_{4}^{2}(m)=-y_{3}^{2}(m)$. The proof of the claim is an immediate consequence of the uniqueness of the solution $\mathbf{t}^{2}(m)=\left(y_{3}^{2}(m), y_{4}^{2}(m)\right)$ together with Lemma 4 , which assures the existence of a solution of system (8) with $y_{4}=-y_{3}$ satisfying that $y_{3} \rightarrow \sqrt{3}$ when $m \rightarrow 0$. In short we have proved the following result.

Proposition 5. The following statements hold.
(a) There exists a unique family $\mathbf{t}^{1}(m)=\left(y_{3}^{1}(m), y_{4}^{1}(m)\right)$, with $y_{3}^{1}(m)$ and $y_{4}^{1}(m)$ given by (10), of kite central configurations emanating from the central configuration with $m=0, x_{3}=x_{4}=0$ and $\left(y_{3}, y_{4}\right)=(\sqrt{3}, 0)$.
(b) There exists a unique family $\mathbf{t}^{2}(m)=\left(y_{3}^{2}(m), y_{4}^{2}(m)\right)$, with $y_{4}^{2}(m)=$ $-y_{3}^{2}(m)$ and $y_{3}^{2}(m)$ given by (11), of kite central configurations emanating from the central configuration with $m=0, x_{3}=x_{4}=0$ and $\left(y_{3}, y_{4}\right)=(\sqrt{3},-\sqrt{3})$.
4.3. Central configurations with $m>0$ small emanating from the solutions $\mathbf{t c}_{1}$ and $\mathbf{t c}_{2}$
Next we analyze the existence of families of central configurations with $x_{3}=0$ and $x_{4}=0$ emanating from the collision solutions $\mathbf{t c}_{1}$ and $\mathbf{t c}_{2}$.

We define two new equations in the following way

$$
\begin{gathered}
\bar{F}=\widetilde{F}_{4}+\widetilde{F}_{5}=m\left(\frac{y_{3}-y_{4}}{\left(y_{3}^{2}+1\right)^{3 / 2}}-\frac{y_{3}-y_{4}}{\left(y_{4}^{2}+1\right)^{3 / 2}}\right)+\frac{2 y_{3}}{\left(y_{3}^{2}+1\right)^{3 / 2}} \\
-\frac{y_{3}}{4}+\frac{2 y_{4}}{\left(y_{4}^{2}+1\right)^{3 / 2}}-\frac{y_{4}}{4}=0 \\
\bar{G}=\left(y_{3}-y_{4}\right)^{2} \widetilde{F}_{4}=0
\end{gathered}
$$

Obviously, a solution of system (8) is also a solution of (12). Furthermore the functions $\bar{F}$ and $\bar{G}$ are analytic with respect to all its variables. So we shall work with system (12) instead of (8).

Let now

$$
D=\left|\begin{array}{ll}
\frac{\partial \bar{F}}{\partial m} & \frac{\partial \bar{F}}{\partial y_{4}} \\
\frac{\partial \bar{G}}{\partial m} & \frac{\partial \bar{G}}{\partial y_{4}}
\end{array}\right|
$$

It is easy to check that

$$
\left.D\right|_{m=0, \mathbf{t}=\mathbf{t c}_{1}}=-\frac{7}{4} \neq 0,\left.\quad D\right|_{m=0, \mathbf{t}=\mathbf{t c}_{2}}=\frac{9}{16} \neq 0
$$

Therefore, from the Implicit Function Theorem, we can find unique analytic functions $m^{i}\left(y_{3}\right)$ and $y_{4}^{i}\left(y_{3}\right)$ satisfying system (12) and $m^{1}(0)=0, m^{2}(\sqrt{3})=$ $0, y_{4}^{1}(0)=0$ and $y_{4}^{2}(\sqrt{3})=\sqrt{3}$ which are defined in a sufficiently small neighborhood $V$ of $y_{3}=\left.y_{30}^{i}=\left.y_{3}\right|_{\mathbf{t}=\mathbf{t c}_{i}}$ for $i=1,2$.

Next we analyze the functions $m^{i}\left(y_{3}\right)$ and $y_{4}^{i}\left(y_{3}\right)$ by proceeding in a similar way than in Subsection 4.2. Let $Y_{3}=y_{3}-y_{30}^{i}, \tau^{i}\left(Y_{3}\right)=\left(m^{i}\left(Y_{3}\right), y_{4}^{i}\left(Y_{3}\right)\right)$, let

$$
m^{i}\left(Y_{3}\right)=\sum_{k=0}^{\infty} m_{k}^{i} Y_{3}^{k}, \quad y_{4}^{i}\left(Y_{3}\right)=\sum_{k=0}^{\infty} y_{4 k}^{i} Y_{3}^{k}
$$

where $m_{0}=0,\left.y_{40}^{i}=\left.y_{4}\right|_{\mathbf{t}=\mathbf{t c}_{i}}\right;$ and let

$$
\left.\bar{F}\right|_{\left(m, y_{4}\right)=\tau^{i}\left(Y_{3}\right)}=\sum_{k=0}^{\infty} \bar{f}_{k}^{i} Y_{3}^{k},\left.\quad \bar{G}\right|_{\left(m, y_{4}\right)=\tau^{i}\left(Y_{3}\right)}=\sum_{k=0}^{\infty} \bar{g}_{k}^{i} Y_{3}^{k}
$$

be the expansion in power series of $Y_{3}$ of the functions $\bar{F}$ and $\bar{G}$ evaluated at $m=m^{i}\left(Y_{3}\right), y_{4}=y_{4}^{i}\left(Y_{3}\right)$.

The terms of order 0 of the power series expansions (13), $\bar{F}_{0}^{i}=0$ and $\bar{G}_{0}^{i}=0$, are zero because $m=m_{0}^{i}$ and $y_{4}=y_{40}^{i}$ is a solution of system (12) for $Y_{3}=0$. Next we analyze higher order terms of this power series expansions.

Case $i=1$. After some computations we see that the terms of order 1 of the power series expansions (13) are

$$
\bar{f}_{1}^{1}=\frac{7 y_{41}}{4}+\frac{7}{4}, \quad \bar{g}_{1}^{1}=m_{1}
$$

By equating these terms to zero we get $m_{1}=0$ and $y_{41}=-1$. We substitute them into the expressions of $m^{i}\left(Y_{3}\right)$ and $y_{4}^{i}\left(Y_{3}\right)$, and then we compute the terms of order 2 of the power series expansions (13) obtaining

$$
\bar{f}_{2}^{1}=\frac{7 y_{42}}{4}, \quad \bar{g}_{2}^{1}=m_{2}
$$

We equate these terms to zero and we get $m_{2}=0$ and $y_{42}=0$. By computing the terms of order 3 of the power series expansions (13) we get

$$
\bar{f}_{3}^{1}=\frac{7 y_{43}}{4}, \quad \bar{g}_{3}^{1}=m_{3}+7
$$

So $m_{3}=-7$ and $y_{43}=0$. By computing the terms of order 4 of the power series expansions (13) we get

$$
\bar{f}_{4}^{1}=\frac{7 y_{44}}{4}, \quad \bar{g}_{4}^{1}=m_{4}
$$

therefore $m_{4}=0$ and $y_{44}=0$. By computing the terms of order 5 of the power series expansions (13) we get

$$
\bar{f}_{5}^{1}=\frac{7 y_{45}}{4}, \quad \bar{g}_{5}^{1}=m_{5}-12
$$

hence $m_{5}=12$ and $y_{45}=0$. In short,

$$
m^{1}\left(Y_{3}\right)=-7 Y_{3}^{3}+12 Y_{3}^{5}+O\left(Y_{3}^{6}\right), \quad y_{4}^{1}\left(Y_{3}\right)=-Y_{3}+O\left(Y_{3}^{6}\right)
$$

By observing the first terms of the power series expansions of $m^{1}\left(Y_{3}\right)$ and $y_{4}^{1}\left(Y_{3}\right)$ we claim that $y_{4}^{1}\left(Y_{3}\right)=-Y 3$. Indeed, we have proved that $m^{1}\left(Y_{3}\right)$ and $y_{4}^{1}\left(Y_{3}\right)$ are the unique functions satisfying (12), and consequently satisfying (8). Moreover in Section 4.1 we have proved that there exists a family of solutions of (8) with $y_{4}=-y_{3}$ which is defined in a neighborhood of $y_{3}=0$. Therefore we can conclude that $y_{4}^{1}\left(Y_{3}\right)=-Y_{3}$ which proves the claim. This solution does not provide a family of central configurations with $x_{3}=x_{4}=0$ because on this family $m<0$ (see Figure 4).

Case $i=2$. Proceeding as in the case $i=1$ we get

$$
\begin{aligned}
m^{2}\left(Y_{3}\right)= & \frac{9 Y_{3}^{3}}{4}-\frac{27 \sqrt{3} Y_{3}^{4}}{32}+\frac{195 Y_{3}^{5}}{256}+O\left(Y_{3}^{6}\right) \\
y_{4}^{2}\left(Y_{3}\right)= & \sqrt{3}-Y_{3}+\frac{\sqrt{3} Y_{3}^{2}}{4}-\frac{3 Y_{3}^{3}}{16}- \\
& \frac{7 \sqrt{3} Y_{3}^{4}}{768}+\frac{3(31-512 \sqrt{3}) Y_{3}^{5}}{1024}+O\left(Y_{3}^{6}\right)
\end{aligned}
$$

where $Y_{3}=y_{3}-\sqrt{3}$.
In short we have proved the following result.

The graph of the functions $y_{3}(m)$ (continuous line) and $y_{4}(m)$ (dashed line), for $m \in(0,1]$, on the families of central configurations given by Propositions 5 and 6 .

Proposition 6. The following statements hold.
(a) There is no family of kite central configurations emanating from the collision central configuration with $m=0, x_{3}=x_{4}=0$ and $\left(y_{3}, y_{4}\right)=$ $(0,0)$.
(b) There exists a unique family $\mathbf{t c}^{2}$ of kite central configurations emanating from the collision central configuration with $m=0, x_{3}=x_{4}=0$ and $\left(y_{3}, y_{4}\right)=(\sqrt{3}, \sqrt{3})$. This family is given by (14).
4.4. Numerical study of the families of central configurations with $x_{3}=x_{4}=$ 0

With the help of Mathematica, we have followed the families of central configurations $\mathbf{t}^{1}, \mathbf{t}^{2}$ and $\mathbf{t c}^{2}$ given by Propositions 5 and 6 respectively from $m=0$ to $m=1$. The results that we have obtained are plotted in Figure 5.

It is well known that there are three different classes of planar noncollinear central configurations of the four-body problem with equal masses:

the square, an equilateral triangle with a mass at its center, and an isosceles triangle with one mass on its axis of symmetry (see ).

By computing the solutions of system (8) when $m=1$ we find exactly three real solutions satisfying $y_{3} \geqslant 0$ and $y_{3} \geqslant y_{4}$,
(i) the solution $y_{3}=\sqrt{3}, y_{4}=1 / \sqrt{3}$ which belongs to the family $\mathbf{t}^{1}$ and provides an equilateral triangle with the mass $m_{4}$ at its center
(ii) the solution $y_{3}=1, y_{4}=-1$ which belongs to the family $\mathbf{t}^{2}$ and provides a square
(iii) the solution $y_{3}=1.81723 \ldots, y_{4}=0.650378 \ldots$ which belongs to the family $\mathbf{t c}^{2}$ and provides an isosceles triangle with the masses $m_{3}$ and $m_{4}$ on its axis of symmetry.

# 5. Central configurations with $y_{3}=0$ and $y_{4}=0$ for $m>0$ small 

In this section we consider the collinear central configurations; i.e. central configurations such that that $y_{3}=0$ and $y_{4}=0$. Without loss of generality we can assume that $x_{3} \geqslant 0$ and $x_{3} \geqslant x_{4}$. Under these conditions the last three equations of (5) are always satisfied, and the first two equations become

$$
\widetilde{F}_{1}=0, \quad \widetilde{F}_{2}=0
$$

with

$$
\begin{aligned}
\widetilde{F}_{1}= & -\frac{x_{3}}{4}+\frac{x_{3}-1}{\left|x_{3}-1\right|^{3}}+\frac{1}{\left(x_{3}+1\right)^{2}}+m\left(-\frac{x_{3}-1}{2\left(x_{3}+1\right)^{2}}+\right. \\
& \frac{\left(x_{4}-1\right)\left(x_{3}+1\right)}{2\left|x_{4}-1\right|^{3}}+\frac{x_{3}^{2}-1}{2\left|x_{3}-1\right|^{3}}-\frac{\left(x_{3}-1\right)\left(x_{4}+1\right)}{2\left|x_{4}+1\right|^{3}}+\frac{1}{\left(x_{3}-x_{4}\right)^{2}} \\
\widetilde{F}_{2}= & -\frac{x_{4}}{4}+\frac{x_{4}-1}{\left|x_{4}-1\right|^{3}}+\frac{x_{4}+1}{\left|x_{4}+1\right|^{3}}+m\left(-\frac{\left(x_{4}-1\right)}{2\left(x_{3}+1\right)^{2}}-\right. \\
& \left.\frac{x_{4}^{2}-1}{2\left|x_{4}+1\right|^{3}}+\frac{\left(x_{3}-1\right)\left(x_{4}+1\right)}{2\left|x_{3}-1\right|^{3}}+\frac{x_{4}^{2}-1}{2\left|x_{4}-1\right|^{3}}-\frac{1}{\left(x_{3}-x_{4}\right)^{2}}\right)
\end{aligned}
$$

Let $\mathbf{r}=\left(x_{3}, x_{4}\right)$. The solutions of (15) that provide non-equivalent noncollision collinear central configurations with $m=0$ are $\mathbf{r}_{1}=(\alpha, 0)$ and $\mathbf{r}_{2}=(\alpha,-\alpha)$, where $\alpha=2.39681 \ldots$ is the unique real root of the equation $x^{5}-2 x^{3}-8 x^{2}+x-8=0$. These solutions correspond to the components $x_{3}$ and $x_{4}$ of the solutions $\mathbf{s}_{3}$ and $\mathbf{s}_{4}$ given in Theorem 2(a.1). The solutions of (15) that provide non-equivalent collision collinear central configurations

The graph of the function $g(x)$ for $x \geqslant 0$.
with with $m=0$ are $\mathbf{r c}_{1}=(0,0)$ and $\mathbf{r c}_{2}=(\alpha, \alpha)$. They correspond to the components $x_{3}$ and $x_{4}$ of the solutions $\mathbf{s c}_{1}$ and $\mathbf{s c}_{3}$ given in Theorem 2(a.2)).

We start analyzing the collinear central configurations with $x_{4}=-x_{3}$, which play an important role in our study.

# 5.1. Central configurations with $y_{3}=y_{4}=0$ and $x_{4}=-x_{3}$ 

When $x_{4}=-x_{3}$ system (15) is equivalent to equation

$$
-\frac{x_{3}}{4}+\frac{x_{3}-1}{\left|x_{3}-1\right|^{3}}+\frac{1}{\left(x_{3}+1\right)^{2}}+m\left(\frac{1}{4 x_{3}^{2}}+\frac{\left(x_{3}-1\right) x_{3}}{\left|x_{3}-1\right|^{3}}-\frac{x_{3}}{\left(x_{3}+1\right)^{2}}\right)=0
$$

By solving this equation with respect to $m$ we get

$$
m=g\left(x_{3}\right)=-\frac{-\frac{x_{3}}{4}+\frac{x_{3}-1}{\left|x_{3}-1\right|^{3}}+\frac{1}{\left(x_{3}+1\right)^{2}}}{\frac{1}{4 x_{3}^{2}}+\frac{\left(x_{3}-1\right) x_{3}}{\left|x_{3}-1\right|^{3}}-\frac{x_{3}}{\left(x_{3}+1\right)^{2}}}
$$

It is not difficult to prove that the numerator of $m$ equals zero when $x_{3}=$ 0 and $x_{3}=\alpha$, and the denominator of $m$ equals zero when $x_{3}=\beta=$ $0.417220 \ldots$, where $\beta$ is the unique real root of equation $8 x^{5}-x^{4}+8 x^{3}+$ $2 x^{2}-1=0$. Analyzing the sign of $m$ when $x_{3} \geqslant 0$ we have that $m>0$ for $x_{3} \in(0, \beta) \cup(\alpha,+\infty), m=0$ when $x_{3}=0$ and $x_{3}=\alpha$, and $m<0$ when $x_{3} \in(\beta, \alpha)$. Moreover, the function $g\left(x_{3}\right)$ is increasing in $[0, \beta) \cup$ $(\beta,+\infty), g(0)=0, g(\alpha)=0$ and $\lim _{x_{3} \rightarrow \beta^{-}}=+\infty$ and $\lim _{x_{3} \rightarrow+\infty}=+\infty$ (see Figure 6). This proves the following lemma.

Lemma 7. For all $m \geqslant 0$ there exist two families of collinear central configurations with $x_{4}=-x_{3}$ and $x_{3} \geqslant 0$, one for each branch of $x_{3}(m)=g^{-1}(m)$.

(a) A family $x_{3}(m) \in(0, \beta)$ for $m>0$ satisfying that $x_{3}(m) \rightarrow 0$ when $m \rightarrow 0$, and $x_{3}(m) \rightarrow \beta$ when $m \rightarrow+\infty$.
(b) A family $x_{3}(m) \in(\alpha,+\infty)$ for $m>0$ satisfying that $x_{3}(m) \rightarrow \alpha$ when $m \rightarrow 0$, and $x_{3}(m) \rightarrow+\infty$ when $m \rightarrow+\infty$.
5.2. Central configurations with $m>0$ small emanating from the solutions $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$

Notice that system (15) is analytic with respect to all its variables except at the points corresponding to binary collisions between the masses. Therefore it is analytic in a neighborhood of the solutions $\mathbf{r}_{1}$ and $\mathbf{r}_{2}$.

Let

$$
\widetilde{D}=\left|\begin{array}{ll}
\frac{\partial \widetilde{F}_{1}}{\partial x_{3}} & \frac{\partial \widetilde{F}_{1}}{\partial x_{4}} \\
\frac{\partial \widetilde{F}_{2}}{\partial x_{3}} & \frac{\partial \widetilde{F}_{2}}{\partial x_{4}}
\end{array}\right|
$$

It is easy to check that

$$
\begin{aligned}
& \left.D\right|_{m=0, \mathbf{r}=\mathbf{r}_{1}}=\frac{17\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)}{16\left(\alpha^{2}-1\right)^{3}}=4.39829 \cdots \neq 0 \\
& \left.D\right|_{m=0, \mathbf{r}=\mathbf{r}_{2}}=\frac{\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)^{2}}{16\left(\alpha^{2}-1\right)^{6}}=1.07100 \cdots \neq 0
\end{aligned}
$$

Therefore from the Implicit Function Theorem we can find unique analytic functions $x_{3}^{i}(m)$ and $x_{4}^{i}(m)$ satisfying system (15) and $\left(x_{3}^{i}(0), x_{4}^{i}(0)\right)=\mathbf{r}_{i}$ for $i=1,2$ which are defined in a sufficiently small neighborhood $U$ of $m=0$.

Next we analyze the functions $x_{3}^{i}(m)$ and $x_{4}^{i}(m)$ by proceeding as in Section 4.2. Let $\mathbf{r}^{i}(m)=\left(x_{3}^{i}(m), x_{4}^{i}(m)\right)$ with

$$
x_{3}^{i}(m)=\sum_{k=0}^{\infty} x_{3 k}^{i} m^{k}, \quad x_{4}^{i}(m)=\sum_{k=0}^{\infty} x_{4 k}^{i} m^{k}
$$

where $\left(x_{30}^{i}, x_{40}^{i}\right)=\mathbf{r}_{i}$. We expand the functions $\widetilde{F}_{1}$ and $\widetilde{F}_{2}$ evaluated at $\mathbf{r}=\mathbf{r}^{i}(m)$ in power series of $m$. By computing the first terms of these power

series expansions and equating them to zero we get

$$
\begin{aligned}
x_{3}^{1}(m) & =\alpha-\frac{4\left(\alpha^{2}-1\right)\left(\alpha^{7}-2 \alpha^{5}-4 \alpha^{4}+\alpha^{3}+\alpha^{2}-1\right)}{\alpha^{2}\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)} m+O\left(m^{2}\right) \\
& =2.39681 \cdots-1.36514 \ldots m+O\left(m^{2}\right) \\
x_{4}^{1}(m) & =\frac{4\left(3 \alpha^{2}-1\right)}{17 \alpha^{2}\left(\alpha^{2}-1\right)^{2}} m+O\left(m^{2}\right)=0.0295360 \ldots m+O\left(m^{2}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
x_{3}^{2}(m) & =\alpha+\frac{\left(\alpha^{2}-1\right)\left(17 \alpha^{4}-2 \alpha^{2}+1\right)}{\alpha^{2}\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)} m+O\left(m^{2}\right) \\
& =2.39681 \cdots+1.02836 \ldots m+O\left(m^{2}\right) \\
x_{4}^{2}(m) & =-\alpha-\frac{\left(\alpha^{2}-1\right)\left(17 \alpha^{4}-2 \alpha^{2}+1\right)}{\alpha^{2}\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)} m+O\left(m^{2}\right) \\
& =-2.39681 \cdots-1.02836 \ldots m+O\left(m^{2}\right)
\end{aligned}
$$

By observing the first terms of the expansions of $x_{3}^{2}(m)$ and $x_{4}^{2}(m)$ in power series of $m$ we claim that the solution $\mathbf{r}^{2}(m)$ satisfies that $x_{4}^{2}(m)=-x_{3}^{2}(m)$. The proof of the claim is an immediate consequence of the uniqueness of the solution $\mathbf{r}^{2}(m)=\left(x_{3}^{2}(m), x_{4}^{2}(m)\right)$ together with Lemma 7 , which assures the existence of a solution of system (8) with $x_{4}=-x_{3}$ satisfying that $x_{3} \rightarrow \alpha$ when $m \rightarrow 0$. In short we have proved the following result.

Proposition 8. The following statements hold.
(a) There exists a unique family $\mathbf{r}^{1}(m)=\left(x_{3}^{1}(m), x_{4}^{1}(m)\right)$, with $x_{3}^{1}(m)$ and $x_{4}^{1}(m)$ given by (16), of collinear central configurations emanating from the central configuration with $m=0, y_{3}=y_{4}=0$ and $\left(x_{3}, x_{4}\right)=(\alpha, 0)$.
(b) There exists a unique family $\mathbf{r}^{2}(m)=\left(x_{3}^{2}(m),-x_{3}^{2}(m)\right)$, with $x_{3}^{2}(m)$ is given by (17), of collinear central configurations emanating from the central configuration with $m=0, y_{3}=y_{4}=0\left(x_{3}, x_{4}\right)=(\alpha,-\alpha)$.
5.3. Central configurations with $m>0$ small emanating from the solutions $\mathbf{r c}_{1}$ and $\mathbf{r c}_{2}$
Next we analyze the existence of families of central configurations with $y_{3}=0$ and $y_{4}=0$ emanating from the collision solutions $\mathbf{r c}_{1}$ and $\mathbf{r c}_{2}$.

We define two new equations

$$
\bar{F}=\widetilde{F}_{1}+\widetilde{F}_{2}=0, \quad \bar{G}=\left(x_{3}-x_{4}\right)^{2} \widetilde{F}_{1}=0
$$

Obviously, a solution of system (8) is also a solution of (18) and the functions $\bar{F}$ and $\bar{G}$ are analytic with respect to all its variables except when $x_{3}=1$ and $x_{4}= \pm 1$ (remember that we have considered only solutions with $x_{3} \geqslant 0$ ); i.e. at the binary collisions between $m_{3}$ and $m_{2}, m_{4}$ and $m_{1}$, and $m_{4}$ and $m_{2}$. Therefore $\bar{F}$ and $\bar{G}$ are analytic in a neighborhood of $\mathbf{r c}_{1}$ and $\mathbf{r c}_{2}$.

We shall work with system (18) instead of (8). Let now

$$
D=\left|\begin{array}{ll}
\frac{\partial \bar{F}}{\partial m} & \frac{\partial \bar{F}}{\partial y_{4}} \\
\frac{\partial \bar{G}}{\partial m} & \frac{\partial \bar{G}}{\partial y_{4}}
\end{array}\right|
$$

It is easy to check that

$$
\begin{aligned}
& \left.D\right|_{m=0, \mathbf{r}=\mathbf{r c}_{1}}=\frac{17}{4} \neq 0 \\
& \left.D\right|_{m=0, \mathbf{r}=\mathbf{r c}_{2}}=\frac{\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1}{4\left(\alpha^{2}-1\right)^{3}}=1.03489 \cdots \neq 0
\end{aligned}
$$

Therefore from the Implicit Function Theorem we can find unique analytic functions $m^{i}\left(x_{3}\right)$ and $x_{4}^{i}\left(x_{3}\right)$ satisfying system (18) and $m^{1}(0)=0$, $m^{2}(\alpha)=0, x_{4}^{1}(0)=0$ and $x_{4}^{2}(\alpha)=\alpha$ which are defined in a sufficiently small neighborhood $V$ of $x_{3}=\left.x_{30}^{i}=\left.x_{3}\right|_{\mathbf{r}=\mathbf{r c}_{i}}$ with $i=1,2$.

Next we analyze the functions $m^{i}\left(x_{3}\right)$ and $x_{4}^{i}\left(x_{3}\right)$. Let $X_{3}=x_{3}-x_{30}^{i}$, $\rho^{i}\left(X_{3}\right)=\left(m^{i}\left(X_{3}\right), x_{4}^{i}\left(X_{3}\right)\right)$ with

$$
m^{i}\left(X_{3}\right)=\sum_{k=0}^{\infty} m_{k}^{i} X_{3}^{k}, \quad x_{4}^{i}\left(X_{3}\right)=\sum_{k=0}^{\infty} x_{4 k}^{i} X_{3}^{k}
$$

and $m_{0}=0, x_{40}^{i}=\left.x_{4}\right|_{\mathbf{r}=\mathbf{r c}_{i}}$. By proceeding as in Subsection 4.3 for $i=1$ we get

$$
\begin{aligned}
m^{1}\left(X_{3}\right) & =17 X_{3}^{3}+32 X_{3}^{5}+O\left(X_{3}^{6}\right) \\
x_{4}^{1}\left(X_{3}\right) & =-X_{3}+O\left(X_{3}^{6}\right)
\end{aligned}
$$

where $X_{3}=x_{3}$. We claim that $x_{4}^{1}\left(X_{3}\right)=-X_{3}$. The proof of the claim is an immediate consequence of the fact that $m^{1}\left(X_{3}\right)$ and $x_{4}^{1}\left(X_{3}\right)$ are the unique functions satisfying (18), $m^{1}(0)=0$ and $x_{4}^{1}(0)=0$ together with the fact that there exists a family of of collinear central configurations with $x_{4}=-x_{3}$ defined in a neighborhood of $x_{3}=0$ (see Lemma 7(a)).

For $i=2$ we get

$$
\begin{aligned}
m^{2}\left(X_{3}\right) & =m_{3} X_{3}^{3}+O\left(X_{3}^{4}\right) \\
x_{4}^{2}\left(X_{3}\right) & =\alpha-X_{3}+x_{42}^{2} X_{3}^{2}+x_{43}^{2} X_{3}^{3}+O\left(X_{3}^{4}\right)
\end{aligned}
$$

where $X_{3}=x_{3}-\alpha$ and

$$
\begin{aligned}
m_{3}= & -\left(\alpha^{2}-1\right)^{-3}\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)^{-1} \\
& \left(47 \alpha^{12}-170 \alpha^{10}-752 \alpha^{9}+209 \alpha^{8}+704 \alpha^{7}+2356 \alpha^{6}+\right. \\
& \left.736 \alpha^{5}+2913 \alpha^{4}-576 \alpha^{3}+150 \alpha^{2}-112 \alpha+639\right)=4.13957 \ldots \\
x_{42}^{2}= & \frac{16\left(3 \alpha^{7}-5 \alpha^{5}-21 \alpha^{4}+\alpha^{3}-14 \alpha^{2}+\alpha-5\right)}{\left(\alpha^{2}-1\right)\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)}=1.56656 \ldots \\
x_{43}^{2}= & -16\left(\alpha^{2}-1\right)^{-2}\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)^{-2} \\
& \left(141 \alpha^{14}-463 \alpha^{12}-2112 \alpha^{11}+457 \alpha^{10}+1984 \alpha^{9}+6269 \alpha^{8}+\right. \\
& 1664 \alpha^{7}+4375 \alpha^{6}-896 \alpha^{5}-1917 \alpha^{4}-576 \alpha^{3}-45 \alpha^{2}- \\
& 64 \alpha+399)=10.5053 \ldots
\end{aligned}
$$

In short, we have proved the following result.
Proposition 9. The following statements hold.
(a) There exists a unique family $\mathbf{r c}^{1}$ of collinear central configurations emanating from the collision collinear central configuration with $m=$ $0, x_{3}=x_{4}=0$ and $y_{3}=y_{4}=0$. This family satisfies that $x_{4}=-x_{3}$ and it given by (19).
(b) There exists a unique family $\mathbf{r c}^{2}$ of collinear central configurations emanating from the collinear collision central configuration with $m=$ $0, x_{3}=x_{4}=\alpha$ and $y_{3}=y_{4}=0$. This family is given by (20).
5.4. Numerical study of the families of central configurations with $y_{3}=y_{4}=$ 0
We have followed the families of central configurations $\mathbf{r}^{1}, \mathbf{r}^{2}, \mathbf{r c}^{1}$ and $\mathbf{r c}^{2}$ given by Propositions 8 and 9 respectively from $m=0$ to $m=1$. The results that we have obtained are plotted in Figure 7.

We have computed the solutions of system (15) when $m=1$ and we have found exactly four real solutions satisfying $x_{3} \geqslant 0$ and $x_{3} \geqslant x_{4}$,
(i) the solution $\left(x_{3}, y_{3}\right)=(2.03895 \ldots, 0.0389514 \ldots)$ which belongs to the family $\mathbf{r}^{1}$,

The graphs of the functions $x_{3}(m)$ (continuous line) and $x_{4}(m)$ (dashed line), for $m \in(0,1]$, on the families of collinear central configurations given by Propositions 8 and 9.

(ii) the solution $\left(x_{3}, y_{3}\right)=(3.16212 \ldots,-3.16212 \ldots)$ which belongs to the family $\mathbf{r}^{2}$,
(iii) the solution $\left(x_{3}, y_{3}\right)=(0.316243 \ldots,-0.316243 \ldots)$ which belongs to the family $\mathbf{r c}^{1}$,
(iv) the solution $\left(x_{3}, y_{3}\right)=(4.85003 \ldots, 2.85003 \ldots)$ which belongs to the family $\mathbf{r c}^{2}$.

# 6. Central configurations for $m>0$ sufficiently small emanating from non-collision central configurations for $m=0$ 

Let $\mathbf{s}=\left(x_{3}, y_{3}, x_{4}, y_{4}\right)$, and let $\mathbf{s}_{1}, \mathbf{s}_{2}, \mathbf{s}_{3}, \mathbf{s}_{4}$, and $\mathbf{s}_{5}$ be the solutions of (6) for $m=0$ given by Theorem 2(a).

System (5) is analytic with respect to all its variables except at the points $\mathbf{s}$ corresponding to binary collisions between the masses. Therefore it is analytic in a neighborhood of the solutions $\mathbf{s}_{1}, \mathbf{s}_{2}, \mathbf{s}_{3}, \mathbf{s}_{4}$, and $\mathbf{s}_{5}$.

Let

$$
D=\left|\begin{array}{llll}
\frac{\partial F_{1}}{\partial x_{3}} & \frac{\partial F_{1}}{\partial y_{3}} & \frac{\partial F_{1}}{\partial x_{4}} & \frac{\partial F_{1}}{\partial y_{4}} \\
\frac{\partial F_{2}}{\partial x_{3}} & \frac{\partial F_{2}}{\partial y_{3}} & \frac{\partial F_{2}}{\partial x_{4}} & \frac{\partial F_{2}}{\partial y_{4}} \\
\frac{\partial F_{4}}{\partial x_{3}} & \frac{\partial F_{4}}{\partial y_{3}} & \frac{\partial F_{4}}{\partial x_{4}} & \frac{\partial F_{4}}{\partial y_{4}} \\
\frac{\partial F_{5}}{\partial x_{3}} & \frac{\partial F_{5}}{\partial y_{3}} & \frac{\partial F_{5}}{\partial x_{4}} & \frac{\partial F_{5}}{\partial y_{4}}
\end{array}\right|
$$

Let

$$
A=\frac{1}{(\alpha+1)^{3}}+\frac{1}{(\alpha-1)^{3}}
$$

It is not difficult to check that

$$
\begin{aligned}
& \left.D\right|_{m=0, \mathbf{s}=\mathbf{s}_{1}}=\frac{3213}{4096} \neq 0, \\
& \left.D\right|_{m=0, \mathbf{s}=\mathbf{s}_{2}}=-\frac{729}{65536} \neq 0, \\
& \left.D\right|_{m=0, \mathbf{s}=\mathbf{s}_{3}}=\frac{119}{16}\left(\frac{1}{4}+2 A\right)\left(\frac{1}{4}-A\right)=-1.09641 \cdots \neq 0, \\
& \left.D\right|_{m=0, \mathbf{s}=\mathbf{s}_{4}}=-\left(\frac{1}{4}-A\right)^{2}\left(\frac{1}{4}+2 A\right)^{2}=-0.0217317 \cdots \neq 0, \\
& \left.D\right|_{m=0, \mathbf{s}=\mathbf{s}_{5}}=-\frac{27}{256}\left(\frac{1}{4}+2 A\right)\left(\frac{1}{4}-A\right)=0.0155478 \cdots \neq 0 .
\end{aligned}
$$

Therefore from the Implicit Function Theorem we can find unique analytic functions $x_{3}^{i}(m), y_{3}^{i}(m), x_{4}^{i}(m)$, and $y_{4}^{i}(m)$ satisfying system $F_{1}=0, F_{2}=0$, $F_{4}=0$ and $F_{5}=0$ and $\left(x_{3}^{i}(0), y_{3}^{i}(0), x_{4}^{i}(0), y_{4}^{i}(0)\right)=\mathbf{s}_{i}$ for $i=1, \ldots, 5$ which are defined in a sufficiently small neighborhood $U$ of $m=0$.

Xia in  proves that for each $i=1, \ldots, 5$ the central configuration $\mathbf{s}_{i}$ can be continued to a family of central configurations with $m>0$ small. Therefore the solution $\mathbf{s}^{i}(m)=\left(x_{3}^{i}(m), y_{3}^{i}(m), x_{4}^{i}(m), y_{4}^{i}(m)\right)$ of system $F_{1}=$ $0, F_{2}=0, F_{4}=0$ and $F_{5}=0$ provides a family of central configurations for $m>0$ small and consequently it satisfies also equation $F_{3}=0$. Here we shall give the analytical expression of the families of central configurations given by the solutions $\mathbf{s}^{i}(m)=\left(x_{3}^{i}(m), y_{3}^{i}(m), x_{4}^{i}(m), y_{4}^{i}(m)\right)$.

By uniqueness, the family of central configurations given by the solution $\mathbf{s}^{i}(m)=\left(x_{3}^{i}(m), y_{3}^{i}(m), x_{4}^{i}(m), y_{4}^{i}(m)\right)$ with $i=1$ coincides with the family given by Proposition 5(a), the one with $i=2$ coincides with the one given by Proposition 5(b), the one with $i=3$ coincides with the one given by Proposition 8(a), and the one with $i=4$ coincides with the one given by Proposition 8(b). This proves statements (b), (c), (d) and (e) of Theorem 2.

Next we analyze the family of central configurations given by the solution $\mathbf{s}^{5}(m)$ by finding the analytic expression of the functions $x_{3}^{5}(m), y_{3}^{5}(m)$, $x_{4}^{5}(m)$ and $y_{4}^{5}(m)$ as in Section 4.2. Let

$$
\begin{aligned}
& x_{3}^{5}(m)=\sum_{k=0}^{\infty} x_{3 k}^{5} m^{k}, \quad x_{4}^{5}(m)=\sum_{k=0}^{\infty} x_{4 k}^{5} m^{k} \\
& y_{3}^{5}(m)=\sum_{k=0}^{\infty} y_{3 k}^{5} m^{k}, \quad y_{4}^{5}(m)=\sum_{k=0}^{\infty} y_{4 k}^{5} m^{k}
\end{aligned}
$$

where $\left(x_{30}^{5}, y_{30}^{5}, x_{40}^{5}, y_{40}^{5}\right)=\mathbf{s}_{5}$. We expand the functions $F_{1}, F_{2}, F_{4}$ and $F_{5}$ evaluated at $\mathbf{s}=\mathbf{s}^{5}(m)$ in power series of $m$. By computing the first terms of these power series expansions and equating them to zero we get

$$
\begin{aligned}
x_{3}^{5}(m) & =\frac{16}{3}\left(\frac{\alpha^{2}+1}{\left(\alpha^{2}-1\right)^{2}}-\frac{\alpha}{\left(\alpha^{2}+3\right)^{3 / 2}}\right) m+O\left(m^{2}\right) \\
& =1.10354 \ldots m+O\left(m^{2}\right)
\end{aligned}
$$

The graph of the points $\left(x_{3}^{5}(m), y_{3}^{5}(m)\right.$ ) (continuous line) and the points $\left(x_{4}^{5}(m), y_{4}^{5}(m)\right.$ ) (dashed line), for $m \in(0,1]$, on the family of solutions $\mathbf{s}^{5}(m)$.

$$
\begin{aligned}
y_{3}^{5}(m) & =\sqrt{3}+\frac{16}{3 \sqrt{3}}\left(\frac{2 \alpha}{\left(\alpha^{2}-1\right)^{2}}+\frac{1}{\left(\alpha^{2}+3\right)^{3 / 2}}\right) m+O\left(m^{2}\right) \\
& =1.73205 \cdots+0.774741 \ldots m+O\left(m^{2}\right) \\
x_{4}^{5}(m) & =\alpha+\frac{\frac{\alpha}{\left(\alpha^{2}+3\right)^{3 / 2}}-\frac{\alpha}{8}+\frac{3 \alpha^{2}+1}{\left(\alpha^{2}-1\right)^{2}}}{\frac{4 \alpha\left(\alpha^{2}+3\right)}{\left(\alpha^{2}-1\right)^{3}}+\frac{1}{4}} m+O\left(m^{2}\right) \\
& =2.39681 \cdots+0.582716 \ldots m+O\left(m^{2}\right) \\
y_{4}^{5}(m) & =-\frac{\sqrt{3}\left(\frac{1}{8}-\frac{1}{\left(\alpha^{2}+3\right)^{3 / 2}}\right)}{\frac{2 \alpha\left(\alpha^{2}+3\right)}{\left(\alpha^{2}-1\right)^{3}}-\frac{1}{4}} m+O\left(m^{2}\right)=-1.04970 \ldots m+O\left(m^{2}\right)
\end{aligned}
$$

This completes the proof of statement (f) of Theorem 2.

# 6.1. Numerical study of the family of central configurations $\mathbf{s}^{5}(m)$ 

We have followed numerically the family of non-symmetric central configurations $\mathbf{s}^{5}(m)$ from $m=0$ to $m=1$. The solutions that we have obtained are plotted in Figure 8.

We note that when $m=1$ the configuration $\mathbf{s}^{5}$ is given by $\left(x_{3}, y_{3}\right)=$ $(1.81097 \ldots, 1.82819 \ldots)$ and $\left(x_{4}, y_{4}\right)=(2.06662 \ldots,-1.64001 \ldots)$, and it becomes an isosceles triangle with the masses $m_{2}$ and $m_{4}$ on its axis of symmetry.

## 7. Central configurations for $m>0$ sufficiently small emanating from collision central configurations for $m=0$

System (5) is not defined when $\left(x_{3}, y_{3}\right)=\left(x_{4}, y_{4}\right)$. Inspired in the work of Xia , we transform system (5) into a new system that is well defined,

and in fact analytic, in a neighborhood of $\left(x_{3}, y_{3}\right)=\left(x_{4}, y_{4}\right)$ in the following way. First we consider the system of equations

$$
\begin{array}{lll}
G_{1}=F_{1}+F_{2}=0, & G_{2}=F_{4}+F_{5}=0, & G_{3}=F_{3} \\
G_{4}=F_{2}-F_{1}=0, & G_{5}=F_{5}-F_{4}=0 &
\end{array}
$$

which is equivalent to system (5). It is easy to see that the first three equations of (21) are analytic with respect to all its variables in a neighborhood of $\left(x_{3}, y_{3}\right)=\left(x_{4}, y_{4}\right)$ and $m=0$. The last two equations of (21) are not analytic at these points because they contain the term

$$
\frac{m}{r_{34}^{3}}=\frac{m}{\left(\left(x_{3}-x_{4}\right)^{2}+\left(y_{3}-y_{4}\right)^{2}\right)^{3 / 2}}
$$

This term is well defined when $m \rightarrow 0$ if $\left(x_{3}, y_{3}\right)-\left(x_{4}, y_{4}\right)=O\left(m^{\beta}\right)$ with $\beta \leqslant 1 / 3$. Let $\mu=m^{1 / 3}$, then by doing the the change of variables defined by $\left(x_{4}, y_{4}\right)=\left(x_{3}, y_{3}\right)+\mu\left(X_{4}, Y_{4}\right)$, we obtain a new system of equations which is analytic in a neighborhood of the point $\left(x_{3}, y_{3}\right), \mu=0$ and $\left(X_{4}, Y_{4}\right) \neq 0$ where

$$
\begin{aligned}
G_{1}= & \frac{2\left(x_{3}-1\right)}{r_{23}^{3}}+\frac{2\left(x_{3}+1\right)}{r_{13}^{3}}-\frac{x_{3}}{2}+O(\mu) \\
G_{2}= & \frac{2 y_{3}}{r_{23}^{2}}+\frac{2 y_{3}}{r_{13}^{3}}-\frac{y_{3}}{2}+O(\mu) \\
G_{3}= & 2 y_{3}\left(\frac{1}{r_{23}^{3}}-\frac{1}{r_{13}^{3}}\right) \mu^{3}+O\left(\mu^{4}\right) \\
G_{4}= & \left(\frac{2 X_{4}}{\left(X_{4}^{2}+Y_{4}^{2}\right)^{3 / 2}}+\frac{X_{4}\left(-2 x_{3}^{2}+4 x_{3}+y_{3}^{2}-2\right)-3\left(x_{3}-1\right) y_{3} Y_{4}}{r_{23}^{5}}\right. \\
& \left.+\frac{X_{4}\left(-2 x_{3}^{2}-4 x_{3}+y_{3}^{2}-2\right)-3\left(x_{3}+1\right) y_{3} Y_{4}}{r_{13}^{5}}-\frac{X_{4}}{4}\right) \mu+O\left(\mu^{2}\right) \\
G_{5}= & \left(\frac{2 Y_{4}}{\left(X_{4}^{2}+Y_{4}^{2}\right)^{3 / 2}}+\frac{Y_{4}\left(x_{3}^{2}-2 x_{3}-2 y_{3}^{2}+1\right)-3\left(x_{3}-1\right) X_{4} y_{3}}{r_{23}^{5}}\right. \\
& \left.+\frac{Y_{4}\left(x_{3}^{2}+2 x_{3}-2 y_{3}^{2}+1\right)-3\left(x_{3}+1\right) X_{4} y_{3}}{r_{13}^{5}}-\frac{Y_{4}}{4}\right) \mu+O\left(\mu^{2}\right)
\end{aligned}
$$

Consider now the system of equations

$$
\begin{array}{lll}
\bar{G}_{1}=G_{1}=0, & \bar{G}_{2}=G_{2}=0, & \bar{G}_{3}=G_{3} / \mu^{3}=0 \\
\bar{G}_{4}=G_{4} / \mu=0, & \bar{G}_{5}=G_{5} / \mu=0, &
\end{array}
$$

which is also analytic with respect to all its variables in a neighborhood of $\left(x_{3}, y_{3}\right), \mu=0$ and $\left(X_{4}, Y_{4}\right) \neq 0$.

First we compute the solutions of (22) with $\mu=0$. When $\mu=0$ the third equation of (22) is always satisfied and the first two equations of (22) become $G\left(x_{3}, y_{3}\right)=0$ and $H\left(x_{3}, y_{3}\right)=0$ (see (7)). Therefore the solutions of $\bar{G}_{1}=0, \bar{G}_{2}=0$ and $G_{3}=0$ with $x_{3}, y_{3} \geqslant 0$ are $\left(x_{3}, y_{3}\right)=(0,0),\left(x_{3}, y_{3}\right)=$ $(0, \sqrt{3})$ and $\left(x_{3}, y_{3}\right)=(\alpha, 0)$. We substitute these solutions into the last two equations of (22), then by solving the resultant system of equations we get that when $\mu=0$ system (22) has 8 different real solutions with $x_{3}, y_{3} \geqslant 0$, they are given by

$$
\begin{array}{ll}
\mathbf{s c}_{11}=\left(0,0, \frac{2}{17^{1 / 3}}, 0\right), & \mathbf{s c}_{12}=\left(0,0,-\frac{2}{17^{1 / 3}}, 0\right) \\
\mathbf{s c}_{21}=\left(0, \sqrt{3}, \frac{2^{5 / 3}}{3^{1 / 3}}, 0\right), & \mathbf{s c}_{22}=\left(0, \sqrt{3},-\frac{2^{5 / 3}}{3^{1 / 3}}, 0\right) \\
\mathbf{s c}_{23}=\left(0, \sqrt{3}, 0, \frac{2^{5 / 3}}{3^{2 / 3}}\right), & \mathbf{s c}_{24}=\left(0, \sqrt{3}, 0,-\frac{2^{5 / 3}}{3^{2 / 3}}\right) \\
\mathbf{s c}_{31}=(\alpha, 0, \bar{X}, 0), & \mathbf{s c}_{32}=(\alpha, 0,-\bar{X}, 0)
\end{array}
$$

where

$$
\bar{X}=\frac{2\left(\alpha^{2}-1\right)}{\sqrt{\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1}}=1.245598 \ldots
$$

Here the components of $\mathbf{s c}_{i j}$ are $\left(x_{3}, y_{3}, X_{4}, Y_{4}\right)$. We note that system (22) has no solutions with $\left(X_{4}, Y_{4}\right) \rightarrow(0,0)$ as $\mu \rightarrow 0$, because either $\bar{G}_{4}$ or $\bar{G}_{5}$ tend to $\pm \infty$ when $\mu \rightarrow 0$ and $\left(x_{3}, y_{3}\right)=(0,0),\left(x_{3}, y_{3}\right)=(0, \sqrt{3})$ or $\left(x_{3}, y_{3}\right)=(\alpha, 0)$.

Next we continue the solutions of system (22) with $\mu=0$ to $\mu>0$ small by applying the Implicit Function Theorem as in Section 6. Clearly system (22) is analytic with respect to all its variables in a neighborhood of the points $\mathbf{s c}_{1 j}, \mathbf{s c}_{2 j}, \mathbf{s c}_{2 k}$ and $\mathbf{s c}_{3 j}$ with $j=1,2$, and $k=3,4$.

Let

$$
\bar{D}=\left|\begin{array}{llll}
\frac{\partial \bar{G}_{1}}{\partial x_{3}} & \frac{\partial \bar{G}_{1}}{\partial y_{3}} & \frac{\partial \bar{G}_{1}}{\partial X_{4}} & \frac{\partial \bar{G}_{1}}{\partial Y_{4}} \\
\frac{\partial \bar{G}_{2}}{\partial x_{3}} & \frac{\partial \bar{G}_{2}}{\partial y_{3}} & \frac{\partial \bar{G}_{2}}{\partial X_{4}} & \frac{\partial \bar{G}_{2}}{\partial Y_{4}} \\
\frac{\partial \bar{G}_{4}}{\partial x_{3}} & \frac{\partial \bar{G}_{4}}{\partial y_{3}} & \frac{\partial \bar{G}_{4}}{\partial X_{4}} & \frac{\partial \bar{G}_{4}}{\partial Y_{4}} \\
\frac{\partial \bar{G}_{5}}{\partial x_{3}} & \frac{\partial \bar{G}_{5}}{\partial y_{3}} & \frac{\partial \bar{G}_{5}}{\partial X_{4}} & \frac{\partial \bar{G}_{5}}{\partial Y_{4}}
\end{array}\right|
$$

and let $\overline{\mathbf{s}}=\left(x_{3}, y_{3}, X_{4}, Y_{4}\right)$. It is not difficult to check that

$$
\begin{aligned}
\left.\bar{D}\right|_{\mu=0, \overline{\mathbf{s}}=\mathbf{s c}_{1 j}}= & \frac{18207}{8} \neq 0 \\
\left.\bar{D}\right|_{\mu=0, \overline{\mathbf{s}}=\mathbf{s c}_{2 j}}= & \frac{729}{8192} \neq 0 \\
\left.\bar{D}\right|_{\mu=0, \overline{\mathbf{s}}=\mathbf{s c}_{2 k}}= & -\frac{2187}{8192} \neq 0 \\
\left.\bar{D}\right|_{\mu=0, \overline{\mathbf{s}}=\mathbf{s c}_{3 j}}= & -\frac{9 \alpha\left(\alpha^{2}+3\right)}{8\left(\alpha^{2}-1\right)^{12}}\left(\alpha^{6}-3 \alpha^{4}-8 \alpha^{3}+3 \alpha^{2}-24 \alpha-1\right) \\
& \left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)^{2}=2.15539 \cdots \neq 0
\end{aligned}
$$

for all $j=1,2$ and $k=3,4$. Therefore from the Implicit Function Theorem we can find unique analytic functions $x_{3}^{i}(\mu), y_{3}^{i}(\mu), X_{4}^{i}(\mu)$, and $Y_{4}^{i}(\mu)$, defined in a sufficiently small neighborhood $U$ of $\mu=0$, satisfying system $\bar{G}_{1}=0$, $\bar{G}_{2}=0, \bar{G}_{4}=0$ and $\bar{G}_{5}=0$ and such that $\left(x_{3}^{i}(0), y_{3}^{i}(0), X_{4}^{i}(0), Y_{4}^{i}(0)\right)=\mathbf{s c}_{i j}$ for all $j=1,2$ when $i=1,3$; and $j=1, \ldots, 4$ when $i=2$. Next we will give the analytical expression of these functions.

Let $\overline{\mathbf{s}}=\overline{\mathbf{s}}(\mu)=\left(x_{3}(\mu), y_{3}(\mu), X_{4}(\mu), Y_{4}(\mu)\right)$ be the solutions of system $\bar{G}_{1}=0, \bar{G}_{2}=0, \bar{G}_{4}=0$ and $\bar{G}_{5}=0$ with

$$
\begin{aligned}
& x_{3}(\mu)=\sum_{k=0}^{\infty} x_{3 k} \mu^{k}, \quad X_{4}(\mu)=\sum_{k=0}^{\infty} X_{4 k} \mu^{k} \\
& y_{3}(\mu)=\sum_{k=0}^{\infty} y_{3 k} \mu^{k}, \quad Y_{4}(\mu)=\sum_{k=0}^{\infty} y_{4 k} \mu^{k}
\end{aligned}
$$

We expand the functions $\bar{G}_{1}, \bar{G}_{2}, \bar{G}_{4}$ and $\bar{G}_{5}$ evaluated at $\overline{\mathbf{s}}=\overline{\mathbf{s}}(\mu)$ with $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{i j}$ for $j=1,2$ when $i=1,3$; and $j=1, \ldots, 4$ when $i=2$. By computing the first terms of these power series expansions and equating them to zero we get the following.

If $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{11}$, then

$$
\begin{array}{ll}
x_{3}(\mu)=-\frac{\mu}{\sqrt{17}}+\frac{32 \mu^{3}}{867}+O\left(\mu^{4}\right), & y_{3}(\mu)=0+O\left(\mu^{4}\right) \\
X_{4}(\mu)=\frac{2}{\sqrt{17}}-\frac{64 \mu^{2}}{867}-\frac{16 \mu^{3}}{51 \sqrt{17}}+O\left(\mu^{4}\right), & Y_{4}(\mu)=0+O\left(\mu^{4}\right)
\end{array}
$$

This solution does not provide solutions of (5) with $x_{3}, y_{3} \geqslant 0$.

If $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{12}$, then

$$
\begin{array}{ll}
x_{3}(\mu)=\frac{\mu}{\sqrt{17}}-\frac{32 \mu^{3}}{867}+O\left(\mu^{4}\right), & y_{3}(\mu)=0+O\left(\mu^{4}\right) \\
X_{4}(\mu)=-\frac{2}{\sqrt{17}}+\frac{64 \mu^{2}}{867}+\frac{16 \mu^{3}}{51 \sqrt{17}}+O\left(\mu^{4}\right), & Y_{4}(\mu)=0+O\left(\mu^{4}\right)
\end{array}
$$

We undo the change of variables $\left(x_{4}, y_{4}\right)=\left(x_{3}, y_{3}\right)+\mu\left(X_{4}, Y_{4}\right)$ and we have

$$
\begin{array}{ll}
x_{3}(\mu)=\frac{1}{17^{1 / 3}} \mu-\frac{32}{867} \mu^{3}+O\left(\mu^{4}\right), & y_{3}(\mu)=0+O\left(\mu^{4}\right) \\
x_{4}(\mu)=-\frac{1}{17^{1 / 3}} \mu+\frac{32}{867} \mu^{3}+O\left(\mu^{4}\right), & y_{4}(\mu)=0+O\left(\mu^{4}\right)
\end{array}
$$

By observing the first terms of these power series expansions we see that this solution must provide the family of collinear central configurations given by Proposition 9(a). This proves statement (g) of Theorem 2.

If $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{21}$, then

$$
\begin{array}{ll}
x_{3}(\mu)=-\frac{2^{2 / 3} \mu}{3^{1 / 3}}-\frac{5 \mu^{3}}{27}+O\left(\mu^{4}\right), & y_{3}(\mu)=\sqrt{3}+\frac{\mu^{2}}{2^{5 / 3} 3^{7 / 6}}+O\left(\mu^{4}\right) \\
X_{4}(\mu)=\frac{2^{5 / 3}}{3^{1 / 3}}+\frac{10 \mu^{2}}{27}-\frac{2^{11 / 3} \mu^{3}}{3^{7 / 3}}+O\left(\mu^{4}\right), & Y_{4}(\mu)=0+O\left(\mu^{4}\right)
\end{array}
$$

This solution does not provide solutions of (5) with $x_{3}, y_{3} \geqslant 0$.
If $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{22}$, then

$$
\begin{array}{ll}
x_{3}(\mu)=\frac{2^{2 / 3} \mu}{3^{1 / 3}}+\frac{5 \mu^{3}}{27}+O\left(\mu^{4}\right), & y_{3}(\mu)=\sqrt{3}+\frac{\mu^{2}}{2^{5 / 3} 3^{7 / 6}}+O\left(\mu^{4}\right) \\
X_{4}(\mu)=-\frac{2^{5 / 3}}{3^{1 / 3}}-\frac{10 \mu^{2}}{27}+\frac{2^{11 / 3} \mu^{3}}{3^{7 / 3}}+O\left(\mu^{4}\right), & Y_{4}(\mu)=0+O\left(\mu^{4}\right)
\end{array}
$$

By undoing the change of variables $\left(x_{4}, y_{4}\right)=\left(x_{3}, y_{3}\right)+\mu\left(X_{4}, Y_{4}\right)$ we have

$$
\begin{array}{ll}
x_{3}(\mu)=\frac{2^{2 / 3}}{3^{1 / 3}} \mu+\frac{5}{27} \mu^{3}+O\left(\mu^{4}\right), & y_{3}(\mu)=\sqrt{3}+\frac{1}{2^{5 / 3} 3^{7 / 6}} \mu^{2}+O\left(\mu^{4}\right) \\
x_{4}(\mu)=-\frac{2^{2 / 3}}{3^{1 / 3}} \mu-\frac{5}{27} \mu^{3}+O\left(\mu^{4}\right), & y_{4}(\mu)=\sqrt{3}+\frac{1}{2^{5 / 3} 3^{7 / 6}} \mu^{2}+O\left(\mu^{4}\right)
\end{array}
$$

From the first terms of these power series expansions it seems that the solution $\mathbf{s}(\mu)$ satisfies that $x_{4}=-x_{3}$ and $y_{4}=y_{3}$, so it could be an isosceles trapezoid. From  we know the existence of a unique family of isosceles

trapezoid central configurations defined for all $m>0$ that tends to the equilateral triangle central configuration $\mathbf{s c}_{2}$ when $m \rightarrow 0$. Therefore the family of solutions $\mathbf{s}(\mu)$ must provide the family of isosceles trapezoid central configurations. This proves statement (h.2) of Theorem 2.

By proceeding in a similar way we see that the family of solutions of $\bar{G}_{1}=0, \bar{G}_{2}=0, \bar{G}_{4}=0$ and $\bar{G}_{5}=0$ with $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{23}$ provides a family of solutions of (5) with

$$
\begin{array}{ll}
x_{3}(\mu)=0+O\left(\mu^{4}\right), & y_{3}(\mu)=\sqrt{3}+\frac{2^{2 / 3}}{3^{2 / 3}} \mu+\frac{1}{12^{5 / 6}} \mu^{2}+\frac{1}{81} \mu^{3}+O\left(\mu^{4}\right) \\
x_{4}(\mu)=0+O\left(\mu^{4}\right), & y_{4}(\mu)=\sqrt{3}-\frac{2^{2 / 3}}{3^{2 / 3}} \mu+\frac{1}{12^{5 / 6}} \mu^{2}-\frac{1}{81} \mu^{3}+O\left(\mu^{4}\right)
\end{array}
$$

This family must be the family of kite central configurations given by Proposition 6(b). This proves statement (h.1) of Theorem 2.

Since without loss of generality we can assume that $y_{3} \geqslant y_{4}$, we can check that the family of solutions of $\bar{G}_{1}=0, \bar{G}_{2}=0, \bar{G}_{4}=0$ and $\bar{G}_{5}=0$ with $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{24}$ does not provide solutions of (5) with $x_{3}, y_{3} \geqslant 0$ and $y_{3} \geqslant y_{4}$.

Without loss of generality we also can assume that $x_{3} \geqslant x_{4}$. Then we can see that the family of solutions of $\bar{G}_{1}=0, \bar{G}_{2}=0, \bar{G}_{4}=0$ and $\bar{G}_{5}=0$ with $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{31}$ does not provide a family of solutions of (5) with $x_{3}, x_{4} \geqslant 0$ and $x_{3} \geqslant x_{4}$.

The family of solutions of $\bar{G}_{1}=0, \bar{G}_{2}=0, \bar{G}_{4}=0$ and $\bar{G}_{5}=0$ with $\left(x_{30}, y_{30}, X_{40}, Y_{40}\right)=\mathbf{s c}_{32}$ provides the family of solutions of (5) given by

$$
\begin{array}{ll}
x_{3}(\mu)=\alpha+\overline{x_{31}} \mu+\overline{x_{32}} \mu^{2}+\overline{x_{33}} \mu^{3}+O\left(\mu^{4}\right), & y_{3}(\mu)=O\left(\mu^{4}\right) \\
x_{4}(\mu)=\alpha-\overline{x_{31}} \mu+\overline{x_{32}} \mu^{2}+\overline{x_{43}} \mu^{3}+O\left(\mu^{4}\right), & y_{4}(\mu)=O\left(\mu^{4}\right)
\end{array}
$$

where $\overline{x_{31}}=\bar{X} / 2=0.622799 \ldots$, (see the definition of $\mathbf{s c}_{32}$ ) and

$$
\begin{aligned}
\overline{x_{32}}= & \frac{24\left(\alpha^{6}+5 \alpha^{4}-5 \alpha^{2}-1\right)}{\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1\right)^{5 / 3}}=0.303818 \ldots \\
\overline{x_{33}}= & \frac{8}{3}\left(9 \alpha^{16}-60 \alpha^{14}+284 \alpha^{13}+168 \alpha^{12}-216 \alpha^{11}+2132 \alpha^{10}-\right. \\
& 1708 \alpha^{9}+13314 \alpha^{8}+3312 \alpha^{7}+13004 \alpha^{6}-1788 \alpha^{5}- \\
& \left.20896 \alpha^{4}-152 \alpha^{3}-7524 \alpha^{2}+268 \alpha-147\right) /\left(\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+\right. \\
& \left.3 \alpha^{2}+48 \alpha-1\right)^{3}=1.60489 \ldots
\end{aligned}
$$

and

$$
\overline{x_{43}}=-\overline{x_{33}}+\frac{16\left(3 \alpha^{4}-2 \alpha^{2}-1\right)}{\alpha^{6}-3 \alpha^{4}+16 \alpha^{3}+3 \alpha^{2}+48 \alpha-1}=1.52572 \ldots
$$

The graph of the points $\left(x_{3}(m), y_{3}(m)\right)$ for $m \in(0,1]$ on the family of solutions of (5) with $x_{4}=-x_{3}$ and $y_{4}=y_{3} \neq 0$.

We note that these solutions must provide the family of collinear central configurations given by Proposition 9(b). This proves statement (i) of Theorem 2 .

# 7.1. Numerical study of the family of isosceles trapezoid central configurations 

We have followed numerically the family of isosceles trapezoid central configurations from $m=0$ to $m=1$, the solutions that we have obtained are plotted in Figure 9. We note that if $m \rightarrow 0$, then $\left(x_{3}, y_{3}\right) \rightarrow(0, \sqrt{3})$, and if $m=1$ then the configurations tends to the square with $\left(x_{3}, y_{3}\right) \rightarrow(1,2)$.

## 8. Central configurations for $m>0$ sufficiently small that do not emanate from central configurations with $m=0$

The families of solutions of system (5) for $m>0$ small can come either from the solutions for $m=0$, from the singularities of the equations (5) (which correspond to collision between the masses), or from infinity.

Up to here we have found all the families of non-equivalent central configurations of the planar four-body problem emanating from central configurations with $m=0$. In this section we prove that there are no families of central configurations for $m>0$ sufficiently small with one of the small masses near collision with either $m_{1}$ and $m_{2}$, and that there are no families of central configurations with one of the masses coming from infinity. This proves statement (j) of Theorem 2.

### 8.1. Central configurations for $m>0$ sufficiently small with one small mass near collision with either $m_{1}$ and $m_{2}$

Without loss of generality we can assume that $m_{3}$ tends to collision with $m_{2}$ when $m \rightarrow 0$.

Lemma 10. Let

$$
h_{1}(x, y)=\frac{x}{\left(x^{2}+y^{2}\right)^{3 / 2}}, \quad h_{2}(x, y)=\frac{y}{\left(x^{2}+y^{2}\right)^{3 / 2}}
$$

We introduce polar coordinates $x=r \cos \theta$ and $y=r \sin \theta$. If $\gamma_{\theta_{0}}$ denotes an arbitrary path that approaches the origin along the direction of the ray $\theta=\theta_{0}$; i.e. $\theta \rightarrow \theta_{0}$ when $r \rightarrow 0$ along the path, then the following statements hold.
(a) The values of $\lim _{(x, y) \rightarrow(0,0)} h_{1}(x, y)$ and $\lim _{(x, y) \rightarrow(0,0)} h_{2}(x, y)$ along the path $\gamma_{\theta_{0}}$ depend on the values of $\theta_{0}$ and they are summarized in Table 1.
(b) If $\theta_{0} \neq \pm \pi / 2$, then $\lim _{(x, y) \rightarrow(0,0),(x, y) \in \gamma_{\theta_{0}}} h_{1}(x, y)$ is infinity of order $1 / r^{2}$ when $r \rightarrow 0$; i.e. $\lim _{r \rightarrow 0^{+}} r^{2} h_{1}\left(r \cos \theta_{0}, r \sin \theta_{0}\right)=\ell$ with $\ell \neq 0$ and $\ell \neq \infty$.
(c) If $\theta_{0} \neq 0, \pi$, then $\lim _{(x, y) \rightarrow(0,0),(x, y) \in \gamma_{\theta_{0}}} h_{2}(x, y)$ is infinity of order $1 / r^{2}$ when $r \rightarrow 0$; i.e. $\lim _{r \rightarrow 0^{+}} r^{2} h_{2}\left(r \cos \theta_{0}, r \sin \theta_{0}\right)=\ell$ with $\ell \neq 0$ and $\ell \neq \infty$.

Proof. The proof is an immediate consequence of the fact that the expressions of $h_{1}$ and $h_{2}$ in polar coordinates are

$$
h_{1}(r \cos \theta, r \sin \theta)=\frac{\cos \theta}{r^{2}}, \quad h_{2}(r \cos \theta, r \sin \theta)=\frac{\sin \theta}{r^{2}}
$$

Indeed, if $\cos \theta \neq 0$, then $\lim _{r \rightarrow 0^{+}} h_{1}(r \cos \theta, r \sin \theta)=\infty$. If $\theta= \pm \pi / 2$ is constant along the path, then $\lim _{r \rightarrow 0^{+}} h_{1}(r \cos \theta, r \sin \theta)=0$. And finally if $\theta \rightarrow \pm \pi / 2$ as $r \rightarrow 0$ but $\theta \neq \pm \pi / 2$ along the path, then the limit will depend on the path that we choose in order to approach the origin on the direction of the rays $\theta= \pm \pi / 2$. For instance, if we approach the origin along paths of the form $x=a y^{3}$ with $a \in \mathbb{R}$ arbitrary then

$$
\lim _{y \rightarrow 0} h_{1}\left(a y^{3}, y\right)=\lim _{y \rightarrow 0} \frac{a y^{3}}{\left(a^{2} y^{6}+y^{2}\right)^{3 / 2}}=a
$$

The limit $\lim _{(x, y) \rightarrow(0,0)} h_{2}(x, y)$ along the paths $\gamma_{\theta_{0}}$ depending on the values of $\theta_{0}$ can be analyzed in a similar way.

In what follows we use the notation $\lim _{(x, y) \rightarrow(0,0)} h(x, y)$ to denote the limit $\lim _{(x, y) \rightarrow(0,0)} h(x, y)$ along the path $\gamma_{\theta_{0}}$.

By applying the properties of limits and after some computations we get

$$
\begin{aligned}
\lim _{(x_{3}, y_{3}) \rightarrow(1,0)} F_{1}= & (1+m) \cdot \lim _{(x_{3}, y_{3}) \rightarrow(1,0)} \frac{x_{3}-1}{r_{23}^{3}}+m \cdot \lim _{(x_{3}, y_{3}) \rightarrow(1,0)} \frac{x_{3}-x_{4}}{r_{34}^{3}}+ \\
& m \cdot \frac{x_{4}-1}{r_{24}^{3}}-m \cdot \frac{x_{4}+1}{r_{14}^{3}} \cdot \lim _{x_{3} \rightarrow 1} \frac{x_{3}-1}{2}
\end{aligned}
$$

The limit $\lim _{(x_{3}, y_{3}) \rightarrow(1,0)}\left(x_{3}-1\right) / r_{23}^{3}$ depends on the path that we choose to approach the point $(1,0)$, see Lemma 10. We consider polar coordinates $x_{3}=1+r \cos \theta$ and $y_{3}=r \sin \theta$ and we denote by $\gamma_{\theta_{0}}$ an arbitrary path that approaches the point $\left(x_{3}, y_{3}\right)=(1,0)$ along the direction of the ray $\theta=\theta_{0}$, then

$$
L_{1}=\lim _{(x_{3}, y_{3}) \xrightarrow{\gamma_{\theta_{0}}}(1,0)} \frac{x_{3}-1}{\left(\left(x_{3}-1\right)^{2}+y_{3}^{2}\right)^{3 / 2}}= \begin{cases}\infty & \text { if } \theta_{0} \neq \pm \pi / 2 \\ 0 & \text { if } \theta= \pm \pi / 2 \\ a \in \mathbb{R} & \text { if } \theta \xrightarrow{r \rightarrow 0} \pm \pi / 2\end{cases}
$$

Since we only are interested in solutions with $x_{3}, y_{3} \geqslant 0$, we assume that $\theta \in[0, \pi / 2]$.

We note that the second, the third and the fourth summands in (23) could tend to infinity when $m_{4} \rightarrow m_{2}$ or $m_{4} \rightarrow m_{1}$ as $m \rightarrow 0$. So the limit of $F_{1}$ when $\left(x_{3}, y_{3}\right) \rightarrow(1,0)$ and $m \rightarrow 0$ depends on wether $m_{4} \rightarrow m_{2}$ as $m \rightarrow 0, m_{4} \rightarrow m_{1}$ as $m \rightarrow 0$, or $m_{4}$ is far from collision with $m_{1}$ and $m_{2}$ as $m \rightarrow 0$.

8.1.1. Case $m_{4}$ far from collision with either $m_{1}$ or $m_{2}$ when $m \rightarrow 0$.

From (23) and (24), if $m_{4}$ is far from collision with either $m_{1}$ or $m_{2}$ when $m \rightarrow 0$ then

$$
\lim _{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{\theta_{0}}} \underset{(1,0)}{(1,0)}} F_{1}=(1+m) L_{1}
$$

Since we need that $F_{1} \rightarrow 0$ as $\left(x_{3}, y_{3}\right) \rightarrow(1,0)$ and $m \rightarrow 0, \theta_{0}=\pi / 2$. On the other hand, if $m_{4}$ is far from collision with $m_{1}$ and $m_{2}$ when $m \rightarrow 0$, then it is easy to check that

$$
\lim _{\left(x_{3}, y_{3}\right) \rightarrow(1,0)} F_{4}=(1+m) \lim _{\left(x_{3}, y_{3}\right) \rightarrow(1,0)} \frac{y_{3}}{\left(\left(x_{3}-1\right)^{2}+y_{3}^{2}\right)^{3 / 2}}
$$

By Lemma 10 this limit becomes $\infty$ when we approach the point $\left(x_{3}, y_{3}\right)=$ $(1,0)$ along an arbitrary path $\gamma_{\theta_{0}}$ with $\theta_{0}=\pi / 2$. Therefore there are no solutions of (5) in this case.

# 8.1.2. Case $m_{4}$ tending to collision with $m_{1}$ when $m \rightarrow 0$. 

We define $L_{1}$ as in (24). We introduce polar coordinates $x_{4}=-1+$ $R \cos \varphi$ and $y_{4}=R \sin \varphi$ and we denote by $\gamma_{\varphi_{0}}$ an arbitrary path that approaches the point $\left(x_{4}, y_{4}\right)=(-1,0)$ along the direction of the ray $\varphi=\varphi_{0}$. Then we define

$$
\bar{L}_{2}=\lim _{\left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(-1,0)} \frac{x_{4}+1}{\left(\left(x_{4}+1\right)^{2}+y_{4}^{2}\right)^{3 / 2}}= \begin{cases}\infty & \text { if } \varphi_{0} \neq \pm \pi / 2 \\ 0 & \text { if } \varphi= \pm \pi / 2 \\ b \in \mathbb{R} & \text { if } \varphi \xrightarrow{r \rightarrow 0} \pm \pi / 2\end{cases}
$$

see Lemma 10. From (23), (24), and (25) we get

Next we analyze the values of (26) and the possible solutions of (5) depending on the values of $L_{1}$ and $\bar{L}_{2}$.

Case $L_{1}=\infty$ and $\bar{L}_{2}=\infty$. From Lemma 10, if $\theta_{0} \neq \pi / 2$ and $\varphi_{0} \neq$ $\pm \pi / 2$, then $L_{1}$ is infinity of order $1 / r^{2}$ as $r \rightarrow 0$ and $\bar{L}_{2}$ is infinity of order $1 / R^{2}$ as $R \rightarrow 0$. Moreover $\left(x_{3}-1\right)$ is an infinitesimal of order $r$ as $r \rightarrow 0$. Therefore if $F_{1} \rightarrow 0$, then the mass $m$ has order $R^{2} / r^{3}$ as $r, R \rightarrow 0$ (see (26)).

On the other hand, it is easy to see that

$$
\lim _{\substack{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{30}}(1,0) \\\left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{30}}(-1,0)}} F_{2}=(1+m) \cdot \bar{L}_{2}-m \cdot L_{1} \cdot \lim _{x_{4} \rightarrow-1} \frac{x_{4}+1}{2}
$$

In order that $F_{2} \rightarrow 0$ the mass $m$ must have order $r^{2} / R^{3}$ as $r, R \rightarrow 0$. Therefore $R^{2} / r^{3}$ and $r^{2} / R^{3}$ must have the same order as $r, R \rightarrow 0$. This implies that $R$ and $r$ have the same order which is not possible because $m \rightarrow 0$ as $r, R \rightarrow 0$. So there are no solutions of (5) in this case.

If either $\theta_{0}=\pi / 2$ or $\varphi_{0}= \pm \pi / 2$, then $L_{1}$ is infinity of order $1 / r^{\alpha}$ as $r \rightarrow 0$ and $\bar{L}_{2}$ is infinity of order $1 / r^{\beta}$ as $r \rightarrow 0$ for some $\alpha, \beta>0$. Moreover $\left(x_{4}+1\right)$ is an infinitesimal of order $r^{\gamma}$ as $r \rightarrow 0$ for some $\gamma>0$. Therefore if $F_{1} \rightarrow 0$, then the mass $m$ has order $r^{\beta-\alpha-1}$ as $r \rightarrow 0$ (see (26)). On the other hand, in order that $F_{2} \rightarrow 0$ the mass $m$ must have order $r^{\alpha-\beta-\gamma}$ as $r \rightarrow 0$ (see (27)). Therefore $\beta-\alpha-1=\alpha-\beta-\gamma$. This implies that $m$ has order $r^{-(\gamma+1) / 2}$ as $r \rightarrow 0$ which is impossible because $\gamma>0$ and $m \rightarrow 0$ as $r \rightarrow 0$. There are no solutions of (5) in this case.

Case $L_{1}=a \neq \infty$ and $\bar{L}_{2}=\infty$. There are no solutions of (5) when $L_{1}=a \neq \infty$ and $\bar{L}_{2}=\infty$ because $F_{2}$ tends to $\infty$ (see (27)).

Case $L_{1}=\infty$ and $\bar{L}_{2}=b \neq \infty$. In this case $F_{1}$ tends to $\infty$, so system (5) is not satisfied.

Case $L_{1}=a \neq \pm \infty$ and $\bar{L}_{2}=b \neq \pm \infty$. Under these assumptions $F_{1}$ tends to $a$, so $a$ must be zero (see (26)). This means that $\theta_{0}=\pi / 2$. It is easy to check that

$$
\lim _{\substack{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{30}}(1,0) \\\left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{30}}(-1,0)}} F_{4}=(1+m) \cdot L_{3}-m \cdot \bar{L}_{2} \cdot \lim _{y_{3} \rightarrow 0} \frac{y_{3}}{2}
$$

where

$$
L_{3}=\lim _{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{30}}(1,0)} \frac{y_{3}}{\left(\left(x_{3}-1\right)^{2}+y_{3}^{2}\right)^{3 / 2}}= \begin{cases}\infty & \text { if } \theta_{0} \neq 0, \pi \\ 0 & \text { if } \theta=0, \pi \\ c \in \mathbb{R} & \text { if } \theta \xrightarrow{r \rightarrow 0} 0, \pi\end{cases}
$$

see Lemma 10. Since $\theta_{0}=\pi / 2$ and $\bar{L}_{2}=b \neq \pm \infty, F_{4}$ tends to $\infty$. Therefore there are no solutions of (5) in this case.

8.1.3. Case $m_{4}$ tends to collision with $m_{2}$ when $m \rightarrow 0$.

We define $L_{1}$ and $L_{3}$ as in (24) and (28) respectively. We introduce polar coordinates $x_{4}=1+R \cos \varphi$ and $y_{4}=R \sin \varphi$ and we denote by $\gamma_{\varphi_{0}}$ an arbitrary path that approaches the point $\left(x_{4}, y_{4}\right)=(1,0)$ along the direction of the ray $\varphi=\varphi_{0}$. Then we define

$$
\begin{aligned}
& L_{2}=\lim _{\left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)} \frac{x_{4}-1}{\left(\left(x_{4}-1\right)^{2}+y_{4}^{2}\right)^{3 / 2}}= \begin{cases}\infty & \text { if } \varphi_{0} \neq \pm \pi / 2, \\
0 & \text { if } \varphi= \pm \pi / 2, \\
b \in \mathbb{R} & \text { if } \varphi \xrightarrow{r \rightarrow 0} \pm \pi / 2,\end{cases} \\
& L_{4}=\lim _{\left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)} \frac{y_{4}}{\left(\left(x_{4}-1\right)^{2}+y_{4}^{2}\right)^{3 / 2}}= \begin{cases}\infty & \text { if } \varphi_{0} \neq 0, \pi, \\
0 & \text { if } \varphi=0, \pi, \\
d \in \mathbb{R} & \text { if } \varphi \xrightarrow{r \rightarrow 0} 0, \pi,\end{cases}
\end{aligned}
$$

see Lemma 10. And we define

$$
\begin{aligned}
& H_{1}=\lim _{\substack{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0) \\
\left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)}} \bar{H}_{1}, \quad H_{2}=\lim _{\substack{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0) \\
\left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)}} \bar{H}_{2}, \\
& \text { where } \\
& \bar{H}_{1}=\frac{x_{3}-x_{4}}{\left(\left(x_{3}-x_{4}\right)^{2}+\left(y_{3}-y_{4}\right)^{2}\right)^{3 / 2}}=\frac{r \cos \theta-R \cos \varphi}{\left(r^{2}+R^{2}-2 r R \cos (\theta-\varphi)\right)^{3 / 2}} \\
& \bar{H}_{2}=\frac{y_{3}-y_{4}}{\left(\left(x_{3}-x_{4}\right)^{2}+\left(y_{3}-y_{4}\right)^{2}\right)^{3 / 2}}=\frac{r \sin \theta-R \sin \varphi}{\left(r^{2}+R^{2}-2 r R \cos (\theta-\varphi)\right)^{3 / 2}} .
\end{aligned}
$$

By applying the properties of limits and after some computations we get

$$
\begin{aligned}
& \lim _{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)} F_{1}=(1+m) \cdot L_{1}+m \cdot L_{2}+m \cdot H_{1}, \\
& \left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0) \\
& \lim _{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)} F_{2}=(1+m) \cdot L_{2}+m \cdot L_{1}-m \cdot H_{1}, \\
& \left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0) \\
& \lim _{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)} F_{4}=(1+m) \cdot L_{3}+m \cdot L_{2} \cdot \lim _{y_{3} \rightarrow 0} \frac{y_{3}}{2}+m \cdot L_{4}+m \cdot H_{2}, \\
& \left(x_{4}, y_{4}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0) \\
& \lim _{\left(x_{3}, y_{3}\right) \xrightarrow{\gamma_{\varphi_{0}}}(1,0)} F_{5}=(1+m) \cdot L_{4}+m \cdot L_{1} \cdot \lim _{y_{4} \rightarrow 0} \frac{y_{4}}{2}+m \cdot L_{3}-m \cdot H_{2} .
\end{aligned}
$$

We consider also the limits

$$
\begin{aligned}
\lim _{\substack{\tau_{25} \\
\left(x_{3}, y_{3}\right)}} & \left(F_{1}+F_{2}\right)=(1+2 m) \cdot\left(L_{1}+L_{2}\right) \\
& \left(x_{4}, y_{4}\right) \xrightarrow{\tau_{25}}(1,0) \\
\lim _{\substack{\left(x_{3}, y_{3}\right) \\
\left(x_{4}, y_{4}\right)}} & \left(F_{4}+F_{5}\right)=(1+2 m) \cdot\left(L_{3}+L_{4}\right)+ \\
& \left(x_{5}, y_{5}\right) \xrightarrow{\tau_{25}}(1,0) \\
& m \cdot L_{1} \cdot \lim _{y_{4} \rightarrow 0} \frac{y_{4}}{2}+m \cdot L_{2} \cdot \lim _{y_{3} \rightarrow 0} \frac{y_{3}}{2}
\end{aligned}
$$

Clearly the solutions of (5) are also solutions of $F_{1}+F_{2}=0$ and $F_{4}+F_{5}=0$. Next we analyze the possible solutions of (5) depending on the values of $L_{1}$ and $L_{2}$.

Case $L_{1}=\infty, L_{2}=\infty$. If $L_{1}$ and $L_{2}$ are infinity of different order, then $F_{1}+F_{2}$ tends to infinity (see (29)). Assume now that $L_{1}$ and $L_{2}$ are infinity of the same order. It is easy to see that if equation $F_{1}+F_{2}=0$ is satisfied then $\cos \theta_{0}=-\cos \varphi_{0}$; that is, $\varphi_{0}=\pi \pm \theta_{0}$. If $\theta_{0} \neq \pi / 2$, then $L_{1}$ and $L_{2}$ are infinity of order $1 / r^{2}$ as $r \rightarrow 0$, see Lemma 10. Moreover

$$
\bar{H}_{1}=\frac{\cos \theta_{0}-\cos \varphi_{0}}{r^{2}\left(2-2 \cos \left(\theta_{0}-\varphi_{0}\right)^{3 / 2}\right.}= \begin{cases}\frac{\cos \theta_{0}}{4 r^{2}\left(\cos ^{2} \theta_{0}\right)^{3 / 2}} & \text { if } \varphi_{0}=\pi-\theta_{0} \\ \frac{\cos \theta_{0}}{4 r^{2}} & \text { if } \varphi_{0}=\pi+\theta_{0}\end{cases}
$$

Thus $H_{1}$ is infinity of order $1 / r^{2}$ as $r \rightarrow 0$. In short, if $\theta_{0} \neq \pi / 2$, then $F_{1}$ tends to infinity and system (5) cannot be satisfied.

If $\theta_{0}=\pi / 2$ and consequently $\varphi_{0}= \pm \pi / 2$, then that $L_{3}$ is infinity of order $1 / r^{2}$ as $r \rightarrow 0$ and $L_{4}$ is infinity of order $1 / R^{2}$ as $R \rightarrow 0$, see Lemma 10. Thus, if $r$ and $R$ have different orders then $F_{4}+F_{5}$ tends to infinity and there are no solutions of (5). If $r$ and $R$ have the same order, then it is easy to see that if equation $F_{4}+F_{5}=0$ is satisfied, then $\sin \theta_{0}=-\sin \varphi_{0}$. Thus $\theta_{0}=\pi / 2$ and $\varphi_{0}=-\pi / 2$ and

$$
\bar{H}_{2}=\frac{r \sin (\pi / 2)-r \sin (-\pi / 2)}{\left(r^{2}+r^{2}-2 r^{2} \cos (\pi)\right)^{3 / 2}}=\frac{1}{4 r^{2}}
$$

So $H_{2}$ is infinity of order $1 / r^{2}$ as $r \rightarrow 0$. Therefore $F_{4}$ is infinity of order $1 / r^{2}$ as $r \rightarrow 0$ which implies that there are no solutions of (5) in this case.

Cases $L_{1}=\infty, L_{2}=b \neq \infty$ and $L_{1}=a \neq \infty, L_{2}=\infty$. These cases cannot provide solutions of (5) because $F_{1}+F_{2}$ becomes infinity.

Case $L_{1}=a \neq \infty, L_{2}=b \neq \infty$. From (29), in order to have a solution of $F_{1}+F_{2}=0$, we need that $a=-b$. Since $L_{1}=a \neq \infty, L_{2}=b \neq \infty$, from Lemma 10, we have that $\theta_{0}=\pi / 2$ and $\varphi_{0}= \pm \pi / 2$. Proceeding as in the case $L_{1}=\infty$ and $L_{2}=\infty$ with $\theta_{0}=\pi / 2$ we prove that the case $L_{1}=a \neq \infty, L_{2}=b \neq \infty$ cannot provide solutions of system (5).

# 8.2. Central configurations for $m>0$ sufficiently small with one small mass coming from infinity 

Without loss of generality we can assume that the small mass coming from infinity is $m_{3}$. We introduce polar coordinates $\left(x_{3}, y_{3}\right)=(r \cos \theta, r \sin \theta)$. So the mass $m_{3}$ comes from infinity when $r \rightarrow+\infty$ by following the direction of the ray $\theta=\theta_{0}$ with $\theta_{0} \in[0, \pi / 2]$ (remember that we have assumed that $x_{3}, y_{3} \geqslant 0$. Next we will prove that there are no solutions of (5) such that $r \rightarrow+\infty$ as $m \rightarrow 0$.

### 8.2.1. Case $m_{4}$ comes from infinity when $m \rightarrow 0$

After some computations we can see easily that

$$
\begin{array}{lll}
\lim _{r \rightarrow+\infty} \frac{x_{3}+1}{r_{13}^{3}}=0, & \lim _{r \rightarrow+\infty} \frac{x_{3}-1}{r_{23}^{3}}=0, & \lim _{r \rightarrow+\infty} \frac{x_{3}^{2}-1}{r_{13}^{3}}=0 \\
\lim _{r \rightarrow+\infty} \frac{x_{3}^{2}-1}{r_{23}^{3}}=0, & \lim _{r \rightarrow+\infty} \frac{y_{3}}{r_{13}^{3}}=0, & \lim _{r \rightarrow+\infty} \frac{y_{3}}{r_{23}^{3}}=0 \\
\lim _{r \rightarrow+\infty} \frac{\left(x_{3}+1\right) y_{3}}{r_{13}^{3}}=0, & \lim _{r \rightarrow+\infty} \frac{\left(x_{3}+1\right) y_{3}}{r_{23}^{3}}=0
\end{array}
$$

We introduce polar coordinates $\left(x_{4}, y_{4}\right)=(R \cos \varphi, R \sin \varphi)$. So the mass $m_{4}$ comes from infinity when $R \rightarrow+\infty$ by following the direction of the ray $\varphi=\varphi_{0}$. In a similar way than in (30) we get

$$
\begin{array}{lll}
\lim _{R \rightarrow+\infty} \frac{x_{4}+1}{r_{14}^{3}}=0, & \lim _{R \rightarrow+\infty} \frac{x_{4}-1}{r_{24}^{3}}=0, & \lim _{R \rightarrow+\infty} \frac{x_{4}^{2}-1}{r_{14}^{3}}=0 \\
\lim _{R \rightarrow+\infty} \frac{x_{4}^{2}-1}{r_{24}^{3}}=0, & \lim _{R \rightarrow+\infty} \frac{y_{4}}{r_{14}^{3}}=0, & \lim _{R \rightarrow+\infty} \frac{y_{4}}{r_{24}^{3}}=0 \\
\lim _{R \rightarrow+\infty} \frac{\left(x_{4}+1\right) y_{4}}{r_{14}^{3}}=0, & \lim _{R \rightarrow+\infty} \frac{\left(x_{4}+1\right) y_{4}}{r_{24}^{3}}=0
\end{array}
$$

Moreover

$$
\begin{aligned}
\ell_{1} & =\frac{x_{3}-x_{4}}{r_{34}^{3}}=\frac{r \cos \theta-R \cos \varphi}{\left(r^{2}+R^{2}-2 r R \cos (\theta-\varphi)\right)^{3 / 2}} \\
\ell_{2} & =\frac{\left(x_{3}+1\right)\left(x_{4}-1\right)}{r_{24}^{3}}=\frac{-1-r \cos \theta+R \cos \varphi+r R \cos \theta \cos \varphi}{\left(R^{2}-2 R \cos \varphi+1\right)^{3 / 2}} \\
\ell_{3} & =\frac{\left(x_{3}-1\right)\left(x_{4}+1\right)}{r_{14}^{3}}=\frac{-1+r \cos \theta-R \cos \varphi+r R \cos \theta \cos \varphi}{\left(R^{2}+2 R \cos \varphi+1\right)^{3 / 2}} \\
\ell_{4} & =\frac{\left(x_{3}+1\right)\left(x_{4}-1\right)}{r_{13}^{3}}=\frac{-1-r \cos \theta+R \cos \varphi+r R \cos \theta \cos \varphi}{\left(r^{2}+2 r \cos \varphi+1\right)^{3 / 2}} \\
\ell_{5} & =\frac{\left(x_{3}-1\right)\left(x_{4}+1\right)}{r_{23}^{3}}=\frac{-1+r \cos \theta-R \cos \varphi+r R \cos \theta \cos \varphi}{\left(r^{2}-2 r \cos \varphi+1\right)^{3 / 2}}
\end{aligned}
$$

and

$$
\begin{aligned}
\ell_{6} & =\frac{y_{3}-y_{4}}{r_{34}^{3}}=\frac{r \sin \theta-R \sin \varphi}{\left(r^{2}+R^{2}-2 r R \cos (\theta-\varphi)\right)^{3 / 2}} \\
\ell_{7} & =\frac{y_{3}\left(x_{4}-1\right)}{r_{24}^{3}}=\frac{-r \sin \theta+r R \sin \theta \cos \varphi}{\left(R^{2}-2 R \cos \varphi+1\right)^{3 / 2}} \\
\ell_{8} & =\frac{y_{3}\left(x_{4}+1\right)}{r_{14}^{3}}=\frac{r \sin \theta+r R \sin \theta \cos \varphi}{\left(R^{2}+2 R \cos \varphi+1\right)^{3 / 2}} \\
\ell_{9} & =\frac{\left(x_{3}+1\right) y_{4}}{r_{13}^{3}}=\frac{R \sin \varphi+r R \cos \theta \sin \varphi}{\left(r^{2}+2 r \cos \varphi+1\right)^{3 / 2}} \\
\ell_{10} & =\frac{\left(x_{3}-1\right) y_{4}}{r_{23}^{3}}=\frac{-R \sin \varphi+r R \cos \theta \sin \varphi}{\left(r^{2}-2 r \cos \varphi+1\right)^{3 / 2}}
\end{aligned}
$$

From (30), (31), (32) and (33) the limit of $F_{1}$ as $r, R \rightarrow+\infty$ can be reduced to the limit of

$$
m\left(\ell_{1}+\ell_{2}-\ell_{3}\right)-\frac{x_{3}}{4}
$$

Next we analyze this limit depending on the orders of $r$ and $R$.
Case $R$ and $r$ are infinities of different orders. We assume that $R=r^{\beta}$ with $\beta>0$ and $\beta \neq 1$ and that $\ell_{2}-\ell_{3}$ has order $r^{\gamma}$ for some $\gamma \in \mathbb{R}$ as $r \rightarrow+\infty$. It is easy to see that $\ell_{1} \rightarrow 0$ as $r, R \rightarrow+\infty$. Moreover it is easy to see that the order of $\ell_{2}-\ell_{3}$ is smaller than the order of $r^{1-2 \beta}$; that is, $\gamma<1-2 \beta$. In order to have solutions of equation $F_{1}=0$ the order of $m$ must be equal to the order of $r / r^{\gamma}=r^{1-\gamma}$. Since $\gamma<1-2 \beta, 1-\gamma>2 \beta$. Thus the order of $m$ is bigger than the order of $r^{2 \beta}$ which is impossible

because $\beta>0$ and $m \rightarrow 0$ as $r, R \rightarrow+\infty$. Therefore there are no solutions of (5) in this case.

Case $R$ and $r$ are infinities of the same orders. It is easy to see that if $R$ and $r$ have the same order, then $\ell_{2}, \ell_{3}, \ell_{4}$ and $\ell_{5}$ tend to 0 as $r \rightarrow+\infty$. Moreover the limit of $F_{1}+F_{2}$ when $r \rightarrow+\infty$ is equivalent to the limit of $-x_{3} / 4-x_{4} / 4$ when $r \rightarrow+\infty$. In order to have a solution of $F_{1}+F_{2}=0$ we need that $\cos \theta=-\cos \varphi$. On the other hand, $\ell_{7}, \ell_{8}, \ell_{9}$ and $\ell_{10}$ tend to 0 as $r \rightarrow+\infty$ and the limit of $F_{4}+F_{5}$ when $r \rightarrow+\infty$ is equivalent to $-y_{3} / 4-y_{4} / 4$ when $r \rightarrow+\infty$. In order to have a solution of $F_{4}+F_{5}=0$ we need that $\sin \theta=-\sin \varphi$. Therefore we only can have solutions of $F_{1}+F_{2}=0$ and $F_{4}+F_{5}=0$ when either $\theta=0$ and $\varphi=\pi$ or $\theta=\pi / 2$ and $\varphi=3 \pi / 2$. If $\theta=0$ and $\varphi=\pi$, then $\ell_{1} \rightarrow 0$ as $r \rightarrow+\infty$, so $F_{1}$ tends to $\infty$ as $r \rightarrow+\infty$, see (34). If $\theta=\pi / 2$ and $\varphi=3 \pi / 2$, then $\ell_{6} \rightarrow 0$ as $r \rightarrow+\infty$, so by proceeding in a similar way wee see $F_{4}$ tends $\infty$ as $r \rightarrow+\infty$. In short there are no solutions of (5) in this case.

# 8.2.2. Case $m_{4}$ tends to $m_{1}$ when $m \rightarrow 0$ 

We introduce polar coordinates $\left(x_{4}, y_{4}\right)=(-1+R \cos \varphi, R \sin \varphi)$. This means that if $R \rightarrow 0$, then the mass $m_{4}$ tends to $m_{1}$ following the direction of the ray $\varphi=\varphi_{0}$. We can see easily that

$$
\frac{x_{3}-x_{4}}{r_{34}^{3}} \rightarrow 0 \quad \text { as } r \rightarrow+\infty \text { and } R \rightarrow 0
$$

We define $\bar{L}_{2}$ as in (25). If $\bar{L}_{2}=b \neq \pm \infty$, then it is easy to see from (30) that $F_{1}$ tends to $\infty$ as $r \rightarrow+\infty$ and $R \rightarrow 0$. Otherwise $\bar{L}_{2}$ is infinity of order $1 / R^{\alpha}$ as $R \rightarrow 0$ for some $\alpha>0$ and consequently $F_{2}$ is an infinity of order $1 / R^{\alpha}$ as $R \rightarrow 0$. Therefore there are no solutions of (5) in this case.

### 8.2.3. Case $m_{4}$ tends to $m_{2}$ when $m \rightarrow 0$

By proceeding as in the previous case we can prove that there are no solutions of (5) with $m_{3}$ coming from infinity and $m_{4}$ tending to $m_{2}$ as $m \rightarrow 0$.

### 8.2.4. None of the above cases

If $m_{4}$ is far from either infinity, or $m_{1}$ and $m_{2}$ when $m \rightarrow 0$, then $F_{1}$ is infinity of order $r$ as $r \rightarrow+\infty$. Therefore there are no solutions of (5) in this case.


# Bifurcations of Central Configurations in the Four-Body Problem with some equal masses 


#### Abstract

We study the bifurcations of central configurations of the Newtonian four-body problem when some of the masses are equal. First, we continue numerically the solutions for the equal mass case, and we find values of the mass parameter at which the number of solutions changes. Then, using the Krawczyk method and some result of equivariant bifurcation theory, we rigorously prove the existence of such bifurcations and classify them.


## Contents

1 Introduction
2 Equations of central configurations in terms of mutual distances
2.1 Dziobeck equations
2.2 Albouy-Chenciner equations


3 Theoretical Background ..... 7
3.1 Interval arithmetic and the Krawczyk operator ..... 7
3.2 Bifurcations ..... 8
3.3 Group actions and equivariant bifurcation theory ..... 9
4 The Case of Three Equal Masses ..... 11
4.1 Equivariance ..... 11
4.2 The global picture ..... 12
4.3 Bifurcation at $m=m^{*} \approx 1.00266054$ ..... 14
4.4 Bifurcation at $m=m_{* *} \approx 0.99184227$ ..... 16
4.5 Bifurcation at $m=m_{*}=(81+64 \sqrt{3}) / 249 \approx 0.77048695$ ..... 19
5 The Case of Two Pairs of Equal Masses ..... 22
5.1 Equivariance ..... 22
5.2 The global picture ..... 23
5.3 Bifurcation at $m=\tilde{m}_{* *} \approx 0.99729401$ ..... 24
5.4 Bifurcation at $m=\tilde{m}_{*} \approx 0.99229944$ ..... 25

# 1 Introduction 

The Newtonian $n$-body problem is the study of the dynamics of $n$ point particles with masses $m_{i} \in \mathbb{R}^{+}$and positions $q_{i} \in \mathbb{R}^{d}(i=1, \ldots, n)$, moving according to Newton's laws of motion:

$$
m_{j} \ddot{q}_{j}=F_{i}=\sum_{i \neq j} \frac{m_{i} m_{j}\left(q_{i}-q_{j}\right)}{r_{i j}^{3}} \quad 1 \leq j \leq n
$$

where $r_{i j}=\left\|q_{i}-q_{j}\right\|$ is the distance between $q_{i}$ and $q_{j}$. The force vector $F_{i} \in \mathbb{R}^{d}$ can also be written as a partial gradient $F_{i}=\nabla_{i} U$ where

$$
U=\sum_{i<j} \frac{m_{i} m_{j}}{r_{i j}}
$$

is the Newtonian potential function and $\nabla_{i}$ denotes the vector of partial derivatives with respect to the $d$ components of $q_{i}$.

In the Newtonian $n$-body problem, the simplest possible motions are such that the configuration is constant up to rotations and scaling, and each body describes a Keplerian orbit. Only some special configurations of particles

are allowed in such motions. Wintner called them central configurations (or c.c's, for short). A configuration $\left(q_{1}, \ldots, q_{n}\right)$ is called a central configuration if and only if there exists a $\lambda \in \mathbb{R}$ such that

$$
\lambda\left(q_{j}-q_{G}\right)=\frac{1}{m_{j}} \nabla_{j} U=\sum_{i \neq j} \frac{m_{i}\left(q_{i}-q_{j}\right)}{r_{i j}^{3}} \quad 1 \leq j \leq n
$$

where $q_{G}=\sum_{i} m_{i} q_{i} / \sum_{i} m_{i}$ is the center of mass. It turns out that the values of $\lambda$ are uniquely determined by the equation above, in fact

$$
\lambda=-\frac{U}{I}
$$

where

$$
I=\sum_{i} m_{i}\left\|q_{i}-q_{G}\right\|^{2}=\frac{1}{M} \sum_{i<j} m_{i} m_{j} r_{i j}^{2}
$$

is the moment of inertia with respect to $q_{G}$, and $M=\sum_{i} m_{i}$. Equations (2) are invariant under rotations, dilatations and translations on the plane. Two central configurations are considered equivalent if they are related by these symmetry operations, and thus lie in the same equivalence class.

The question of the existence and classification of central configurations is a difficult and fascinating problems that dates back to the work of 18thcentury mathematicians Euler and Lagrange, and has been revived by contemporary mathematician Steven Smale  with the conjecture (due to Chazy  and Wintner ) that the number of central configurations is finite.

An exact count of the central configurations of $n$-bodies was found by Moulton  for the collinear $n$-body problem. Moulton showed that there are $n!/ 2$ collinear equivalence classes, that is there is one collinear relative equilibrium for each ordering of the masses.

The number of planar central configurations of $n$-bodies (for arbitrary $n$ ) is know when some of the masses are assumed sufficiently small , however, an exact count for an arbitrary set of positive masses is known only when $n=2,3$.

In the four-body problem the number of central configurations has been shown to be finite , but a complete characterization is known only for the equal masses case , when one of the masses is sufficiently small , and when there are two pairs of equal masses, with one pair sufficiently small . There are also some partial results if some of the masses are equal .

There are a number of papers investigating the bifurcations of central configurations in the four-body problem. In  Simó presented a numerical study of the bifurcations of the central configurations with arbitrary masses, and gave exact numbers of central configurations inferred by these numerical computations. In  Meyer and Schmidt studied the equilateral triangle family of central configurations and showed that families of isosceles triangle bifurcate from the equilateral triangle family. In  Bernat, Llibre and PerezChavela, studied the kite configurations of the four-body problem with three equal masses and found two bifurcation in the number of c.c.'s, one of which is Meyer and Schmidt's bifurcation. This allowed them to obtain an exact count of the number of kite shaped c.c's.

In this paper we study the four-body problem in two special cases: the case where three of the masses are equal and the case where there are two pairs of equal masses. In both cases we first do a numerical study by varying one of the masses from the equal masses case. This allows us to determine, numerically, the values of the mass parameter for which there are bifurcations. Then we use interval arithmetic to implement the Krawczyk method  and prove rigorously the existence of the bifurcations we located numerically. In the three equal masses case we recover the bifurcations obtained in  and  but we also find three supercritical pitchfork bifurcations for $m=m_{* *} \approx 0.99184227$. These are symmetry breaking bifurcations where one $\mathbb{Z}_{2}$-symmetric configurations splits into three, two of which have no symmetry. In the case of two pairs of equal masses ( $m_{1}=m_{2}=1$ and $m_{3}=m_{4}=m$ with $m \leq 1$ ) we find two bifurcations: a fold and a supercritical pitchfork bifurcation. A consequence of our analysis is that, based on our numerical results, we are able to give an exact count of the number of c.c's in the four body problem with some equal masses. The numbers we obtain seem to be compatible with the numerical results of Simó . Unfortunately, our counts are also based on certain numerical computations and therefore we are unable to prove the well known conjecture that states that, given four masses, there is a unique convex c.c. for each cyclic order of the masses (see Problem 10 in , and references therein).

Interestingly, in the four-vortex problem, a companion problem of the four-body problem, it is possible to give an exact count of the number of central configuration if some of the vorticities are equal. In fact, in  we gave a complete description of the central configurations for the four-vortex problem with two pairs of equal vortices. Unfortunately, the approach taken in  does not work in the Newtonian four-body problem, because the degree

of the polynomial equations studied is greater and thus it is not possible to perform the same type of Gröbner basis computations.

The paper is organized as follows. In Section 2 we write the Dziobeck and the Albouy-Chenciner equations for central configurations. In Section 3 we briefly recall some important tools, namely the Krawczyk method, some bifurcation theory and some facts related to equivariant bifurcation theory. In Section 4 we study the bifurcations in the case of three equal masses. In Section 5 we study the bifurcations in the case of two pairs of equal masses.

# 2 Equations of central configurations in terms of mutual distances 

### 2.1 Dziobeck equations

For $n=4$ there are six mutual distances. A necessary and sufficient condition that six positive numbers $r_{i j}, 1 \leq i<j \leq 4$, are the mutual distances between four coplanar points is

$$
S=\left[\begin{array}{cccccc}
0 & 1 & 1 & 1 & 1 \\
1 & 0 & r_{12}^{2} & r_{13}^{2} & r_{14}^{2} \\
1 & r_{12}^{2} & 0 & r_{23}^{2} & r_{24}^{2} \\
1 & r_{13}^{2} & r_{23}^{2} & 0 & r_{34}^{2} \\
1 & r_{14}^{2} & r_{24}^{2} & r_{34}^{2} & 0
\end{array}\right]
$$

This determinant is equal to $288 V^{2}$, where $V$ is the volume of the tetrahedron whose six edges are the mutual distances $r_{i j}$. This formula is the threedimensional generalization of Heron's formula for the are of a triangle.

Using Lagrange multipliers, Dziobeck characterized the central configurations of four bodies as the critical points of

$$
V=U+\lambda_{0}\left(I-I_{0}\right)+\mu S
$$

viewed as a function of eight variables $\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}$, subject to the constraints $I=I_{0}$ and $S=0$. Here $\lambda_{0}$ and $\mu$ are Lagrange multipliers and $I_{0}$ is a fixed moment of inertia. Hence, the central configurations are the solution of the following eight equations:

$$
\begin{array}{ll}
\frac{\partial V}{\partial \lambda_{0}}=0, & \frac{\partial V}{\partial \mu}=0 \\
\frac{\partial V}{\partial r_{i j}}=0 & 1 \leq i<j \leq 4
\end{array}
$$

We will denote by $F=\left(F_{1}, \ldots, F_{8}\right)$ the equation obtained from the equations above by clearing the denominators, with the normalization $I_{0}=1$, and we will refer to them as Dziobek equations. Note that this equations give only the "strictly planar" configurations, that is the planar configurations that are not collinear.

# 2.2 Albouy-Chenciner equations 

The Albouy-Chenciner equations are algebraic equations satisfied by the mutual distances $r_{i j}$ of every central configuration $$

$$
\sum_{k=1}^{n} m_{k}\left[S_{i k}\left(r_{j k}^{2}-r_{i k}^{2}-r_{i j}^{2}\right)+S_{j k}\left(r_{i k}^{2}-r_{j k}^{2}-r_{i j}^{2}\right)\right]=0
$$

for $1 \leq i<j \leq n$, where $S_{i k}$ and $S_{j k}$ are given by When $m=m_{* *}$ the $4 \times 4$ submatrix obtained from the Jacobian of the Albouy-Chenciner equations by deleting the last two rows and columns has non-zero determinant.

$$
S_{i j}=\frac{1}{r_{i j}^{3}}+\lambda^{\prime} \quad(i \neq j), \quad S_{i i}=0
$$

where $\lambda^{\prime}=\lambda / M$. Since any relative equilibria may be rescaled, we will impose the normalization $\lambda^{\prime}=-1$. This, in this case, can be assumed without loss of generality, however, this is not true in the vortex case, . After clearing the denominators in the $S_{i j}$ terms, these equations form a polynomial system in the $r_{i j}$ variables. These new equations are also called Albouy-Chenciner (AC) equations.

In the four body case the AC equations reduce to a system of six algebraic equations in six variables (the mutual distances). Note that the solutions of the Albouy-Chenciner equations for the four body problem include collinear solutions, planar solutions and one three-dimensional solution (the regular tetrahedron). It follows that the number of solution of the AC equation is

equal to the number of solutions of the Dziobeck ones plus 13, since it is well known that the number of collinear solutions in the four body problem is always 12 .

# 3 Theoretical Background 

In this section we review a few theoretical facts concerning interval arithmetic, bifurcation theory and group actions, that we will be useful in our analysis.

### 3.1 Interval arithmetic and the Krawczyk operator

We discuss a method to find rigorous bounds on the solution of a nonlinear smooth function $F: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$. Let $\mathbf{x} \in \mathbb{R}^{n}$, and let $[\mathbf{x}]_{r} \subset \mathbb{R}^{n}$ be the interval set centered at $\mathbf{x}$ with radius $r>0$. Namely,

$$
[\mathbf{x}]_{r}=\left\{\mathbf{y} \in \mathbb{R}^{n}:\|\mathbf{y}-\mathbf{x}\|_{\infty} \leq r\right\}
$$

where $\|\cdot\|_{\infty}$ is the infinity norm. Assume the derivative of $F$ at $\mathbf{x}$, denoted by $D F(\mathbf{x})$ is nonsingular, then the Krawczyk operator of $F$ associated with $[\mathbf{x}]_{r}$ is defined as

$$
K\left(\mathbf{x},[\mathbf{x}]_{r}\right)=\mathbf{x}-D F(\mathbf{x})^{-1} F(\mathbf{x})+\left[I-D F(\mathbf{x})^{-1} D F\left([\mathbf{x}]_{r}\right)\right]\left([\mathbf{x}]_{r}-\mathbf{x}\right)
$$

The Krawczyk operator can be used to test the existence and uniqueness of a zero in a set $[\mathbf{x}]_{r}$ using the following theorem

Theorem 1. Let $F: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$ be a smooth nonlinear function

1. If $F$ has a root $x^{*} \in[\mathbf{x}]_{r}$ then $x^{*} \in[\mathbf{x}]_{r} \cap K\left(\mathbf{x},[\mathbf{x}]_{r}\right)$.
2. If $[\mathbf{x}]_{r} \cap K\left(\mathbf{x},[\mathbf{x}]_{r}\right)=\varnothing$ then $F$ has no zeroes in $[\mathbf{x}]_{r}$.
3. If $\varnothing \neq K\left(\mathbf{x},[\mathbf{x}]_{r}\right)$ is a subset of the interior of $[\mathbf{x}]_{r}$ then $F$ contains a unique zero in $\mathbf{x}$.

This is essentially a fixed point theorem. A proof is given in . Using this theorem it is possible to implement code to find bounds on roots of nonlinear equations. We wrote the code for Sage , using Sage arbitrary

precision real intervals. Sage real intervals are based on the Multiple Precision Floating-point Interval library (MPFI) by Nathalie Revol and Fabrice Rouillier.

An interval $$ will often be written as a standard floating-point number with a question mark (for instance, 3.1416? ). The question mark indicates that the preceding digit may have an error of $\pm 1$. Note that in such cases usually a more precise bound is known, but it is not displayed to save space.

# 3.2 Bifurcations 

The saddle-node, transcritical and pitchfork bifurcations are the most important types of bifurcations that occur in system with a system whose linearization has a one dimensional null-space. Let

$$
F: \mathbb{R}^{n} \times \mathbb{R} \rightarrow \mathbb{R}^{n}:(\mathbf{x}, \mu) \rightarrow F(\mathbf{x}, \mu)
$$

be a smooth map, where $\mu$ is a parameter. We use $D F$ to denote the Jacobian matrix, and $F_{\mu}$ to denote the vector of partial derivatives of the components of $F$ with respect to $\mu$. We are interested in studying how the number of solutions of the system $F(\mathbf{x}, \mu)=0$ varies as $\mu$ varies. We have the following useful theorem, a proof of which can be found in .

Theorem 2. Suppose that $F\left(x_{0}, \mu_{0}\right)=0$ and that the Jacobian matrix $A=$ $D F\left(\mathbf{x}_{0}, \mu_{0}\right)$ has a simple eigenvalue $\lambda=0$ with eigenvector $\mathbf{v}$, and that the matrix $A^{T}$ has an eigenvector $\mathbf{w}$ corresponding to the eigenvalue $\lambda=0$. Then

1. If $\mathbf{w}^{T} F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right) \neq 0, \quad \mathbf{w}^{T}\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right] \neq 0$, then the system experiences a fold bifurcation at the equilibrium point $\mathbf{x}_{0}$ as the parameter $\mu$ passes through the bifurcation value $\mu=\mu_{0}$.
2. If

$$
\begin{aligned}
& \mathbf{w}^{T} F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)=0 \\
& \mathbf{w}^{T}\left[D F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right) \mathbf{v}\right] \neq 0 \\
& \mathbf{w}^{T}\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right] \neq 0
\end{aligned}
$$

then the system experiences a transcritical bifurcation at the equilibrium point $\mathbf{x}_{0}$ as the parameter $\mu$ passes through the bifurcation value $\mu=\mu_{0}$.

3. If

$$
\begin{aligned}
& \mathbf{w}^{T} F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)=0 \\
& \mathbf{w}^{T}\left[D F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right) \mathbf{v}\right] \neq 0 \\
& \mathbf{w}^{T}\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right]=0 \\
& \mathbf{w}^{T}\left[D^{3} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right] \neq 0
\end{aligned}
$$

then the system experiences a pitchfork bifurcation at the equilibrium point $\mathbf{x}_{0}$ as the parameter $\mu$ passes through the bifurcation value $\mu=\mu_{0}$. If $\mathbf{w}^{T}\left[D^{3} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right]<0$ the branches occur for $\mu>\mu_{0}$, and the bifurcation is supercritical. Otherwise, the branches occur for $\mu<\mu_{0}$ and the bifurcation is subcritical.

# 3.3 Group actions and equivariant bifurcation theory 

Definition 1. Let $M$ be a manifold and let $G$ be a group. A action of a group $G$ on $M$ is a map $\Phi: G \times M \rightarrow M$ such that:
(i) $\Phi(E, x)=x$, for all $x \in M$, where $E$ is the identity element of $G$; and
(ii) $\Phi(g, \phi(h, x))=\Phi(g h, x)$ for all $g, h \in G$ and $x \in M$.

For every $g \in G$ let $\Phi_{g}: M \rightarrow M: x \rightarrow \Phi(g, x)$; then (i) becomes $\Phi_{E}=\operatorname{id}_{M}$ while (ii) becomes $\Phi_{g h}=\Phi_{g} \circ \Phi_{h}$. In the special but important case where $M$ is a vector space $V$ and each $\Phi_{g}$ a linear transformation, the action of $G$ on $V$ is called a linear representation of $G$ on $V$.

Definition 2. Let $M$ and $N$ be manifolds and let $\Phi: G \times M \rightarrow M$, $\Psi: G \times N \rightarrow N$ be two actions. Assume that $F: M \rightarrow N$ is a smooth function, then we say that $F$ is equivariant with respect to these actions if for all $g \in G$

$$
F \circ \Phi_{g}=\Psi_{g} \circ F
$$

Definition 3. Let $G$ be a group acting on $M$. The isotropy subgroup of any $x \in M$ is

$$
\Sigma_{x}:=\left\{g \in G: \Phi_{g}(x)=x\right\} \subset G
$$

If $\Sigma_{x}$ is nontrivial then $x$ is called an isotropic point .

Definition 4. Let $\Sigma$ be a subgroup of $G$ where $G$ is a compact Lie group acting on a vector space $V$. The fixed point subspace of $\Sigma$ is

$$
\operatorname{Fix}(\Sigma)=\left\{x \in V: \Phi_{g}(x)=x, \forall g \in \Sigma\right\}
$$

We are interested in the case where the group $G=\mathbb{Z}_{2}$ and $\{I, R\}$ is a linear representation of $\mathbb{Z}_{2}$ in $\mathbb{R}^{n}$, where $I$ is the identity and $R$ is an $n \times n$ matrix satisfying

$$
R^{2}=I
$$

We want to show that if $x_{0}$ is $\mathbb{Z}_{2}$-symmetric, that is $R x_{0}=x_{0}$ then the symmetry can be helpful in determining the type of bifurcation.

Lemma 1. Let $F: \mathbb{R}^{n} \times \mathbb{R} \rightarrow \mathbb{R}^{n}:(\mathbf{x}, \mu) \rightarrow F(\mathbf{x}, \mu)$ be a smooth function. Suppose that $F$ is $\mathbb{Z}_{2}$-equivariant for each $\mu$, that is $F(R \mathbf{x}, \mu)=R F(\mathbf{x}, \mu)$ for every $\mu$, and let $\mathbf{x}_{0}$ such that $R \mathbf{x}_{0}=\mathbf{x}_{0}$. Let $F\left(\mathbf{x}_{0}, \mu .0\right)=0$ and let $A=$ $D F\left(\mathbf{x}_{0}, \mu_{0}\right)$. Suppose that $A$ has a simple eigenvalue $\lambda=0$ with eigenvector $\mathbf{v}$ such that $R \mathbf{v}=-\mathbf{v}$, and that $A^{T}$ has an eigenvector $\mathbf{w}$ corresponding to $\lambda=0$. Then

$$
\begin{aligned}
& \mathbf{w}^{T} F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)=0 \\
& \mathbf{w}^{T}\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right]=0
\end{aligned}
$$

Proof. We prove that first expression is zero. Differentiating $F(R \mathbf{x}, \mu)=$ $R F(\mathbf{x}, \mu)$ with respect to $\mu$ at the point $\left(\mathbf{x}_{0}, \mu_{0}\right)$, and using the fact that $R \mathbf{x}_{0}=\mathbf{x}_{0}$, yields

$$
F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)=R F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)
$$

Since the symmetry of the kernel and cokernel are the same $R \mathbf{v}=-\mathbf{v}$ implies $\mathbf{w}^{T} R=-\mathbf{w}^{T}$. Thus, applying $\mathbf{w}^{T}$ to the left of the equation above, we obtain

$$
\mathbf{w}^{T} F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)=\mathbf{w}^{T} R F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)=-\mathbf{w}^{T} F_{\mu}\left(\mathbf{x}_{0}, \mu_{0}\right)
$$

We now show that the second expression is zero. Differentiating $F(R \mathbf{x}, \mu)=$ $R F(\mathbf{x}, \mu)$ with respect to $\mathbf{x}$ yields

$$
D F(R \mathbf{x}, \mu)(R \mathbf{u})=R[D F(\mathbf{x})(\mathbf{u})]
$$

differentiating again and computing the derivative at $\left(\mathbf{x}_{0}, \mu\right)$ :

$$
D^{2} F\left(R \mathbf{x}_{\mathbf{0}}, \mu_{0}\right)(R \mathbf{u}, R \mathbf{v})=R\left[D^{2} F\left(\mathbf{x}_{\mathbf{0}}, \mu_{0}\right)(\mathbf{u}, \mathbf{v})\right]
$$

If we apply $\mathbf{w}^{T}$ on the left put $\mathbf{u}=\mathbf{v}$ and assume $R \mathbf{x}_{\mathbf{0}}=\mathbf{x}_{\mathbf{0}}$ from the equation above we obtain

$$
\begin{aligned}
\mathbf{w}^{T} & {\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right]=\mathbf{w}^{T}\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(-\mathbf{v},-\mathbf{v})\right] } \\
& =\mathbf{w}^{T}\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(R \mathbf{v}, R \mathbf{v})\right]=\mathbf{w}^{T} R\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right] \\
& =-\mathbf{w}^{T}\left[D^{2} F\left(\mathbf{x}_{0}, \mu_{0}\right)(\mathbf{v}, \mathbf{v})\right]
\end{aligned}
$$

Another useful result is the following (see ):
Lemma 2. Suppose $T: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$ is a linear operator and $A$ is its matrix representation. If $T$ is $\mathbb{Z}_{2}$-equivariant then $A R=R A$. Suppose that the kernel of $A$ is one-dimensional, then $A \mathbf{v}=0$ implies $R \mathbf{v}=\mathbf{v}$ or $R \mathbf{v}=-\mathbf{v}$.

# 4 The Case of Three Equal Masses 

In this section we study the bifurcations of the four body problem with three equal masses. In the first subsection we show that the equation of the central configurations are equivariant with respect to the group $D_{6}$. In the following section we give an overview of the three bifucations we found. In the last three subsections of this section we analyze each of the bifurcations in detail.

### 4.1 Equivariance

Recall that the dihedral group of order six, is a group with six elements $D_{6}=\left\{E, g_{1}, g_{2}, g_{3}, g_{4}, g_{5}\right\}$ with $g_{3}=g_{1} g_{2} g_{1}, g_{4}=g_{1} g_{2}, g_{5}=g_{2} g_{1}$ and Cayley table

| $\circ$ | $E$ | $g_{1}$ | $g_{2}$ | $g_{3}$ | $g_{4}$ | $g_{5}$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| $E$ | $E$ | $g_{1}$ | $g_{2}$ | $g_{3}$ | $g_{4}$ | $g_{5}$ |
| $g_{1}$ | $g_{1}$ | $E$ | $g_{4}$ | $g_{5}$ | $g_{2}$ | $g_{3}$ |
| $g_{2}$ | $g_{2}$ | $g_{5}$ | $E$ | $g_{4}$ | $g_{3}$ | $g_{1}$ |
| $g_{3}$ | $g_{3}$ | $g_{4}$ | $g_{5}$ | $E$ | $g_{1}$ | $g_{2}$ |
| $g_{4}$ | $g_{4}$ | $g_{3}$ | $g_{1}$ | $g_{2}$ | $g_{5}$ | $E$ |
| $g_{5}$ | $g_{5}$ | $g_{2}$ | $g_{3}$ | $g_{1}$ | $E$ | $g_{4}$ |

where $E$ is the identity. This group is isomorphic to the symmetric group of degree three. The proper subgroups of $D_{6}$ are $\{E\}$ (the trivial group),

$\left\{E, g_{1}\right\},\left\{E, g_{2}\right\},\left\{E, g_{3}\right\}$, and $\left\{E, g_{4}, g_{5}\right\}$ (the cyclic group of order 3 ). Consider the four body problem with three equal masses, for example let $m_{1}=m_{2}=m_{3}=1$ and $m_{4}=m$, and consider the action $\Phi$ of the dihedral group $D_{6}$ on $\mathbb{R}^{8}$ defined by

$$
\begin{aligned}
\Phi_{E} & =e:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \\
\Phi_{g_{1}} & =\gamma_{1}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{13}, r_{12}, r_{14}, r_{23}, r_{34}, r_{24}\right) \\
\Phi_{g_{2}} & =\gamma_{2}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{23}, r_{13}, r_{34}, r_{12}, r_{24}, r_{14}\right) \\
\Phi_{g_{3}} & =\gamma_{3}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{12}, r_{23}, r_{24}, r_{13}, r_{14}, r_{34}\right) \\
\Phi_{g_{4}} & =\gamma_{4}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{13}, r_{23}, r_{34}, r_{12}, r_{14}, r_{24}\right) \\
\Phi_{g_{5}} & =\gamma_{5}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{23}, r_{12}, r_{24}, r_{13}, r_{34}, r_{14}\right)
\end{aligned}
$$

Then, for each fixed value of $m_{4}$ we can think of the Dziobeck equations as a map $F: \mathbb{R}^{8} \rightarrow \mathbb{R}^{8}$. A computation shows that this map is equivariant with respect to the action $\Phi$ for each value of $m_{4}$.

Similarly one can consider the action $\Phi$ of the dihedral group $D_{6}$ on $\mathbb{R}^{6}$ defined by

$$
\begin{aligned}
& \Phi_{E}=e:\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \\
& \Phi_{g_{1}}=\gamma_{1}:\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(r_{13}, r_{12}, r_{14}, r_{23}, r_{34}, r_{24}\right) \\
& \Phi_{g_{2}}=\gamma_{2}:\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(r_{23}, r_{13}, r_{34}, r_{12}, r_{24}, r_{14}\right) \\
& \Phi_{g_{3}}=\gamma_{3}:\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(r_{12}, r_{23}, r_{24}, r_{13}, r_{14}, r_{34}\right) \\
& \Phi_{g_{4}}=\gamma_{4}:\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(r_{13}, r_{23}, r_{34}, r_{12}, r_{14}, r_{24}\right) \\
& \Phi_{g_{5}}=\gamma_{5}:\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(r_{23}, r_{12}, r_{24}, r_{13}, r_{34}, r_{14}\right)
\end{aligned}
$$

Then, for each fixed value of $m_{4}$ we can think of the Albouy-Chenciner equations as a map $f: \mathbb{R}^{6} \rightarrow \mathbb{R}^{6}$. A computation shows that this map is equivariant with respect to the action $\Phi$ for each value of $m_{4}$.

# 4.2 The global picture 

In this subsection we give an overview of the bifurcations we found in the case three of the masses are equal. Many of the remarks are based on numerical computations. The central configurations of four bodies with four equal

masses are well understood since the work of Alain Albouy . Hence, one can compute numerical approximations of the central configurations and then use continuation methods to find the central configurations for as the mass parameter varies. We computed the solutions of the central configuration equations using homotopy continuation methods for the equal mass case using HOM4PS2  for the Dziobeck equations, and HOM4body (an offshoot of HOM4PS2 ) for the Albouy-Chenciner equations . We then numerically studied the solutions of the equations as we varied the parameter $m=m_{4}$. We found that the Jacobian determinant of the equations vanishes along certain solutions at $m=m_{*}=(81+64 \sqrt{3}) / 249 \approx 0.77048695$, $m=m_{* *} \approx 0.99184227$ and at $m=m^{*} \approx 1.00266054$. Each of these values of $m$ actually correspond to a bifurcation.

At $m=m^{*}$ there are three fold bifurcations (or turning points). In this case, as $m$ is increased through $m^{*}$ six solutions coalesce to three. These solutions are illustrated in Figure 1.

At $m=m_{* *}$ there are three supercritical pitchfork bifurcation, so that, when decreasing $m$, nine solutions coalesce to three. Some of these solutions are illustrated in Figure 2, where we show one of the pitchfork bifurcations. The other two cases are similar, except that the solutions to be considered in the two remaining cases have $m_{1}$ in the convex hull formed by the other three masses, in one case, and $m_{2}$ in the other.

At $m=m_{*}=(81+64 \sqrt{3}) / 249 \approx 0.77048695$ four solutions coalesce into one, and then, as $m$ decreases the one solution branches into four solutions again (see Figure 3 ). This value of $m$ can easily be found analytically by studying the equilateral triangle family $r_{12}=r_{13}=r_{23}=1, r_{14}=r_{24}=$ $r_{34}=\frac{\sqrt{3}}{3}$. With the aid of a computer algebra system one can show that the value of the Jacobian determinant of the Dziobeck equations (with the normalizing condition $I=1$ ) along the equilateral family is

$$
-\frac{64(60 \sqrt{3}-133)(-249 m+64 \sqrt{3}+81)^{2} m^{2}(m+3)^{5}}{20667}
$$

which is non-zero for all positive values of $m$ except for $m=m_{* *}=(81+$ $64 \sqrt{3}) / 249 \approx 0.77048695$. The value of $m_{* *}$ was originally found analytically by Palmore  and an analytical study of the bifurcations at this point was done in .

The number of solutions to the Dziobeck and Albouy-Chenciner equations together with the number of geometrically distinct planar central configurations implied by our numerical computations is summarized in the following

# 4.3 Bifurcation at $m=m^{*} \approx 1.00266054$ 

We now use interval arithmetic to analyze one of the folds bifurcations at $m=m^{*}$ (the one with $m_{3}$ in the convex hull formed by the other masses). This approach will allow us to prove that the bifurcation exists and it is a fold. Let $\tilde{F}=\left[\left(F_{1}, \ldots, F_{8}, \operatorname{det}(D F)\right]\right.$ be the vector having as components the Dziobeck equations and the determinant of the Jacobian matrix of $F$. Then we can use the Krawczyk operator to prove the existence of a (unique) solution $\left(\mathbf{x}^{*}, m^{*}\right)$ to the equation $\tilde{F}(\mathbf{x}, m)=0$ in a small box. Let $\left[\mathbf{x}^{*}\right] \times\left[m^{*}\right]$ be the box containing the solution $\left(\mathbf{x}^{*}, m^{*}\right)$. Using as initial guess a value obtain using numerical computations we obtain that

$$
\left[\mathbf{x}^{*}\right]=\left[\begin{array}{c}
4.10486749931246396567394557 ? \\
0.7904883951465367 ? \\
0.98742601345653 ? \\
0.57921860462471 ? \\
1.00549177029900 ? \\
0.57921860462471 ? \\
1.00549177029900 ? \\
0.57304559793134 ?
\end{array}\right]
$$

and $\left[m^{*}\right]=1.00266054757261000068580350$ ?. Suppose $A=D F\left(\left[\mathbf{x}^{*}\right],\left[m^{*}\right]\right)$. Computing the echelon form of $A$ using Gauss elimination it is possible to show rigourosly that the null-space of $A$ is one dimensional, since we know that at least one eigenvalue must be zero, but seven of the eight rows of the echelon form are clearly non-zero. From the echelon form of $A$ we find that

On the left we show three pairs of solutions for $m_{1}=m_{2}=$ $m_{3}=m_{4}=1$. These solutions are continued, by increasing the parameter $m_{4}=m$. Then, at $m=m^{*} \approx 1.00266054 \ldots$, each pair of solution coalesce into one solution with a $\mathbb{Z}_{2}$ symmetry. This solution cannot be continued further, since we encounter a fold bifurcation.

the eigenvectors of $A$ and $A^{T}$ corresponding to the zero eigenvalue are

$$
\mathbf{v}=\left[\begin{array}{c}
0 . ? \times 10^{-9} \\
-0.179026448 ? \\
2.989514215 ? \\
-0.5496816801 ? \\
-1.4331568126 ? \\
-0.5496816801 ? \\
-1.4331568126 ? \\
1
\end{array}\right], \text { and } \quad \mathbf{w}=\left[\begin{array}{c}
0 . ? \times 10^{-9} \\
-0.235312131 ? \\
1.0068617795 ? \\
-0.5380276784 ? \\
-0.46549501352 ? \\
-0.5380276784 ? \\
-0.46549501352 ? \\
1
\end{array}\right]
$$

respectively. Moreover we have that

$$
\begin{aligned}
& \mathbf{w}^{T} F_{m}\left(\left[\mathbf{x}^{*}\right],\left[m^{*}\right]\right)=-6.501134640 ? \\
& \mathbf{w}^{T}\left[D^{2} F\left(\left[\mathbf{x}^{*}\right],\left[m^{*}\right]\right)(\mathbf{v}, \mathbf{v})\right]=-2066.64414 ?
\end{aligned}
$$

and thus, since the interval obtained do not contain zero, by Theorem 2, the bifurcation occurring at $\left(\mathbf{x}^{*}, m^{*}\right)$ is a fold bifurcation.

This bifurcation can also be studied by imposing the symmetry on the equations. This approach was taken in . Note the bifurcation value we obtain differs slightly from the one obtained in . We are confident that our value for $m^{*}$ is the correct one since we verified it using several different methods (including using the equations used in ).

# 4.4 Bifurcation at $m=m_{* *} \approx 0.99184227$ 

We now use interval arithmetic to analyze one of the pitchfork bifurcations at $m=m_{* *}$ (the one in which $m_{3}$ is in the convex hull formed by the other masses). Let $\tilde{F}=\left[\left(F_{1}, \ldots, F_{8}, \operatorname{det}(D F)\right]\right.$ be the vector having as components the Dziobeck equations and the determinant of the Jacobian matrix of $F$. Then we can use the Krawczyk operator to prove the existence of a (unique) solution $\left(\mathbf{x}_{* *}, m_{* *}\right)$ to the equation $\tilde{F}(\mathbf{x}, m)=0$ in a small box. Let $\left[\mathbf{x}_{* *}\right] \times$ $\left[m_{* *}\right]$ be the box containing the solution $\left(\mathbf{x}_{* *}, m_{* *}\right)$. Using as initial guess a

On the left we show three solutions for $m_{1}=m_{2}=m_{3}=m_{4}=1$. These solutions are continued, by varying the parameter $m=m_{4}$. As soon as $m<1$ the solutions loose symmetry. Then, at $m=m_{*} \approx 0.99184227 \ldots$, they coalesce into one solution with a $\mathbb{Z}_{2}$ symmetry. This solution can be continued further. On the right we show the corresponding solutions for $m_{1}=m_{2}=m_{3}=1$ and $m=0.005$.

value obtain using numerical computations we obtain that

$$
\left[\mathbf{x}_{* *}\right]=\left[\begin{array}{c}
4.07733304636361696432719 ? \\
0.777155400247894593452215 ? \\
1.013474951606110121651278 ? \\
0.57621299527180 ? \\
0.995153301920946 ? \\
0.57621299527180 ? \\
0.995153301920946 ? \\
0.582177257875351248071238 ?
\end{array}\right]
$$

and $\left[m_{* *}\right]=0.99184227439094091554349$ ?. Suppose $A=D F\left(\left[\mathbf{x}_{* *}\right],\left[m_{* *}\right]\right)$. Computing the echelon form of $A$ using Gauss elimination it is possible to show rigorously that the null-space of $A$ is one dimensional, since we know that at least one eigenvalue must be zero, but seven of the eight rows of the echelon form are clearly non-zero. From the echelon form of $A$ we find that the eigenvectors of $A$ and $A^{T}$ corresponding to the zero eigenvalue are respectively. Moreover we have that

$$
\begin{aligned}
& \mathbf{w}^{T} F_{m}\left(\left[\mathbf{x}_{* *}\right],\left[m_{* *}\right]\right)=0 . ? \times 10^{-10} \\
& \mathbf{w}^{T}\left[D F_{m}\left(\left[\mathbf{x}_{* *}\right],\left[m_{* *}\right]\right) \mathbf{v}\right]=34.944523147 ? \\
& \mathbf{w}^{T}\left[D^{2} F\left(\left[\mathbf{x}_{* *}\right],\left[m_{* *}\right]\right)(\mathbf{v}, \mathbf{v})\right]=0 . ? \times 10^{-7} \\
& \mathbf{w}^{T}\left[D^{3} F\left(\left[\mathbf{x}_{* *}\right],\left[m_{* *}\right]\right)(\mathbf{v}, \mathbf{v}, \mathbf{v})\right]=-2636.629585 ?
\end{aligned}
$$

and thus, by Theorem 2, this suggests that the bifurcation occurring at $\left(\mathbf{x}_{* *}, m_{* *}\right)$ is a pitchfork bifurcation. Since the last expression above is negative, again by Theorem 2, the branches occur for $m>m_{* *}$ and the bifurcation

is supercritical. To prove rigorously that the bifurcation we found is indeed a pitchfork bifurcation we use Lemma 1. In this case $R=\Phi_{g_{3}}$. The fact that $R \mathbf{x}^{*}=R \mathbf{x}^{*}$ follow from the symmetry of the solution (the symmetry of the solution can be shown rigorously by applying the Krawczyk operator to $\tilde{F}$ with the constraints imposed by the symmetry). Also, from Lemma 2 we have either $R \mathbf{v}=\mathbf{v}$ or $R \mathbf{v}=-\mathbf{v}$. Inspecting the interval expression we obtained for $\mathbf{v}$ it is clear that the first alternative cannot hold, hence $R \mathbf{v}=-\mathbf{v}$. Thus, the hypothesis of 1 are verified and the bifurcation is a pitchfork.

# 4.5 Bifurcation at $m=m_{*}=(81+64 \sqrt{3}) / 249 \approx 0.77048695$ 

The bifurcations at $m_{* *}$ is not covered by the theory of section 3.2 because the null-space is two dimensional. This bifurcation was studied in detail in  using the Dziobeck equations and the Liapunov-Schmidt reduction. For the sake of completeness we reproduce those results, but, to differentiate our computations from the ones in , we use the Albouy-Chenciner equations instead of the Dziobeck equations.

Let us denote the Albouy-Chenciner equations for the four-body problem (with normalization $\lambda^{\prime}=-U /(M I)=-1$ ) as $f=0$ where $f=$ $\left(f_{1}, f_{2}, f_{3}, f_{4}, f_{5}\right)$, and order the 6 variables by introducing the 6 -vector $z=$ $\left(z_{1}, z_{2}, z_{3}, z_{4}, z_{5}, z_{6}\right)=\left(r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right)$. The equilateral triangle family corresponds to the solution $z=a$ where $a=\left(\alpha, \alpha, \frac{\sqrt{3}}{3} \alpha, \alpha, \frac{\sqrt{3}}{3} \alpha, \frac{\sqrt{3}}{3} \alpha\right)$ with

$$
\alpha=\left(\frac{3(\sqrt{3} m+3)}{(m+3)}\right)^{1 / 3}
$$

When $m=m_{* *}$ the $4 \times 4$ submatrix obtained from the Jacobian of the Albouy-Chenciner equations by deleting the last two rows and columns has non-zero determinant.

Let $L_{0}=D f_{m_{* *}}(a)$ be the linearization of $f$ at $a$. Let $Q$ be the projection onto the subspace $\operatorname{span}\left(\left\{e_{5}, e_{6}\right\}\right)$ of $\mathbb{R}^{6}$, where $e_{1}, \ldots, e_{6}$ are the elements of the standard basis of $\mathbb{R}^{6}$. Let $P$ be the projection onto the subspace $\operatorname{span}\left(\left\{e_{5}, e_{6}\right\}\right)$. Let $z=P z+(I d-P) z=u+v$, so that $u=\left(0,0,0,0, z_{5}, z_{6}\right)$ and $v=\left(z_{1}, z_{2}, z_{3}, z_{4}, 0,0\right)$. The original equation $f_{m}(z)=0$ can now be split into the two equations:

$$
\tilde{f}_{m}(u, v)=(I d-Q) f_{m}(u+v)=0, \text { and } Q f_{m}(u+v)=0
$$
On the left we show four solutions of the AC equations for $m_{1}=$ $m_{2}=m_{3}=m_{4}=1$. We vary the parameter $m=m_{4}$ and continue these solutions up to $m=m_{* *} \approx 0.77048695 \ldots$, where they coalesce into one solution. This solution branches again into four solutions. These solutions can be continued further. On the right we show the corresponding solutions for $m_{1}=m_{2}=m_{3}=1$ and $m=0.005$.

By the implicit function theorem, since the Jacobian of $\tilde{f}_{m}$ with respect to $v$ is non-singular, the first of the equations above has the unique solution $v=v_{m}^{*}(u)$ for $m$ near $m_{* *}$. This solution can be substituted in the second equation and yields the so-called bifurcation equation

$$
G_{m}(u)=Q f_{m}\left(u+v_{m}^{*}(u)\right)=0
$$

In our case we use an approximation of $v_{m}^{*}(u)$ and $G_{m}(u)$ by Taylor expansion. More precisely, let $m=m_{* *}+\epsilon, z=a+\epsilon b+\epsilon^{2} c+\ldots$, where $a=$ $\left(\alpha, \alpha, \frac{\sqrt{3}}{3} \alpha, \alpha, \frac{\sqrt{3}}{3} \alpha, \frac{\sqrt{3}}{3} \alpha\right), b=\left(b_{1}, b_{2}, b_{3}, b_{4}, b_{5}, b_{6}\right), c=\left(c_{1}, c_{2}, c_{3}, c_{4}, c_{5}, c_{6}\right)$, and $\alpha$ is as above. We solve $(I d-Q) f_{m}(u+v)=0$ order by order and we substitute into the bifurcation equation $G_{m}(u)=0$. This allows us to find $b_{1}, b_{2}, b_{3}, b_{4}, c_{1}, c_{2}, c_{3}, c_{4}$ as functions of $b_{5}, b_{6}, c_{5}, c_{6}$. In particular we have

$$
\begin{aligned}
& b_{1}=\frac{1}{83}(81+64 \sqrt{3}) b_{6} \\
& b_{2}=\frac{1}{83}(81+64 \sqrt{3}) b_{5} \\
& b_{3}=-b_{6}-b_{5} \\
& b_{4}=-\frac{1}{83}(81+64 \sqrt{3})\left(b_{5}+b_{6}\right)
\end{aligned}
$$

we omit the expressions for the $c_{i} \mathrm{~s}$ since they are quite long. The equation $G_{m}(u)=0$ is identically zero at order 0 and 1 , while at order 2 becomes:

$$
\begin{aligned}
& \left(b_{6}+2 b_{5}\right)\left(p_{1} b_{6}+p_{2}\right)=0 \\
& \left(b_{5}+2 b_{6}\right)\left(p_{1} b_{5}+p_{2}\right)=0
\end{aligned}
$$

where

$$
\begin{aligned}
p_{1} & =529935346928 \\
p_{2} & =2^{1 / 3}(49+9 \sqrt{3})^{1 / 3}(207+16 \sqrt{3})^{2 / 3}(362080075 \sqrt{3}-711993501) \\
& \approx-1.63211356 \times 10^{10}
\end{aligned}
$$

These equations have the following four solutions:

$$
\begin{aligned}
& b_{5}=b_{6}=0 \\
& b_{5}=b_{6}=-p_{3} \\
& b_{5}=-p_{3}, \quad b_{6}=2 p_{3} \\
& b_{5}=2 p_{3}, \quad b_{6}=-p_{3}
\end{aligned}
$$

where $p_{3}=p_{1} / p_{2} \approx-32.46926929$. From this we find four approximate solutions of the form
$\left(\alpha+e b_{1}+\ldots, \alpha+e b_{2}+\ldots, \frac{\sqrt{3}}{3} \alpha+e b_{3}+\ldots, \alpha+e b_{4}+\ldots, \frac{\sqrt{3}}{3} \alpha+e b_{5}+\ldots, \frac{\sqrt{3}}{3} \alpha+e b_{6}+\ldots\right)$
where $b_{1}, \ldots, b_{4}$ can be computed from equations (5). These results seem to be compatible with the results obtained in  for the Dziobeck equations. Note that this analysis is local in nature, while our numerical results show that the branches of the bifurcation can be continued further see figure 3. The symmetry of the various branches is easy to detect numerically and is indicated in figure 3. The symmetry of the solutions can also be inferred theoretically from the symmetry of the equations, see for example the argument in $$.

# 5 The Case of Two Pairs of Equal Masses 

### 5.1 Equivariance

Recall that the Klein four-group is the group $\mathbb{Z}_{2} \times \mathbb{Z}_{2}$, the direct product of two copies of the cyclic group of order 2 . This group has four elements $\mathbb{Z}_{2} \times \mathbb{Z}_{2}=\left\{E, h_{1}, h_{2}, h_{3}\right\}$ with $h_{3}=h_{1} h_{2}$ and Cayley table

| $\circ$ | $E$ | $h_{1}$ | $h_{2}$ | $h_{3}$ |
| :--: | :--: | :--: | :--: | :--: |
| $E$ | $E$ | $h_{1}$ | $h_{2}$ | $h_{3}$ |
| $h_{1}$ | $h_{1}$ | $E$ | $h_{3}$ | $h_{2}$ |
| $h_{2}$ | $h_{2}$ | $h_{3}$ | $E$ | $h_{1}$ |
| $h_{3}$ | $h_{3}$ | $h_{2}$ | $h_{1}$ | $E$ |

where $E$ is the identity. The proper subgroups of the Klein four-group are $\{E\}$ (the trivial group), $\left\{E, h_{1}\right\},\left\{E, h_{2}\right\}$. Consider the four body with masses $m_{1}=m_{2}=1$ and $m_{3}=m_{4}=m$, and consider the action $\Psi$ of the Klein four-group on $\mathbb{R}^{8}$ defined by

$$
\begin{aligned}
& \Psi_{E}=e:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \\
& \Psi_{h_{1}}=\gamma_{1}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{12}, r_{23}, r_{24}, r_{13}, r_{14}, r_{34}\right) \\
& \Psi_{h_{2}}=\gamma_{2}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{12}, r_{14}, r_{13}, r_{24}, r_{23}, r_{34}\right) \\
& \Psi_{h_{3}}=\gamma_{3}:\left(\lambda_{0}, \mu, r_{12}, r_{13}, r_{14}, r_{23}, r_{24}, r_{34}\right) \rightarrow\left(\lambda_{0}, \mu, r_{12}, r_{24}, r_{23}, r_{14}, r_{13}, r_{34}\right)
\end{aligned}
$$

Then, for each fixed value of $m=m_{4}$ we can think of the Dziobeck equations as a map $F: \mathbb{R}^{8} \rightarrow \mathbb{R}^{8}$. A computation shows that this map is equivariant with respect to the action $\Psi$ for each value of $m$.

# 5.2 The global picture 

In this subsection we give an overview of the bifurcations we found in the case $m_{1}=m_{2}=1$ and $m_{3}=m_{4}=m$. The approach taken here is analogous to the approach taken in subsection 4.2, in particular the description presented here is based on numerical computations. Without loss of generality, we restrict our discussion to the case $0<m \leq 1$. We found that the Jacobian of the Dziobeck (and Albouy-Chenciner) equations vanishes along certain solutions for $m=\tilde{m}_{*} \approx 0.99229944 \ldots$ and $m=\tilde{m}_{* *} \approx 0.99729401 \ldots$ Each of these values of $m$ corresponds to a bifurcation.

At $m=\tilde{m}_{* *}$ there are two fold bifurcations. In this case, as $m$ is decreased through $\tilde{m}_{* *}$, four solutions coalesce to two. These solutions are illustrated in Figure 4.

At $m=\tilde{m}_{*}$ there are two supercritical pitchfork bifurcations, so that, when $m$ is decreased through $\tilde{m}_{*}$, six solutions coalesce to two. These solutions are illustrated in Figure 5.

The number of solutions to the Dziobeck and Albouy-Chenciner equations together with the number of geometrically distinct planar central configurations implied by our numerical computations is summarized in the following table

| Value of <br> $m_{3}=m_{4}$ | \# of solns <br> of Dziobek eqns | \# of solns <br> of AC eqns | \# of geometrically <br> different c.c's |
| :-- | :-- | :-- | :-- |
| $\left(0, \tilde{m}_{*}\right)$ | 11 | 24 | 23 |
| $\tilde{m}_{*}$ | 13 | 26 | 25 |
| $\left(\tilde{m}_{*}, \tilde{m}_{* *}\right]$ | 15 | 28 | 27 |
| $\left(\tilde{m}_{* *}, 1\right]$ | 19 | 32 | 31 |

# 5.3 Bifurcation at $m=\tilde{m}_{* *} \approx 0.99729401$ 

On the left we show two pairs of solutions for $m_{1}=m_{2}=m_{3}=$ $m_{4}=1$. These solutions are continued by increasing the parameter $m_{3}=$ $m_{4}=m$. Then, at $m=\tilde{m}_{* *} \approx 0.99729401 \ldots$, each pair of solution coalesce into one solution with a $\mathbb{Z}_{2} \cong\left\{E, h_{2}\right\}$ symmetry. This solution cannot be continued further, since we encounter a fold bifurcation.

We now use interval arithmetic to analyze one of the fold bifurcations at $m=\tilde{m}_{* *}$ (the one with $m_{1}$ in the convex hull formed by the other masses). Let $\tilde{F}=\left[\left(F_{1}, \ldots, F_{8}, \operatorname{det}(D F)\right]\right.$ be the vector having as components the Dziobeck equations and the determinant of the Jacobian matrix of $F$. Then we can use the Krawczyk operator to prove the existence of a (unique) solution $\left(\tilde{\mathbf{x}}_{* *}, \tilde{m}_{* *}\right)$ to the equation $\tilde{F}(\mathbf{x}, m)=0$ in a small box. Let $\left[\tilde{\mathbf{x}}_{* *}\right] \times\left[\tilde{m}_{* *}\right]$ be the box containing the solution $\left(\tilde{\mathbf{x}}_{* *}, \tilde{m}_{* *}\right)$.

Using as initial guess a value obtain using numerical computations we

obtain that

$$
\left[\widehat{\mathbf{x}}_{* *}\right]=\left[\begin{array}{c}
4.08429981829230230011485100912356858215517 ? \\
0.78045312314450202651992 ? \\
0.5737849085182166770049 ? \\
0.58001687737574791204967 ? \\
0.58001687737574791204967 ? \\
1.0069084529737404291463 ? \\
1.0069084529737404291463 ? \\
0.9886256052963805814736 ?
\end{array}\right]
$$

and $\left[\widehat{m}_{* *}\right]=0.997294013195487928197522256274082374264547$ ?. Suppose $A=D F\left(\left[\widehat{\mathbf{x}}_{* *}\right],\left[\widehat{m}_{* *}\right]\right)$. Computing the echelon form of $A$ using Gauss elimination it is possible to show rigorously that the null-space of $A$ is one dimensional. The eigenvectors of $A$ and $A^{T}$ corresponding to the zero eigenvalue are

$$
\mathbf{v}=\left[\begin{array}{c}
0 . ? \times 10^{-9} \\
-0.179026448 ? \\
2.989514215 ? \\
-0.5496816801 ? \\
-1.4331568126 ? \\
-0.5496816801 ? \\
-1.4331568126 ? \\
1
\end{array}\right], \quad \mathbf{w}=\left[\begin{array}{c}
0 . ? \times 10^{-17} \\
-0.23318293319421040 ? \\
0.990420115347107375 ? \\
-0.533270542375855490 ? \\
-0.533270542375855490 ? \\
-0.4619301897243832226 ? \\
-0.4619301897243832226 ? \\
1
\end{array}\right]
$$

respectively. Moreover we have that

$$
\begin{aligned}
& \mathbf{w}^{T} F_{m}\left(\left[\widehat{\mathbf{x}}_{* *}\right],\left[\widehat{m}_{* *}\right]\right)=6.32247017553985546 ? \\
& \mathbf{w}^{T}\left[D^{2} F\left(\left[\widehat{\mathbf{x}}_{* *}\right],\left[\widehat{m}_{* *}\right]\right)(\mathbf{v}, \mathbf{v})\right]=-227.08976277782379 ?
\end{aligned}
$$

and thus, since the interval obtained do not contain zero, by Theorem 2, the bifurcation occurring at $\left(\widehat{\mathbf{x}}_{* *}, \widehat{m}_{* *}\right)$ is a fold bifurcation.

# 5.4 Bifurcation at $m=\widehat{m}_{*} \approx 0.99229944$ 

We now use interval arithmetic to analyze one of the pitchfork bifurcations at $m=\widehat{m}_{*}$. Let $\tilde{F}=\left[\left(F_{1}, \ldots, F_{8}, \operatorname{det}(D F)\right]\right.$ be the vector having as components the Dziobeck equations and the determinant of the Jacobian matrix of $F$. To look for this bifurcation we can impose the symmetry $r_{13}=r_{23}$ and

On the left we show two groups of three solutions for $m_{1}=m_{2}=$ $m_{3}=m_{4}=1$. We continue these solutions by increasing the parameter $m_{3}=$ $m_{4}=m$. Then, at $m=\tilde{m}_{*} \approx 0.99229944 \ldots$, each group of solutions coalesce into one solution with a $\mathbb{Z}_{2}$ symmetry. These solutions can be continued further.

$r_{14}=r_{24}$. Let $G_{i}$ be equal to $F_{i}$ restricted to $r_{13}=r_{23}$ and $r_{14}=r_{24}$ and let $J$ be t he Jacobian of $F$ restricted to $r_{13}=r_{23}$ and $r_{14}=r_{24}$. Let $\tilde{G}=\left[\left(G_{1}, G_{2}, G_{3}, G_{6}, \operatorname{det}(J)\right]\left(\right.\right.$ since $G_{4}=G_{2}$ and $\left.G_{5}=G_{3}\right)$, then we can use the Krawczyk operator to prove the existence of a (unique) solution to the equation $\tilde{G}(\mathbf{y}, m)=0$, in a small box. This correspond to proving the existence of a unique symmetric solution $\left(\tilde{\mathbf{x}}_{*}, \tilde{m}_{*}\right)$ for the original equation $\tilde{F}\left(\mathbf{x}, m\right)=0$ in a small box. Let $\left[\tilde{\mathbf{x}}_{*}\right] \times\left[\tilde{m}_{*}\right]$ be the box containing the solution $\left(\tilde{\mathbf{x}}_{*}, \tilde{m}_{*}\right)$. Using as initial guess a value obtain using numerical computations we obtain that

$$
\left[\mathbf{x}_{*}\right]=\left[\begin{array}{c}
4.0585641815314330056739142 ? \\
0.7731895057295255894879076 ? \\
1.0130295438471170352477195 ? \\
0.57621036528654983921809171 ? \\
0.99527106304736638582196968 ? \\
0.57621036528654983921809171 ? \\
0.99527106304736638582196968 ? \\
0.58204027784245088387823969 ?
\end{array}\right]
$$

and $\left[\tilde{m}_{*}\right]=0.9922994477523853474498458$ ?. Suppose $A=D F\left(\left[\tilde{\mathbf{x}}_{*}\right],\left[\tilde{m}_{*}\right]\right)$. Computing the echelon form of $A$ using Gauss elimination it is possible to show rigourosly that the null-space of $A$ is one dimensional, since we know that at least one eigenvalue must be zero, but seven of the eight rows of the echelon form are clearly non-zero. From the echelon form of $A$ we find that the eigenvectors of $A$ and $A^{T}$ corresponding to the zero eigenvalue are
$\mathbf{v}=\left[\begin{array}{c}0 . ? \times 10^{-20} \\ 0 . ? \times 10^{-21} \\ 0 . ? \times 10^{-21} \\ 0 . ? \times 10^{-21}\end{array}\right] \quad \mathbf{w}=\left[\begin{array}{c}0 . ? \times 10^{-20} \\ 0 . ? \times 10^{-21} \\ 0 . ? \times 10^{-21} \\ 1.045364602949539555131 ? \\ -1.0000000000000000000000 ? \\ -1.0453646029495395551308 ? \\ 1 \\ 0\end{array}\right] \quad 1 \\
27
\end{array}\right]$

respectively. Moreover we have that

$$
\begin{aligned}
& \mathbf{w}^{T} F_{m}\left(\left[\tilde{\mathbf{x}}_{*}\right],\left[m_{*}\right]\right)=0 . ? \times 10^{-20} \\
& \mathbf{w}^{T}\left[D F_{m}\left(\left[\tilde{\mathbf{x}}_{*}\right],\left[\tilde{m}_{*}\right]\right) \mathbf{v}\right]=27.1877227151147526097 ? \\
& \mathbf{w}^{T}\left[D^{2} F\left(\left[\tilde{\mathbf{x}}_{*}\right],\left[\tilde{m}_{*}\right]\right)(\mathbf{v}, \mathbf{v})\right]=0 . ? \times 10^{-17} \\
& \mathbf{w}^{T}\left[D^{3} F\left(\left[\tilde{\mathbf{x}}_{*}\right],\left[\tilde{m}_{*}\right]\right)(\mathbf{v}, \mathbf{v}, \mathbf{v})\right]=-2639.9736664601674948 ?
\end{aligned}
$$

and thus, using the same argument used in Section 4.4, by Theorem 2 and Lemma 1, it follows that the bifurcation occurring at $\left(\mathbf{x}_{*}, m_{*}\right)$ is a pitchfork bifurcation. Since the last expression above is negative, again by Theorem 2 , the branches occur for $m>m_{*}$ and the bifurcation is supercritical.

# PLANAR $N$-BODY CENTRAL CONFIGURATIONS WITH A HOMOGENEOUS POTENTIAL 

#### Abstract

Central configurations give rise to self-similar solutions to the Newtonian $N$-body problem, and play important roles in understanding its complicated dynamics. Even the simple question of whether or not there are finitely many planar central configurations for $N$ positive masses remains unsolved in most cases. Considering central configurations as critical points of a function $f$, we explicitly compute the eigenvalues of the Hessian of $f$ for all $N$ for the point vortex potential for the regular polygon with equal masses. For homogeneous potentials including the Newtonian case we compute bounds on the eigenvalues for the regular polygon with equal masses, and give estimates on where bifurcations occur. These eigenvalue computations imply results on the Morse indices of $f$ for the regular polygon. Explicit formulae for the eigenvalues of the Hessian are also given for all central configurations of the equal mass 4 -body problem with a homogeneous potential. Classic results on collinear central configurations are also generalized to the homogeneous potential case. Numerical results, conjectures, and suggestions for future work in the context of a homogeneous potential are given.


## 1. InTRODUCTION

The classical dynamics of $N$ point particles with masses $m_{i}$ interacting via a central potential $U$ are given by:

$$
m_{i} \ddot{q}_{i ; j}=\frac{\partial U}{\partial q_{i ; j}}, \quad i \in\{0, \ldots N-1\}, \quad j \in\{1, \ldots, d\}
$$

where $q_{i} \in \mathbf{R}^{d}$ is the position of particle $i$ with components $q_{i ; j}$, and

$$
U=\sum_{i<k} m_{i} m_{k} / r_{i, k}^{A-2}
$$

is the potential with a real parameter $A>2$, and $r_{i, k}$ is the distance between $q_{i}$ and $q_{k}$. The case of Newtonian gravity is $A=3$ , and provides the primary motivation for studying this more general problem. We can extend this potential to the case $A=2$ by using the logarithmic potential

$$
U=\sum_{i<k} m_{i} m_{k} \log \left(r_{i, k}\right)
$$

which arises in a simplified model of fluid vortices $$. In the vortex model case the parameters $m_{i}$ represent the strength of a vortex rotation, and can be any

real value. However our main interest is the Newtonian case, for which we usually assume non-negative mass parameters.

In this article we focus our attention on configurations with the special property that each particle is accelerated towards the center of mass of the system at a rate uniformly proportional to its distance from the center of mass, i.e.

$$
m_{i} \ddot{q}_{i ; j}=\lambda\left(q_{i ; j}-q_{C ; j}\right)
$$

with $q_{C}=\frac{1}{M} \sum m_{i} q_{i}$ the center of mass, and $M=\sum m_{i}$ is the total mass. Such configurations are called central configurations (as well as permanent or stationary configurations in some older literature). In the planar case they also account for the relative equilibria, which are equilibria in a uniformly rotating reference frame. Central configurations are important in the $N$-body problem for a number of reasons, including the study of multiple body collisions  and the topology of the phase space for a fixed energy $$. Understanding of the dynamics near central configurations was critical in the proof of chaotic behavior in the three-body problem .

For more background on central configurations we highly recommend the recent summary by Moeckel , as well as earlier surveys .

A longstanding open problem about central configurations is whether or not there are finitely many equivalence classes of central configurations for a particular choice of $N$ positive masses (usually restricted to the Newtonian case of $A=3$ ). The most famous version of this problem further restricts the configurations to $\mathbf{R}^{2}$, and was highlighted by Stephen Smale as the sixth of his 'Mathematical problems for the next century' . Smale himself considered the problem , and introduced a topological viewpoint that we will consider in the next section. This problem was also formulated earlier by Wintner  and Chazy , and highlighted more recently in . We follow the usual convention of considering two planar configurations equivalent if there is a direct isometry between them (i.e. an orientation-preserving rigid motion).

The difficulty of the finiteness problem was underscored by the discovery of a counter-example in the 5 -body problem if a negative mass is allowed . This example has been extended to more general settings . The existence of positive dimensional sets of central configurations for some negative mass parameters makes many approaches using algebraic geometry challenging, since methods based on complex varieties are incapable of ruling these out. Indeed, although there have been numerous successful applications of methods from classical and real algebraic geometry and tropical geometry to the finiteness problem , we believe that solving the finiteness problem in general requires additional tools.

The primary hypothesis of this manuscript is that studying the central configurations for a homogeneous potential (more general than the Newtonian) will more naturally develop mathematical tools that will advance the Newtonian case, analogously to the use of tools from complex analysis in solving real-analytic problems

(e.g. contour integrals). In particular we believe it would be valuable to develop a framework for central configurations in the limiting case of $A \rightarrow \infty$.

In what follows we consider central configurations as critical points of the function

$$
f=\frac{M I}{2}+\frac{U}{A-2}
$$

where $I$ is the moment of inertia

$$
I=\sum_{i=1}^{N} m_{i} r_{i}^{2}
$$

where $r_{i}=\left|q_{i}\right|$ is the distance from the $i$ th point to the origin. If the center of mass is at the origin, then

$$
I=\frac{1}{M} \sum_{i<j} m_{i} m_{j} r_{i, j}^{2}
$$

Because the potential function $U$ is invariant under translation, all critical points of $f$ will have their center of mass at the origin. In contrast to some other formulations of central configurations, our $f$ is homogeneous in the mass parameters but not in the distance variables. We have in effect set a preferred scale from the beginning in order to have an unconstrained problem. We find this approach simplest, but there are many other formulations of the problem .

The idea of studying a more general potential, even if we are mainly interested in the Newtonian case, is an old one . We would like to especially highlight the study of the behavior of central configurations for large values of $A$, which has not recieved much attention in the literature before.

We briefly review the relevant topology for using Morse theory in the $N$-body problem.

The configuration space we will use is $\mathcal{C}_{N}=\left(\mathbb{R}^{2 N} \backslash \Delta\right) / S^{1}$, where $\Delta$ is the subset of collisions ( $q_{i}=q_{j}$ for $i \neq j$ ) and the quotient is taken with respect to proper rotations around the origin treating $\mathbb{R}^{2 N}$ as $\left(\mathbb{R}^{2}\right)^{N}$. The function $f$ is well-defined on this quotient since both $I$ and $U$ are rotationally invariant.

The simplest versions of Morse theory concern the behavior of a smooth function on a compact manifold, with the extra condition that the critical points of the function are nondegenerate (i.e. the Hessian is nondegenerate). Although our function $f$ is not defined on a compact manifold (because of the removal of the set $\Delta$ ), this can be remedied without too much effort because the gradient of $f$ will always become outward pointing close to $\Delta$. This was made precise by Shub . Assuming $f$ is nondegenerate, its level sets change in topology at each critical value. If the topology of the manifold is non-trivial, such changes in the level sets are inevitable. The index of a critical point is the dimension of the largest subspace on which the Hessian of $f$ is negative definite. Let the number of critical points with index $j$ be $n_{j}$, and encode this information in the Morse polynomial:

$$
M(t)=\sum_{j=0}^{\operatorname{dim}\left(\mathcal{C}_{N}\right)} n_{j} t^{j}
$$

where $t$ is an auxiliary variable. The Poincaré polynomial for a manifold is defined as $P(t)=\sum \beta_{j} t^{j}$, where $\beta_{j}$ is the $j$ th Betti number. Morse theory relates these polynomials by

$$
M(t)=P(t)+(1+t) R(t)
$$

where $R(t)$ is a polynomial with non-negative integer coefficients. This not only puts a lower bound on the number of critical points, but also provides constraints on the possible $n_{j}$.

For more background on Morse theory we recommend .
The Poincaré polynomial for the manifold $\mathcal{C}_{N}$ is $P_{N}(t)=\prod_{j=1}^{N-1}(1+j t)$ . The corresponding result in the spatial case was first computed in ; in dimension $d$, $P_{N, d}(t)=\prod_{j=1}^{N-1}\left(1+j t^{d-1}\right)$ .

It is not completely clear how much the index of a critical point influences the more general dynamical behavior of orbits near the central configuration, although there are some results connecting these . Not many cases of exact calculations of linear stability are available. The general problem was made precise by Andoyer . Particular cases have been studied for three bodies , four bodies , restricted cases (i.e. with one or more infinitesimal masses) , and polygonal and $N+1$ ring systems ; more could be done, especially numerically, in our setting of a variable exponent potential. A particularly interesting example is the lower bound for instability of equal mass relative equilbria found by Roberts  in the Newtonian case.

A recent result of Montaldi  uses only the existence of a minimum of $f$ to derive the existence of a large family of symmetric central configurations; in many settings this result could be strengthened using Morse theory (assuming the function $f$ is non-degenerate). The existing upper and lower bounds for central configurations are far from sharp, despite some substantial effort $$.

# 2. The regular polygon in the N-body PROblem 

We can prove some properties of the Morse index of central configurations for the regular polygon in the $N$-body problem for varying $A$, and speculate on some others. Quite a few results for regular polygon central configurations are known for the Newtonian $(A=3)$ and vortex $(A=2)$ cases $$.

These configurations are well suited to polar coordinates, so we will express the position of the $i$ th particle as

$$
q_{i}=\left(r_{i} \cos \left(\theta_{i}\right), r_{i} \sin \left(\theta_{i}\right)\right)
$$

For the regular polygon centered at the origin, all of the radii are equal ( $r_{i}=r$ for some $r)$ and $\theta_{i}=\frac{2 \pi i}{N}$ where we will index the particles starting at $i=0$. In what follows we

denote the evaluation of a function at the equal mass regular polygon by a superscript circle, e.g. $f^{\circ}$. For the interparticles distances we define $p_{i, j}=r u_{i, j}=\left(r_{i, j}\right)^{\circ}$, where

$$
u_{i, j}=\sqrt{2-2 \cos \left[\frac{2 \pi(j-i)}{N}\right]}=2 \sin \left(\frac{\pi|j-i|}{N}\right)
$$

are the distances between points $i$ and $j$ on the unit radius regular polygon.
As before we consider central configurations as critical points of the function $f=$ $\frac{M I}{2}+\frac{U}{A-2}$. To calculate derivatives of $f$ we will need the partial derivatives of the interparticle distances with respect to $r_{i}$ and $\theta_{i}$ :

$$
\begin{aligned}
& \frac{\partial r_{i, j}}{\partial r_{i}}=\frac{r_{i}-r_{j} \cos \left(\theta_{j}-\theta_{i}\right)}{r_{i, j}} \\
& \frac{\partial r_{i, j}}{\partial \theta_{i}}=\frac{-r_{i} r_{j} \sin \left(\theta_{j}-\theta_{i}\right)}{r_{i, j}}
\end{aligned}
$$

Evaluated on the regular polygon, we have

$$
\begin{gathered}
\left(\frac{\partial r_{i, j}}{\partial r_{i}}\right)^{\circ}=\frac{1-\cos \left(\theta_{j}-\theta_{i}\right)}{u_{i, j}}=u_{i, j} / 2 \\
\left(\frac{\partial r_{i, j}}{\partial \theta_{i}}\right)^{\circ}=-r \frac{\sin \left(\theta_{j}-\theta_{i}\right)}{u_{i, j}}=-r \cos \left(\frac{\pi|j-i|}{N}\right)
\end{gathered}
$$

The gradient of $f$ with respect to $r_{i}$ and $\theta_{i}$ has components

$$
\frac{\partial f}{\partial r_{i}}=m_{i} M r_{i}-m_{i} \sum_{j \neq i} m_{j} r_{i, j}^{-A}\left(r_{i}-r_{j} \cos \left(\theta_{j}-\theta_{i}\right)\right)
$$

and

$$
\frac{\partial f}{\partial \theta_{i}}=m_{i} \sum_{j \neq i} m_{j} r_{i, j}^{-A} r_{i} r_{j} \sin \left(\theta_{j}-\theta_{i}\right)
$$

Evaluated at the equal mass regular polygon these are

$$
\begin{gathered}
\left(\frac{\partial f}{\partial r_{i}}\right)^{\circ}=N r-r \sum_{j \neq i} p_{i, j}^{-A}\left(1-\cos \left(\theta_{j}-\theta_{i}\right)\right) \\
\left(\frac{\partial f}{\partial \theta_{i}}\right)^{\circ}=r^{2} \sum_{j \neq i} p_{i, j}^{-A} \sin \left(\theta_{j}-\theta_{i}\right)=0
\end{gathered}
$$

where the second quantity is zero because $\sin (t)$ is odd and $p_{i, j}$ is even.
To be a critical point of $f,\left(\frac{\partial f}{\partial r_{0}}\right)^{\circ}=0$, which can be solved for the radius:

$$
r=\left(\frac{\sum_{j=1}^{N-1} u_{0, j}^{2-A}}{2 N}\right)^{1 / A}
$$

As $A$ increases, this radius increases to the limit value $r_{\infty}(N)=(2 \sin (\pi / N))^{-1}$, for which $p_{i, i+1}=1$. For $A=2$, the radius is equal to $\sqrt{\frac{N-1}{2 N}}$.

Now to compute the Morse index of $f$ for regular polygons we need the components of the Hessian of $f$. In expressions involving indices $i$ and $j$, it is assumed that $i \neq j$. In the final form shown for each expression we use the radius $r$ and unit polygon distances $u_{i, j}$ as much as possible.

$$
\begin{gathered}
\frac{\partial^{2} f}{\partial r_{i} \partial r_{j}}=m_{i} m_{j} r_{i, j}^{-A-2}\left(A\left(r_{i}-r_{j} \cos \left(\theta_{j}-\theta_{i}\right)\right)\left(r_{j}-r_{i} \cos \left(\theta_{j}-\theta_{i}\right)\right)+r_{i, j}^{2} \cos \left(\theta_{j}-\theta_{i}\right)\right) \\
R_{i, j}:=\left(\frac{\partial^{2} f}{\partial r_{i} \partial r_{j}}\right)^{\circ}=p_{i, j}^{-A}\left[\frac{A}{2}\left(1-\cos \left(\frac{2 \pi(j-i)}{N}\right)\right)+\cos \left(\frac{2 \pi(j-i)}{N}\right)\right]
\end{gathered}
$$

which simplifies to

$$
\begin{gathered}
R_{i, j}=r^{-A} u_{i, j}^{-A}\left(u_{i, j}^{2} \frac{A-2}{4}+1\right) \\
\frac{\partial^{2} f}{\partial r_{i}^{2}}=m_{i}\left(M-\sum_{j \neq i} m_{j} r_{i, j}^{-A-2}\left[r_{i, j}^{2}-A\left(r_{i}-r_{j} \cos \left(\theta_{j}-\theta_{i}\right)\right)^{2}\right]\right) \\
R_{i, i}:=\left(\frac{\partial^{2} f}{\partial r_{i}^{2}}\right)^{\circ}=N-\sum_{j \neq i} p_{i, j}^{-A}\left(1-\frac{A p_{i, j}^{2}}{4 r^{2}}\right)
\end{gathered}
$$

or

$$
R_{i, i}=N\left(1+\frac{A}{2}-2 \frac{\sum_{j \neq i} u_{i, j}^{-A}}{\sum_{j \neq i} u_{i, j}^{-A+2}}\right)=r^{-A} \sum_{j \neq i} u_{i, j}^{-A}\left(u_{i, j}^{2}\left(\frac{A}{4}+\frac{1}{2}\right)-1\right)
$$

(for these identities we use the explicit formula for the radius $r$, e.g. to rewrite $\left.N=r^{-A} \sum_{j=1}^{N-1} u_{0, j}^{2-A} / 2\right)$.

$$
\begin{gathered}
\frac{\partial^{2} f}{\partial r_{i} \partial \theta_{j}}=-m_{i} m_{j} r_{i, j}^{-A-2} r_{j} \sin \left(\theta_{j}-\theta_{i}\right)\left[r_{i, j}^{2}-A r_{i}\left(r_{i}-r_{j} \cos \left(\theta_{j}-\theta_{i}\right)\right)\right] \\
W_{i, j}:=\left(\frac{\partial^{2} f}{\partial r_{i} \partial \theta_{j}}\right)^{\circ}=p_{i, j}^{-A} r \sin \left(\frac{2 \pi(j-i)}{N}\right)\left(\frac{A}{2}-1\right)
\end{gathered}
$$

or equivalently

$$
\begin{gathered}
W_{i, j}=r^{-A+1}\left(\frac{A}{2}-1\right) u_{i, j}^{-A+1} \sqrt{1-\frac{u_{i, j}^{2}}{4}} \\
\frac{\partial^{2} f}{\partial r_{i} \partial \theta_{i}}=m_{i} \sum_{j \neq i} m_{j} r_{i, j}^{-A-2} r_{j} \sin \left(\theta_{j}-\theta_{i}\right)\left[-A r_{i}\left(r_{i}-r_{j} \cos \left(\theta_{j}-\theta_{i}\right)\right)+r_{i, j}^{2}\right] \\
W_{i, i}:=\left(\frac{\partial^{2} f}{\partial r_{i} \partial \theta_{i}}\right)^{\circ}=\sum_{j \neq i} p_{i, j}^{-A} r \sin \left(\frac{2 \pi(j-i)}{N}\right)(1-A / 2)=0
\end{gathered}
$$

$$
\begin{gathered}
\frac{\partial^{2} f}{\partial \theta_{i} \partial \theta_{j}}=m_{i} m_{j} r_{i, j}^{-A-2} r_{i} r_{j}\left[-A r_{i} r_{j} \sin ^{2}\left(\theta_{j}-\theta_{i}\right)+r_{i, j}^{2} \cos \left(\theta_{j}-\theta_{i}\right)\right] \\
T_{i, j}:=\left(\frac{\partial^{2} f}{\partial \theta_{j} \partial \theta_{i}}\right)^{\circ}=r^{2} p_{i, j}^{-A-2}\left[-A r^{2} \sin ^{2}\left(\frac{2 \pi(j-i)}{N}\right)+p_{i, j}^{2} \cos \left(\frac{2 \pi(j-i)}{N}\right)\right] \\
=r^{-A+2} u_{i, j}^{-A}\left[-A\left(1-\frac{u_{i, j}^{2}}{4}\right)+\left(1-\frac{u_{i, j}^{2}}{2}\right)\right] \\
\frac{\partial^{2} f}{\partial \theta_{i}^{2}}=m_{i} \sum_{j \neq i} m_{j} r_{i} r_{j} r_{i, j}^{-A-2}\left[A r_{i} r_{j} \sin ^{2}\left(\theta_{j}-\theta_{i}\right)-r_{i, j}^{2} \cos \left(\theta_{j}-\theta_{i}\right)\right] \\
T_{i, i}:=\left(\frac{\partial^{2} f}{\partial \theta_{i}^{2}}\right)^{\circ}=\sum_{j \neq i} r^{2} p_{i, j}^{-A-2}\left[A r^{2} \sin ^{2}\left(\frac{2 \pi(j-i)}{N}\right)-p_{i, j}^{2} \cos \left(\frac{2 \pi(j-i)}{N}\right)\right]=-\sum_{j \neq i} T_{i, j}
\end{gathered}
$$

In terms of these newly defined quantities, with respect to the variables $\left(r_{0}, r_{1}, \ldots r_{N-1}\right.$, $\theta_{0}, \theta_{1}, \ldots \theta_{N-1}$ ), the Hessian is

$$
D^{2} f^{\circ}=\left(\begin{array}{c|c}
R & W \\
\hline-W & T
\end{array}\right)
$$

In a similar way to that in , we can exploit the circulant structure of the Hessian submatrices to compute its eigenvalues. The submatrices $R$ and $T$ are circulant and symmetric, while $W$ is circulant and anti-symmetric. Let $C$ be the $N$ by $N$ matrix with $C_{i, j}=e^{2 \mathrm{i} i j / n}$, where $\mathbb{I}=\sqrt{-1}$, and $i, j \in\{0, \ldots, N-1\}$. This matrix $C$ orthogonally diagonalizes any circulant matrix of the same dimension. Thus we have

$$
H=\left(\begin{array}{c|c}
C^{-1} & 0 \\
\hline 0 & C^{-1}
\end{array}\right)\left(\begin{array}{c|c}
R & W \\
\hline-W & T
\end{array}\right)\left(\begin{array}{c|c}
C & 0 \\
\hline 0 & C
\end{array}\right)=\left(\begin{array}{c|c}
P & S \\
\hline-S & Q
\end{array}\right)
$$

in which the subblocks of $H$ are all diagonal, $P$ and $Q$ are real, and $S$ is purely imaginary. We can express the entries of $P, Q$, and $S$ in terms of the first rows of $R$, $T$, and $W$ respectively:

$$
\begin{gathered}
P_{i, i}=\sum_{j=0}^{N-1} R_{0, j} C_{j, i} \\
=R_{0,0}+\sum_{j=1}^{\lfloor(N-1) / 2\rfloor} 2 \cos \left(\frac{2 \pi i j}{N}\right) R_{0, j}+ \begin{cases}0 \text { for } N \text { odd } \\
(-1)^{i}(2 r)^{-A}(A-1) \text { for } N \text { even }\end{cases}
\end{gathered}
$$

or more explicitly

$$
\begin{aligned}
P_{i, i}= & r^{-A} \sum_{j=1}^{\lfloor(N-1) / 2\rfloor} u_{0, j}^{-A}\left(u_{0, j}^{2}\left[\frac{A}{2}+1+\left(\frac{A}{2}-1\right) \cos \left(\frac{2 \pi i j}{N}\right)\right]-2+2 \cos \left(\frac{2 \pi i j}{N}\right)\right) \\
& + \begin{cases}0 \text { for } N \text { odd } \\
(2 r)^{-A}((-1)^{i}(A-1)+(A+1)) \text { for } N \text { even }\end{cases} \\
Q_{i, i}= & \sum_{j=0}^{N-1} T_{0, j} C_{j, i}=T_{0,0}+\sum_{j=1}^{\lfloor(N-1) / 2\rfloor} 2 \cos \left(\frac{2 \pi i j}{N}\right) T_{0, j}+ \begin{cases}0 \text { for } N \text { odd } \\
(-1)^{i} r^{2}(2 r)^{-A} \text { for } N \text { even }\end{cases}
\end{aligned}
$$

which can be written as

$$
Q_{i, i}=2 r^{-A+2} \sum_{j=1}^{\lfloor(N-1) / 2\rfloor} u_{0, j}^{-A}\left(1-\cos \left(\frac{2 \pi i j}{N}\right)\right)\left(\frac{A-2}{2}\left(1+\cos \left(\frac{2 \pi j}{N}\right)\right)+1\right)
$$

The latter form of $Q_{i, i}$ makes it clear that $Q_{i, i}>0$ for $A \geq 2$ (each term of the sum is non-negative).

Finally

$$
S_{i, i}=\sum_{j=0}^{N-1} W_{0, j} C_{j, i}=\mathbb{I} \sum_{j=1}^{\lfloor(N-1) / 2\rfloor} 2 \sin \left(\frac{2 \pi i j}{N}\right) W_{0, j}
$$

so

$$
S_{i, i}=2 r^{-A+1} \frac{A-2}{2} \mathbb{I} \sum_{j=1}^{\lfloor(N-1) / 2\rfloor} \sin \left(\frac{2 \pi i j}{N}\right) \sin \left(\frac{2 \pi j}{N}\right) u_{0, j}^{-A}
$$

where $\mathbb{I}=\sqrt{-1}$.
Now we can compute the eigenvalues of the Hessian of $f$ in pairs from the two by two matrices

$$
E_{i}=\left(\begin{array}{c|c}
P_{i, i} & S_{i, i} \\
\hline-S_{i, i} & Q_{i, i}
\end{array}\right)
$$

We will denote the two eigenvalues of this block by

$$
\lambda_{(N, i, \pm)}=\frac{1}{2}\left(P_{i, i}+Q_{i, i} \pm \sqrt{\left(P_{i, i}-Q_{i, i}\right)^{2}-4 S_{i, t}^{2}}\right)
$$

2.1. The regular polygon in the vortex case. Now we consider the regular polygon configurations, starting with the extreme case of $A=2$.

Theorem 1. For $A=2,\left.Q_{i, i}\right|_{A=2}=\left\lfloor\frac{i}{2} N-\frac{i^{2}}{2}\right\rfloor$.

Proof. We will prove this by induction on $i$. First note that we can specialize equation (2) for $A=2$ to

$$
\left.Q_{i, i}\right|_{A=2}=\sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} \frac{1-\cos \left(\frac{2 \pi i j}{N}\right)}{1-\cos \left(\frac{2 \pi j}{N}\right)}
$$

The base cases we need are for $i \in\{0,1,2,3\}$. The first two:

$$
\begin{gathered}
\left.Q_{0,0}\right|_{A=2}=0 \\
\left.Q_{1,1}\right|_{A=2}=\left\lfloor\frac{N-1}{2}\right\rfloor
\end{gathered}
$$

follow directly from (5). For $i=2$ and $i=3$ we rewrite the numerator in terms of $\cos \left(\frac{2 \pi j}{N}\right)$, and in each case the denominator appears as a factor we can cancel.

$$
\begin{aligned}
\left.Q_{2,2}\right|_{A=2} & =\sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} \frac{1-\cos \left(\frac{4 \pi j}{N}\right)}{1-\cos \left(\frac{2 \pi j}{N}\right)}=\sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} \frac{2-2 \cos \left(\frac{2 \pi j}{N}\right)^{2}}{1-\cos \left(\frac{2 \pi j}{N}\right)} \\
& =2 \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor}\left(1+\cos \left(\frac{2 \pi j}{N}\right)\right)=N-2 \\
\left.Q_{3,3}\right|_{A=2}= & \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} \frac{1-\cos \left(\frac{6 \pi j}{N}\right)}{1-\cos \left(\frac{2 \pi j}{N}\right)}=\sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor}\left(1+2 \cos \left(\frac{2 \pi j}{N}\right)\right)^{2}=\left\lfloor\frac{3 N-9}{2}\right\rfloor
\end{aligned}
$$

The final form in each of the above cases can be summed using standard properties of Chebyshev polynomials. We will briefly review some of the properties of Chebyshev polynomials used there and in what follows. We define $T_{j}(\cos (\theta))=\cos (j \theta)$, and $U_{j}(\cos (\theta)) \sin (\theta)=\sin ((j+1) \theta)$. The polynomials $T_{j}$ and $U_{j}$ satisfy many known relations including the composition formula $T_{j}\left(T_{k}(\theta)\right)=T_{j k}(\theta)$, and the summation formulae

$$
\begin{aligned}
& \sum_{j=0}^{m} T_{2 j+1}(x)=\frac{U_{2 m+1}(x)}{2} \\
& \sum_{j=0}^{m} T_{2 j}(x)=\frac{U_{2 m}(x)+1}{2}
\end{aligned}
$$

For the induction step we consider the double difference

$$
D_{i}=\left(Q_{i+2, i+2}-Q_{i, i}\right)-\left(Q_{i, i}-Q_{i-2, i-2}\right)=Q_{i+2, i+2}-2 Q_{i, i}+Q_{i-2, i-2}
$$

After writing all the cosines in terms of $\cos \left(\frac{2 \pi j}{N}\right)$, we can eventually simplify $D_{i}$ to

$$
D_{i}=4 \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor}\left(1+\cos \left(\frac{2 \pi j}{N}\right)\right) T_{i}\left(\cos \left(\frac{2 \pi j}{N}\right)\right)=-4
$$

Now we can conclude the induction; assume that $\left.Q_{i, i}\right|_{A=2}=\left\lfloor\frac{i}{2} N-\frac{i^{2}}{2}\right\rfloor$ for $i<j+2$. Then

$$
\begin{gathered}
\left.Q_{j+2, j+2}\right|_{A=2}=\left.2 Q_{j, j}\right|_{A=2}-\left.Q_{j-2, j-2}\right|_{A=2} \\
=2\left\lfloor\frac{j}{2} N-\frac{j^{2}}{2}\right\rfloor-\left\lfloor\frac{j-2}{2} N-\frac{(j-2)^{2}}{2}\right\rfloor-4=\left\lfloor\frac{j+2}{2} N-\frac{(j+2)^{2}}{2}\right\rfloor
\end{gathered}
$$

Theorem 2. For $A=2$,

$$
\left.P_{i, i}\right|_{A=2}=(2-i) N+\frac{\left(i^{2}-i\right) N}{N-1}
$$

Proof. From (1) we have

$$
\begin{aligned}
& \left.P_{i, i}\right|_{A=2}=r^{-2} \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} u_{0, j}^{-2}\left(2 u_{0, j}^{2}-2+2 \cos \left(\frac{2 \pi i j}{N}\right)\right)+\left\{\begin{array}{c}
0 \text { for } N \text { odd } \\
(2 r)^{-2}\left((-1)^{i}+3\right) \text { for } N
\end{array} \text { even }\right. \\
& =\left(\frac{2 N}{N-1}\right)\left[\sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor}\left(2-\frac{1-\cos \left(\frac{2 \pi i j}{N}\right)}{1-\cos \left(\frac{2 \pi j}{N}\right)}\right)+\left\{\begin{array}{c}
0 \text { for } N \text { odd } \\
\left((-1)^{i}+3\right) / 4 \text { for } N
\end{array} \text { even }\right] \\
& =\left(\frac{2 N}{N-1}\right)\left[2\left\lfloor\frac{N-1}{2}\right\rfloor-Q_{i, i}+\left\{\begin{array}{c}
0 \text { for } N \text { odd } \\
\left((-1)^{i}+3\right) / 4 \text { for } N
\end{array} \text { even }\right]
\end{aligned}
$$

and the result follows easily from the previous theorem once we consider all the particular cases of $N$ and $i$ being odd or even.

So it becomes possible to completely determine the eigenvalues of the Hessian for the regular polygon configuration in the vortex case.

Theorem 3. The eigenvalues of the Hessian of $f$ in the case $A=2$ are $(2-i) N+$ $\frac{\left(i^{2}-i\right) N}{N-1}$ and $\left\lfloor\frac{i}{2} N-\frac{i^{2}}{2}\right\rfloor$ for $0 \leq i \leq N-1$. In the quotient configuration space $\mathcal{C}_{N}$, the regular polygon has Morse index of 0 for $N \in\{3,4,5,6\}$, it is degenerate for $N=7$, and has a Morse index of $N-5$ for $N \geq 8$.

Proof. It is immediate from the general formula (3) for $S_{i, i}$ that $\left.S_{i, i}\right|_{A=2}=0$, so the eigenvalues of the Hessian are simply $\left.Q_{i, i}\right|_{A=2}$ and $\left.P_{i, i}\right|_{A=2}$ as given in the previous theorems. The remainder of the theorem follows from considering the sign of these expressions: since the eigenspace blocks are orthogonal the Morse index is simply the number of negative eigenvalues of all the blocks.

The fact that the heptagon has a degenerate Hessian in the vortex case is interesting in comparison to the dynamical stability results in , in which the heptagon was also a degenerate case.

2.2. The regular polygon for $A>2$. Now we prove a theorem characterizing the Morse index of the regular polygon for larger values of $A$. A previous related result specialized to the Newtonian $(A=3)$ case is that the regular $N$-gon does not have index 0 for $N \geq 6$.

Lemma 1. For $N \geq 2$,

$$
\begin{gathered}
\lambda_{(N, 0,+)}>N A, \quad \lambda_{(N, 0,-)}=0 \\
\text { and } \quad \lambda_{(N, 1, \pm)}>0
\end{gathered}
$$

Proof. The result for $i=0$ follows immediately from our expressions for $P_{0,0}, Q_{0,0}$, and $S_{0,0}$.

For $i=1$, we can calculate the determinant

$$
\begin{aligned}
P_{1,1} Q_{1,1}+S_{1,1}^{2}= & r^{-2 A+2} \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor}\left\lvert\, \sum_{k=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} u_{0, j}^{-A} u_{0, k}^{-A}\left(1-\cos \left(\frac{2 \pi j}{N}\right)\right)\left(1-\cos \left(\frac{2 \pi k}{N}\right)\right)\{ \\
& (A-2)^{2}\left(\cos \left(\frac{2 \pi j}{N}\right)-\cos \left(\frac{2 \pi k}{N}\right)\right)\left(\cos \left(\frac{2 \pi j}{N}\right)+1\right) \\
& +4(A-2)\left(\cos \left(\frac{2 \pi j}{N}\right)+1\right)+4\}
\end{aligned}
$$

and we see the coefficients of $(A-2)^{2}$ will cancel out (under the interchange of $j$ and $k$ ), and the remaining terms are positive. Thus the two eigenvalues are either both negative or both positive. The trace can be simplified into a form that makes it clearly positive:
$P_{1,1}+Q_{1,1}=r^{-A}\left(r^{2}+2\right) \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} u_{0, j}^{-A}\left(1-\cos \left(\frac{2 \pi j}{N}\right)\right)\left((A-2)\left(1+\cos \left(\frac{2 \pi j}{N}\right)\right)+2\right)$
so the two eigenvalues of the $i=1$ block must be positive.
For $i \in\{1, \ldots N-1\}, \lambda_{(N, i, \pm)}=\lambda_{(N, N-i, \pm)}$ for each sign choice and so we can restrict our attention to $1 \leq i \leq\left\lfloor\frac{N}{2}\right\rfloor$. Apart from the special cases of small $N$, it turns out that the interesting eigenvalue of the Hessian is always $\lambda_{(N, 2,-)}$ (which equals $\lambda_{(N, N-2,-)}$.
Theorem 4. For each $N \geq 5$ there is a value of $A=A_{N}$, and $i \in\left\{1, \ldots\left\lfloor\frac{N}{2}\right\rfloor\right\}$, such that the eigenvalues of the Hessian of $f$ for the equal-mass regular polygon satisfy

$$
\lambda_{(N, i,+)}>0
$$

and

$$
\lambda_{(N, i,-)}>0 \text { for } i<2, \quad \lambda_{(N, i,-)}<0 \text { for } i \geq 2
$$

for all $A>A_{N}$ so the Morse index of $f$ for the regular polygon on the quotient configuration space $\mathcal{C}_{N}$ is $N-3$ for $A>A_{N}$.

Proof. For the purposes of the Morse index we only need to determine the sign of the eigenvalues of the Hessian of $f$, so for each two by two block $E_{i}$ (cf. Eq. (4)) we need to know the sign of $P_{i, i} Q_{i, i}+S_{i, i}^{2}$. If this is negative then the eigenvalues will have opposite signs. So we examine the terms of the sums in our expression for $P_{i, j} Q_{i, i}+S_{i, i}^{2}$.

In order to make the following rather large expressions more managable we use the notations $\theta=\frac{2 \pi}{N}, c_{i}=\cos (i \theta)$, and $s_{i}=\sin (i \theta)$; it will also be convenient to use $B=A-2$ as well as $A$ because of the structure of $S_{i, i}^{2}$. With these we have:

$$
\begin{aligned}
P_{i, i} Q_{i, i}+S_{i, i}^{2}= & -r^{-2 A+2} \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor}\sum_{k=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} u_{0, j}^{-A} u_{0, k}^{-A}\left\{4\left(1-u_{0, j}^{2}-c_{i j}\right)\left(1-c_{i k}\right)\right. \\
& +B\left(1-c_{i k}\right)\left(u_{0, j}^{2} u_{0, k}^{2}-c_{i j} u_{0, j}^{2}+c_{i j} u_{0, k}^{2}-5 u_{0, j}^{2}-u_{0, k}^{2}-4 c_{i j}+4\right) \\
& +\frac{B^{2}}{4}\left(4 s_{i j} s_{i k} s_{j} s_{k}-c_{i j} c_{i k} u_{0, j}^{2} u_{0, k}^{2}+c_{i j} u_{0, j}^{2} u_{0, k}^{2}-c_{i k} u_{0, j}^{2} u_{0, k}^{2}\right. \\
& \left.+4 c_{i j} c_{i k} u_{0, j}^{2}+u_{0, j}^{2} u_{0, k}^{2}-4 c_{i j} u_{0, j}^{2}+4 c_{i k} u_{0, j}^{2}-4 u_{0, j}^{2}\right)\}
\end{aligned}
$$

which fortunately simplifies a little after using the fact that $u_{0, j}^{2}=2-2 \cos (j \theta)=$ $2-2 c_{j}:$

$$
\begin{aligned}
P_{i, i} Q_{i, i}+S_{i, i}^{2}= & -r^{-2 A+2} \sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} \sum_{k=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} u_{0, j}^{-A} u_{0, k}^{-A}\left\{-4\left(1-c_{i k}\right)\left(1+c_{i j}-2 c_{j}\right)\right. \\
& +2 B\left(1-c_{i k}\right)\left(c_{i j} c_{j}-c_{i j} c_{k}+2 c_{j} c_{k}-2 c_{i j}+3 c_{j}-c_{k}-2\right) \\
& \left.+B^{2}\left(s_{i j} s_{i k} s_{j} s_{k}-\left(1+c_{i j}\right)\left(1-c_{i k}\right)\left(1-c_{j}\right)\left(1+c_{k}\right)\right)\right\}
\end{aligned}
$$

Next we separate out the diagonal terms, since the $B^{2}$ coefficient vanishes for those, and we want to estimate the leading term:

$$
\begin{aligned}
P_{i, i} Q_{i, i}+S_{i, i}^{2}= & -r^{-2 A+2}\left[\sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} u_{0, j}^{-2 A}\left\{-4\left(1-c_{i j}\right)\left(1+c_{i j}-2 c_{j}\right)\right.\right. \\
& \left.\left.+4 B\left(1-c_{i j}\right)\left(c_{j}^{2}-c_{i j}+c_{j}-1\right)\right\}\right. \\
& +\sum_{j=1}^{\left\lfloor\frac{N-1}{2}\right\rfloor} \sum_{k=1, k \neq j}^{\left\lfloor\frac{N-1}{2}\right\rfloor} u_{0, j}^{-A} u_{0, k}^{-A}\left\{-4\left(1-c_{i k}\right)\left(1+c_{i j}-2 c_{j}\right)\right. \\
& +2 B\left(1-c_{i k}\right)\left(c_{i j} c_{j}-c_{i j} c_{k}+2 c_{j} c_{k}-2 c_{i j}+3 c_{j}-c_{k}-2\right) \\
& \left.\left.+B^{2}\left(s_{i j} s_{i k} s_{j} s_{k}-\left(1+c_{i j}\right)\left(1-c_{i k}\right)\left(1-c_{j}\right)\left(1+c_{k}\right)\right)\right\}\right]
\end{aligned}
$$

For a fixed $N$, the leading term $(j=k=1)$ expanded in $\theta$ dominates for large enough $A$ :

$$
P_{i, i} Q_{i, i}+S_{i, i}^{2}=-r^{-2 A+2} u_{0,1}^{-2 A}\left[\left(i^{2}-3\right)(A-2) i^{2} \theta^{4}+O\left(N^{2} A^{2} \theta^{A+4}\right)\right]
$$

and for such $A$ it is negative for $i \geq 2$.

Our numerical investigations suggest a stronger version which we have been unable to prove.

Conjecture 1. We conjecture that the previous theorem can be strengthened to say that there exists a unique value $A_{N}$ for each $N>4$ such that for $A<A_{N}$ the Morse index of $f$ for the regular polygon on the quotient configuration space $\mathcal{C}_{N}$ is $N-5$, and the Morse index is $N-3$ for $A>A_{N}$. Furthermore, the $A_{N}$ are monotonically decreasing in $N$ with $\lim _{N \rightarrow \infty} A_{N}=2$.

To illustrate this conjecture a little more precisely we found an ad-hoc Padé approximation to $A_{N}$ which appears to have a relative error of less than $1 \%$ for $5 \leq N \leq 200$ :

$$
A_{N} \approx \frac{2 N^{3}-2.46 N^{2}+0.713 N-91.5}{N^{3}-3.3 N^{2}-17.17 N+58.5}
$$

It is an interesting curiousity that $A_{7}$ (from Conjecture 1) is exactly equal to 4 ; we did not prove this in detail (i.e. it remains to show the uniqueness of the zero eigenvalue for $A=4$ ) but the key fact is not difficult to show:

Lemma 2. $\left.\lambda_{(7,2,-)}\right|_{A=4}$ is exactly equal to 0 .
Proof. This is a straightforward calculation; we have the explicit formulae 1, 2, and 3 , from which we can compute the eigenvalues of the Hessian of $f$. In the case that $N=7$, these expressions are in terms of trigonometric functions of multiples of $\frac{\pi}{7}$. These quantities can be calculated as cubic roots (and square roots of cubic roots), for example:

$$
\cos \left(\frac{\pi}{7}\right)=\left(\frac{7}{144} \mathbb{I} \sqrt{3}-\frac{7}{432}\right)^{\frac{1}{3}}+\frac{7}{36\left(\frac{7}{144} \mathbb{I} \sqrt{3}-\frac{7}{432}\right)^{\frac{1}{3}}}+\frac{1}{6}
$$

These identities let us simplify:

$$
\begin{gathered}
\left.P_{2,2}\right|_{A=4, N=7}=\frac{7}{4} \\
\left.Q_{2,2}\right|_{A=4, N=7}=\sqrt{\frac{4375}{8}}
\end{gathered}
$$

and

$$
\left.S_{2,2}\right|_{A=4, N=7}=\mathbb{I} \sqrt{\frac{214375}{128}}
$$

and so $\left.\lambda_{(7,2,-)}\right|_{A=4}=\frac{1}{2}\left(\left.P_{2,2}+Q_{2,2} \sqrt{\left(P_{2,2}-Q_{2,2}\right)^{2}-4 S_{2,2}^{2}}\right)\right|_{A=4, N=7}=0$.

# 3. EQUAL MASS CENTRAL CONFIGURATIONS FOR SMALL $N$ 

In this section we survey equal mass central configurations for small $N$ (up to $N=9$ ) for our variable homogeneous potential. Apart from some new results in the four-body problem, the section primarily contains conjectures.
3.1. The three-body problem. For the Newtonian three-body problem the central configurations are well known, being characterized by Euler  and Lagrange  for all positive masses. Very little about these configurations changes as the potential exponent is changed (i.e. for $A \in[2, \infty)$ ): the equilateral triangle is always a central configuration and a minimum for $f$, and there is a symmetric collinear central configuration with index 1 . There are two distinct equivalence classes of equilateral triangles (multiplicity 2 ), and three distinct equivalence classes of collinear configurations (multiplicity 3 ). Configurations are considered equivalent if there is an orientation-preserving isometry (rigid motion) between them. For all $A \in[2, \infty)$, the Poincaré polynomial of the reduced configuration space is $P(t)=1+2 t$, and the Morse polynomial of $f$ is $M(t)+(1+t)=2+3 t$.
3.2. The four-body problem. Although unsolved problems remain, for the Newtonian $(A=3)$ and vortex case $(A=2)$ of the four-body problem the central configurations are well understood, with many particular results for configurations with some special symmetry or other properties $[77,39,86,49,15,104,54,84,55,61,75,108,9$, $62,110,128,35,143,11,18,63,43,37,46,30,122]$. The equal mass case is especially well characterized. The investigations of Simó  strongly indicate that the equal mass case has the largest number of central configurations for the Newtonian case, although a formal proof of that is still unavailable. Some of the bifurcations found by Simó have been rigorous analyzed more recently .

Albouy  proved for a rather general potential function (which includes our homogeneous potential for $A \in[2, \infty)$ ) that for four bodies of equal mass the planar central configurations always have at least an axis of symmetry. For the special cases of $A=2$ and $A=3$ he completely characterized the central configurations . For $A=2$, the square is the only strictly planar convex central configuration, and the equilateral triangle with a central fourth mass is the only concave central configuration. For $A=3$ there is a second concave central configuration with a central mass on the axis of symmetry of an isosceles triangle. Albouy conjectured that for $A>2$ there are no additional central configurations compared to the $A=3$ case. In this section we show this conjecture is true at least for $A>3$, and furthermore characterize the Morse indices of $f$ of the equal-mass four-body central configurations for all $A>3$. These configurations are shown for $A=3$ and $A=20$ in Figure (1).

For the regular polygon central configuration with $N=4$ (the square), we can compute the radius $r$ :

$$
r=\left(\frac{2(\sqrt{2})^{2-A}+2^{2-A}}{8}\right)^{\frac{1}{A}}=\left(2^{-1-A}\left[2^{A / 2}+1\right]\right)^{\frac{1}{A}}
$$

(this is a special case of the general result given in Section 2).

Central configurations of the equal-mass four-body problem for $A=3$ and $A=20$.

We can find the Morse index of the square by explicitly computing the eigenvalues of the Hessian of $f$. The first two of the eight eigenvalues of the Hessian of $f$ are $\lambda_{(4,0,+)}=4 A$ and $\lambda_{(4,0,+)}=0$. The other six are more complicated. There are two equal pairs $\lambda_{(4,1, \pm)}=\lambda_{(4,3, \pm)}$, for which

$$
\begin{gathered}
P_{1,1}=P_{3,3}=2\left(\frac{2^{A / 2} A+2}{1+2^{A / 2}}\right) \\
Q_{1,1}=Q_{3,3}=\frac{\left(2^{\frac{1}{2} A+1} A+4\right)\left(\left(2^{\frac{1}{2} A}+2^{A}\right) 2^{-\frac{3}{2} A-1}\right)^{\frac{2}{A}}}{1+2^{A / 2}} \\
S_{1,1}=S_{3,3}=\frac{2(A-2)\left(\left(2^{A / 2}+2^{A}\right) 2^{-3 A / 2-1}\right)^{1 / A}}{1+2^{-A / 2}}
\end{gathered}
$$

and with these in hand it is not difficult to show that $\lambda_{(4,1, \pm)}=\lambda_{(4,3, \pm)}>0$ for all $A \geq 2$.

Finally $\lambda_{(4,2, \pm)}$ is determined by

$$
\begin{gathered}
P_{2,2}=\frac{4 A}{1+2^{A / 2}} \\
Q_{2,2}=\frac{2^{A / 2+2}\left(\left(1+2^{A / 2}\right) 2^{-A-1}\right)^{\frac{2}{A}} A}{1+2^{A / 2}} \\
S_{2,2}=0
\end{gathered}
$$

and since the diagonal entries of this block are always positive $\lambda_{(4,2, \pm)}>0$ for all $A \geq 2$.

Thus in the quotient space $\mathcal{C}_{4}$ the eigenvalues are positive and the square is always a minimum of $f$. The same conclusion was reached by Jersett  using different methods. Under the direct isometry equivalence relation there are 6 distinct labelings of the square, so it has multiplicity 6 .

The equilateral triangle with a mass at its center was also studied in this context by Jersett . It has eigenvalues $0,4,4,4 A$ and two pairs of eigenvalues

$$
\lambda_{ \pm}=\frac{6+3 A+(5 A-6) 3^{A / 2}}{3+3^{A / 2}} \pm \frac{\sqrt{\left(16 A^{2}+9(A-2)^{2}\right) 3^{A}+9(A-2)^{2}\left(1-2 \cdot 3^{A / 2}\right)}}{3+3^{A / 2}}
$$

The pair of eigenvalues $\lambda_{-}$are negative  for all $A \geq 2$, so the Morse index of this configuration is always 2 . Any of the four masses can be at the center, and then there are only 2 distinct ways to label the outer triangle (under the orientationpreserving equivalence relation), so the equilateral triangle with a mass at its center has multiplicity 8 .

The isosceles central configurations of the four-body problem, which have two pairs of equal mutual distances, are unfortunately much more complicated to analyze. Its lack of rotational symmetry means it has multiplicity 24 .

Using the Albouy-Chenciner equations $$ for the isosceles configuration, we excluded most of the mutual distance and $A$-parameter space using interval analysis. After refining the parameter intervals, we then also used a method from  to prune interval sets which could not contain a bifurcation (i.e. where the Jacobian of our system must have maximal rank). To summarize this method (Theorem 5 in ): for an interval matrix $A$ with entries $[\underline{a}, \bar{a}]$, we define the midpoint and radius matrices $\operatorname{mid}(A)=(\underline{A}+\bar{A}) / 2$ and $\operatorname{rad}(A)=(\bar{A}-\underline{A}) / 2$. Then any matrix with entries contained in the interval entries of $A$ has full rank if $\sigma_{\max }(\operatorname{rad}(A))<\sigma_{\min }(\operatorname{mid}(A))$, where the $\sigma$ denote the singular values of the singular value decomposition of each matrix; as the inequality on singular values is an exact result, it needs to be strengthened slightly to account for the computational precision.

This interval arithmetic method worked very well for $A>5$, and sufficiently well to exclude bifurcations for $A>3$. However, for $A<3$ it became prohibitively computationally expensive due to the bifurcation at $A=2$ where $f$ is no longer nondegenerate.

Since we know that for $N=4$ the Poincaré polynomial of the configuration space $\mathcal{C}_{4}$ is $P(t)=1+5 t+6 t^{2}$, the above analysis implies
Theorem 5. For $A \geq 3$, the Morse polynomial of $f$ is

$$
M=P+(1+t)(5+14 t)=6+24 t+20 t^{2}
$$

All of our numerical analysis strongly supports the following conjecture (a slightly stronger version of a speculation in ), which we are unable to rigorously prove at this time:

Conjecture 2. For $A>2$, the Morse polynomial of $f$ is

$$
M=P+(1+t)(5+14 t)=6+24 t+20 t^{2}
$$

For our purposes, the case of four equal masses is a somewhat special case in that we believe the Morse indices of the critical points do not change in the interval $(2, \infty)$, although there is a degeneracy for $A=2$. We will see below that for $N>4$ there are bifurcations as $A$ is varied.
3.3. The five-body problem. Much less is known about 5-body central configurations in general compared to $N=4$. In the Newtonian case, the earliest systematic attempt was by Williams , who attempted to extend the approach that MacMillan and Bartky  pioneered for $N=4$ on convex configurations for general (not necessarily equal) masses; the work of Williams was later improved by Chen and Hsiao . There are limited results on configurations with particular symmetries $$. Albouy and Kaloshin proved that there are finitely many fivebody central configurations in the Newtonian case, apart from some exceptional cases determined by polynomials in the mass parameters for which the result is unknown $$.

For equal masses the central configurations of the five-body problem in the Newtonian case was completely characterized with a homotopy continuation method in . We can use our formula for the eigenvalues of the Hessian of $f$ to compute the Morse index of the regular pentagon. Then using numerical results we speculate on the complete Morse structure of the problem for $A \in[2, \infty)$.

The central configurations for $A=3, A=7$, and $A=20$ are shown in Figure 2.
The Hessian of $f$ for the regular pentagon has a bifurcation for some $A \in(6.755,6.756)$. As $A$ increases through this bifurcation value, the regular pentagon goes from having Morse index 0 to Morse index 2, and two new central configurations are created. The first new configuration has index 0 , and as $A$ increases its shape becomes close to being three equilateral triangles packed in a row (see Figure 2). The second new configuration has Morse index 1, and its shape approaches a square topped by an equilateral triangle.

An interesting bifurcation occurs at $A \approx 7.5637$. For $A$ below this bifurcation value, there are index-1 central configurations which are symmetric trapezoids with a fifth mass symmetrically placed in the interior of the trapezoid, and the symmetric cross has index 0 . At the bifurcation the trapezoid becomes a square, and the symmetric cross becomes degenerate. After the bifurcation (for larger values of $A$ ) the symmetric cross has index 2, and instead of symmetric trapezoids there are symmetric concave kites with index 1.

We summarize our numerical results by the following conjecture
Conjecture 3. There are unique values $A_{5} \in(6.755,6.756)$ and $A_{c} \in(7.5636,7.5638)$ such that for $2 \leq A<A_{5}$, the Morse polynomial of $f$ on $\mathcal{C}_{5}$ is

$$
M(t)=54+120 t+120 t^{2}+60 t^{3}=P(t)+(1+t)\left(53+58 t+36 t^{2}\right)
$$

for $A_{5}<A<A_{c}$ :

$$
M(t)=150+240 t+144 t^{2}+60 t^{3}=P(t)+(1+t)\left(149+82 t+36 t^{2}\right)
$$

Central configurations of the five-body problem for $A=3$, $A=7$, and $A=20$.
and finally for $A_{c}<A$ :

$$
M(t)=120+240 t+174 t^{2}+60 t^{3}=P(t)+(1+t)\left(119+112 t+36 t^{2}\right)
$$

(For the 5-body problem the Poincaré polynomial for the reduced configuration space is $P(t)=1+9 t+26 t^{2}+24 t^{3}$.)
3.4. The six-body problem. In Figure 3 we show central configurations of the six-body problem for $A=3$ and $A=20$.

The Newtonian configuration close in shape to the regular hexagon is a twisted crown; the existence and uniqueness of the relative equilbria with this type of symmetry has been studied in some detail $$.

In the equal-mass case for $A=2$ and $A=3$, it seems from several numerical experiments that the first time a central configuration without any symmetry appears is $N=8$; in this context it is interesting that as $A$ increases several asymmetric configurations are created from bifurcations already for $N=6$.

Let us consider the asymmetric index-2 central configuration, the seventh in Figure (3), as a case study in what a theory of central configurations for the limit $A \rightarrow \infty$

Conjectured central configurations of the six-body problem for $A=3$ and $A=20$.
might look like. Our choice of $f$ was motivated partly by the desire that in the limit $A \rightarrow \infty$, the nearest-neighbor distance would approach 1. The limiting configuration in question would then be a rhombus composed of equilateral triangles with two masses attached to a single edge. For large $A$, these masses only effectively interact with their single nearest neighbor. Assuming that the core rhombus is robust to small perturbations, we need only determine positions for the single-edge masses so that their single interaction direction is parallel to their position (i.e. pointing towards the center of mass). Denote the rhombus positions by $q_{1}, \ldots, q_{4}$, and assume $q_{5}$ only interacts with $q_{1}$, and $q_{6}$ with $q_{2}$, so that $q_{5}=q_{1}+e^{\mathrm{i} \theta_{1}}$ and $q_{6}=q_{2}+e^{\mathrm{i} \theta_{2}}$. Then (assuming equal masses) the additional constraints on this limit configuration are

$$
\begin{gathered}
\sum_{i=1}^{6} q_{i}=0 \\
\mu_{1} e^{\mathrm{i} \theta_{1}}=q_{5}, \quad \mu_{2} e^{\mathrm{i} \theta_{2}}=q_{6}
\end{gathered}
$$

where the $\mu_{i}$ and $\theta_{i}$ are real. This can be converted into a polynomial system with $q_{i}=\left(x_{i}, y_{i}\right)$, which we solved with computer assistance by computing a Gröbner basis

using Singular  within Sage . Although these equations are much simpler than those of a central configuration for finite $A$, we were somewhat surprised that they require finding roots of sixth-degree polynomials; for example, the position $y_{1}$ is a root of

$$
11583+44505 y_{1}-9238 y_{1}^{2}-71696 y_{1}^{3}+52212 y_{1}^{4}-21692 y_{1}^{5}+7448 y_{1}^{6}=0
$$

with $y_{1} \approx=1.33$.
For the six-body problem the Poincaré polynomial is $P(t)=1+14 t+71 t^{2}+154 t^{3}+$ $120 t^{4}$, and corresponding to Figure (3) we have the following conjectures:

Conjecture 4. For 6 bodies, for sufficiently large $A$,
$M(t)=384+1440 t+2520 t^{2}+2520 t^{3}+1080 t^{4}=P(t)+(1+t)\left(383+1043 t+1406 t^{2}+960 t^{3}\right)$ and for $A=3$
$M(t)=384+840 t+1080 t^{2}+960 t^{3}+360 t^{4}=P(t)+(1+t)\left(383+443 t+566 t^{2}+240 t^{3}\right)$
Support for this comes from the independent investigations of Ferrario , who found consistent sets of central configurations in the Newtonian case using a fixedpoint method for $N \in\{6,7,8,9\}$.
3.5. The $\{7,8,9\}$-body problems. For larger $N$, it becomes difficult to find all of the equal mass central configurations for large $A$. For the Newtonian case we have the following conjectures which agree with the numerical results of Ferrario  (apart from what may be a typo: the 26th central configuration of the 9-body problem listed by Ferrario should have isotropy 1 , rather than the $\frac{1}{2}$ stated there, corresponding to a multiplicity of $9!$ rather than $2 \cdot 9!$ ). In the vortex case $(A=2)$ there appear to be exactly 12 central configurations , so at least one bifurcations occur between $A=2$ and $A=3$.

Conjecture 5. The Morse polynomials of $f$ for $A=3$ are

$$
\begin{gathered}
\text { for } N=7, \quad M(t)=120\left(7+84 t+132 t^{2}+105 t^{3}+84 t^{4}+35 t^{5}\right) \\
\text { for } N=8, \quad M(t)=720\left(8+56 t+224 t^{2}+301 t^{3}+210 t^{4}+112 t^{5}+28 t^{6}\right) \\
\text { for } N=9, \quad M(t)=5040\left(81+216 t+384 t^{2}+732 t^{3}+746 t^{4}+396 t^{5}+168 t^{6}+36 t^{7}\right)
\end{gathered}
$$

These conjectured central configurations are pictured in Figures (4), (5), and (6).
Our experience so far has also suggested another conjecture:
Conjecture 6. The number of equal-mass central configurations never decreases as the exponent $A$ increases.

This conjecture may also be true for unequal mass central configurations, but we lack the intuition to be confident in stating this stronger form.

Conjectured central configurations of the equal-mass sevenbody problem for $A=3$, with Morse indices and multiplicities.

Conjectured central configurations of the equal-mass eightbody problem for $A=3$, with Morse indices and multiplicities.

Conjectured central configurations of the equal-mass ninebody problem for $A=3$, with Morse indices and multiplicities.

# 4. COLLINEAR CENTRAL CONFIGURATIONS 

Fortunately, results from the Newtonian case on the collinear central configurations can be easily extended to $A \in[2, \infty)$. The following result is something of a folk theorem, I do not know of a reference that explicitly states it:

Theorem 6. For any $A \in[2, \infty)$, for each ordering of $N$ positive masses on a line there is a unique central configuration, and its (planar) Morse index is $N-2$.

Proof. The uniqueness of the collinear configurations for a given ordering can be proved as an easy generalization of the argument in  (section 2.9 of that work),

which shows that the function $f$ is convex on each connected component of the collinear configuration equivalence classes (an elegant proof improving on the original result of Moulton ). There is also a proof by Ferrario for homogeneous potentials  using a fixed-point method. The statement of the Morse index being $N-2$ can be proved by generalizing the creative argument of C. Conley presented in  and , as the exponent being $A=3$ plays no essential role in that proof.

The idea of the proof of Conley, which uses an auxiliary dynamical system that converges to collinear configurations, may have inspired a paper of Buck  on Newtonian collinear configurations, which would be interesting to generalize to $A \in$ $[2, \infty)$.

# 5. Future Directions 

In addition to the various conjectures given in this article we would like to highlight some more general goals.
(1) A similar analysis to the one given here for the regular polygon could be carried out for the $N+1$ problem of a regular polygon with a central mass. If the problem is restricted to all equal masses (i.e. including the central mass), the central mass should become inconsequential for large $N$ and $A$. Much is also already known about nested and 'twisted' regular polygon configurations $$ which would be another relatively easy extension.
(2) Numerically complete an analysis of all bifurcations in the equal mass $N$-body problem as the potential exponent $A$ is varied in $[2, \infty)$ for $N \in\{6, \ldots, 10\}$ (and higher if possible).
(3) Find a consistent (within Morse theory) set of central configurations for the equal mass 7 -body problem.
(4) Extend any of these results to non-equal masses; even a perturbative analysis near the equal mass case would be a significant advance. It may also be relatively easy to extend to restricted problems (where some of the masses are infinitesimal compared to others), which already have a rich literature of results in the Newtonian case $[79,124,65,106,107,49,15,142,97,34,75$, $123,125,18,60]$.
(5) Derive equations, or a combinatorial/linear-algebraic framework, for central configurations in the limiting case of $A \rightarrow \infty$. Compared to the Newtonian case (cf. ) it should be much easier to characterize possible central configurations for all $N$. We strongly believe that the development of such a framework is acheivable and will shed useful light on the problem for all $A \geq 2$.