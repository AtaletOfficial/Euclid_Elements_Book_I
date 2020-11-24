from manimlib.imports import *
import math


class RotatingAndMove(Animation):
    CONFIG = {
        "axis": OUT,
        "radians": TAU,
        "run_time": 2.3,
        "rate_func": smooth,
        "about_point": None,
        "about_edge": None,
    }

    def __init__(self, mobject, direction, **kwargs):
        assert(isinstance(mobject, Mobject))
        digest_config(self, kwargs)
        self.mobject = mobject
        self.direction = direction


    def interpolate_mobject(self, alpha):
        self.mobject.become(self.starting_mobject)
        self.mobject.rotate(
            alpha * self.radians,
            axis=self.axis,
            about_point= self.about_point,
            about_edge=self.about_edge,
        )
        self.mobject.shift(alpha*self.direction)

class Giris(Scene):
    def construct(self):

        self.wait(.5)
        self.play(VFadeInThenOut(YasamCicegi(), run_time=3))
        self.wait()


class MaviAsama(Scene):
    def construct(self):
        mayc = MaviYaşamÇiçeği().to_edge(UP)

        self.play(FadeInFrom(mayc, UP * .3), run_time=1)
        self.wait()
        self.play(RotatingAndMove(mayc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait()


class LacivertAsama(MaviAsama, Scene):
    def construct(self):
        lyc = LacivertYaşamÇiçeği().to_edge(UP)

        self.play(RotatingAndMove(mayc, LEFT * 6), run_time=2.5)
        self.wait()

        self.play(ReplacementTransform(mayc, lyc), run_time=1)
        self.play(RotatingAndMove(lyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait()


class MorAsama(Scene):
    def construct(self):
        moyc = MorYaşamÇiçeği().to_edge(UP)

        self.play(RotatingAndMove(lyc, LEFT * 6), run_time=2.5)
        self.wait()

        self.play(ReplacementTransform(lyc, moyc), run_time=1)
        self.play(RotatingAndMove(moyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait()


class Cikis(Scene):
    def construct(self):
        moyc = MorYaşamÇiçeği().to_edge(UP)

        self.play(RotatingAndMove(self.moyc, LEFT * 6))
        self.play(FadeOut(self.moyc))
        self.wait()



class Onerme_I(Scene):

    CONFIG = {
        "yarıcap": 0.4,
        "ust_kesisim": RIGHT * .75,
        "alt_kesisim": DOWN * 1.5 + LEFT * .75,
        "ust_renk": PURPLE_E,
        "alt_renk": CAMGOBEGI,
        "orijin_t": UP * 1.5 + LEFT * 2.5,
        "alpha": -PI / 11,
        "beta": PI / 15,
        "renk_figur": BLUE_D,
        "renk_cizgi": YELLOW,
        "renk_sınır": ORANGE,
        "renk_kosul": GREEN_C
    }

    def construct(self):
        tanım_15 = TextMobject("Tanım 15:"
                               "\f İçindeki bir noktadan üzerindeki "
                               "\f her noktaya çizilen doğruların"
                               "\f birbirine eşit olduğu düzlem şekline "
                               "\f çember denir")
        bellit = TextMobject("Belit ?:"
                             "\f Merkezleri farklı olan çemberler"
                             "\f ortak yaya sahip olamazlar")
        belit_1 = TextMobject("Belit 1: "
                              "\f Herhangi bir noktadan başka herhangi "
                              "\f bir noktaya bir doğru çizilebilir")
        belit_1_ek = TextMobject("Belit 1 Ek:"
                                 "\f Verilmiş iki noktayı içeren sadece"
                                 "\f tek bir doğru vardır"
                                 "\f veya"
                                 "\f Eğer iki doğru ortak iki noktaya "
                                 "\f sahipse çakışıklardır")
        belit_2 = TextMobject("Belit 2:"
                              "\f Bir doğru istenildiği kadar yine bir"
                              "\f doğru olacak şekilde uzatılabilir")
        belit_2_ek = TextMobject("Belit 2 Ek:"
                                 "\f İki doğru ortak bir parçaya sahip"
                                 "\f olamaz")
        belit_3 = TextMobject("Belit 3: "
                              "\f Herhangi bir merkez ve bir uzunluk "
                              "\f verildiğinde bir çember çizilebilir")
        belit_5 = TextMobject("Belit 5:"
                              "\f Eğer bir doğru iki doğruyu kestiğinde"
                              "\f bu doğrunun aynı tarafındaki iç açılar"
                              "\f iki dik açıdan küçükse bu iki doğru"
                              "\f o yönde uzatıldıklarında kesişirler")
        ortak_kavramlar_1  = TextMobject("Ortak Kavramlar 1:"
                                         "\f Aynı şeye eşit olan şeyler"
                                         "\f birbirine de eşittir")
        ortak_kavramlar_5 = TextMobject("Ortak Kavramlar 5:"
                                        "\f Bütün, parçalarından büyüktür")

        tanım_15.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        belit_1.move_to(UP * 2.3 + RIGHT * 4.4).scale(0.6)
        belit_1_ek.move_to(UP * 2.1 + RIGHT * 4.5).scale(0.6)
        belit_2.move_to(UP * 2.3 + RIGHT * 4.4).scale(0.6)
        belit_2_ek.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        belit_3.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        belit_5.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        ortak_kavramlar_1.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        ortak_kavramlar_5.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)

        # Giriş
        self.wait(.5)
        self.play(VFadeInThenOut(YasamCicegi(), run_time=4))
        self.wait()


        # Mavi Aşama____________________________________________________________________________________________________
        mayc = MaviYasamCicegi().to_edge(UP)

        self.play(FadeInFrom(mayc, UP * .3), run_time=1)
        self.wait(31)

        # Önerme________________________________________________________________________________________________________
        önerme = TextMobject("Verilen bir doğru-parçası üzerine eşkenar",
                             "\f bir", "\r üçgen çizmenin yolu")

        self.play(Write(önerme), run_time=1.8)
        self.wait(2)
        self.play(FadeOut(önerme), run_time=0.7)
        self.wait(0.5)

        # Lacivert Aşama________________________________________________________________________________________________
        lyc = LacivertYasamCicegi().to_edge(UP)

        self.play(ReplacementTransform(mayc, lyc), run_time=1)
        self.wait()
        self.play(RotatingAndMove(lyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait(5.5)

        # Kanıt_________________________________________________________________________________________________________
        nokta_A, nokta_B, nokta_C, nokta_D, nokta_E = list(
            map(Dot, [LEFT, RIGHT, UP * 1.732, LEFT * 2 + UP * 1.732, RIGHT * 2 + UP * 1.732]))
        A, B, C, D, E = list(map(TextMobject, ["A", "B", "C", "D", "E"]))
        çember_A = Circle(radius=2).move_to(LEFT)
        cember_B = Circle(radius=2).move_to(RIGHT).rotate(PI, [0, -1, 0])
        cizgi_AB = Line(nokta_A, nokta_B)
        r = cizgi_AB.copy()
        çizgi_BA = Line(nokta_B, nokta_A)
        cizgi_CA = Line(nokta_C, nokta_A)
        cizgi_CB = Line(nokta_C, nokta_B)

        t_nokta_A_AB = nokta_A.copy().set_color(YELLOW).shift([-5, 0, 0])
        t_nokta_A_CA = nokta_A.copy().set_color(YELLOW).shift([-3, -1.866, 0])
        t_nokta_B_AB = nokta_B.copy().set_color(YELLOW).shift([-5, 0, 0])
        t_nokta_B_CB = nokta_B.copy().set_color(YELLOW).shift([-5, 1.866, 0])
        t_nokta_C_CA = nokta_C.copy().set_color(YELLOW).shift([-6, -3.598, 0])
        t_nokta_C_CB = nokta_C.copy().set_color(YELLOW).shift([-6, 0.134, 0])
        t_A_AB = A.copy().set_color(YELLOW).shift([-6.3, 0, 0])
        t_A_CA = A.copy().set_color(YELLOW).shift([-3.7, -1.866, 0])
        t_B_AB = B.copy().set_color(YELLOW).shift([-3.7, 0, 0])
        t_B_CB = B.copy().set_color(YELLOW).shift([-3.7, 1.866, 0])
        t_C_CA = C.copy().set_color(YELLOW).shift([-6.3, -1.9, 0])
        t_C_CB = C.copy().set_color(YELLOW).shift([-6.3, 1.866, 0])
        t_cizgi_AB = cizgi_AB.copy().set_color(YELLOW).shift([-5, 0, 0])
        t_cizgi_CA = cizgi_CA.copy().set_color(YELLOW).rotate(-61 * DEGREES).shift([-4.5, -2.732, 0])
        t_cizgi_CB = cizgi_CB.copy().set_color(YELLOW).rotate(61 * DEGREES).shift([-5.5, 1, 0])

        t_cizgi_AB_2 = cizgi_AB.copy().set_color(YELLOW).shift([-5, -1, 0])
        t_nokta_A_AB_2 = nokta_A.copy().set_color(YELLOW).shift([-5, -1, 0])
        t_nokta_B_AB_2 = nokta_B.copy().set_color(YELLOW).shift([-5, -1, 0])
        t_A_AB_2 = A.copy().set_color(YELLOW).shift([-6.3, -1, 0])
        t_B_AB_2 = B.copy().set_color(YELLOW).shift([-3.7, -1, 0])

        t_cizgi_AB_3 = cizgi_AB.copy().set_color(YELLOW).shift([-5, 1, 0])
        t_nokta_A_AB_3 = nokta_A.copy().set_color(YELLOW).shift([-5, 1, 0])
        t_nokta_B_AB_3 = nokta_B.copy().set_color(YELLOW).shift([-5, 1, 0])
        t_A_AB_3 = A.copy().set_color(YELLOW).shift([-6.3, 1, 0])
        t_B_AB_3 = B.copy().set_color(YELLOW).shift([-3.7, 1, 0])

        t_AB = VGroup(t_A_AB, t_B_AB, t_nokta_A_AB, t_nokta_B_AB, t_cizgi_AB)
        t_AB_2 = VGroup(t_A_AB_2, t_B_AB_2, t_nokta_A_AB_2, t_nokta_B_AB_2, t_cizgi_AB_2)
        t_AB_3 = VGroup(t_A_AB_3, t_B_AB_3, t_nokta_A_AB_3, t_nokta_B_AB_3, t_cizgi_AB_3)
        t_CA = VGroup(t_A_CA, t_C_CA, t_nokta_A_CA, t_nokta_C_CA, t_cizgi_CA)
        t_CB = VGroup(t_B_CB, t_C_CB, t_nokta_B_CB, t_nokta_C_CB, t_cizgi_CB)

        A.next_to(nokta_A, LEFT, 0.1)
        B.next_to(nokta_B, RIGHT, 0.1)
        C.next_to(nokta_C, UP, 0.1)
        D.next_to(nokta_D, UL, 0.1)
        E.next_to(nokta_E, UR, 0.1)

        self.play(*[ShowCreation(i) for i in [cizgi_AB, nokta_A, nokta_B]],
                  *[Write(j) for j in [A, B]], run_time=1)
        self.wait(9)

        r.add_updater(lambda l: l.become(Line(r.get_start(), çember_A.get_end())))

        self.add(r)
        self.play(*[ShowCreation(i) for i in [çember_A, nokta_D]],
                  *[Write(i) for i in [D, belit_3]], run_time=1.5)
        self.remove(r)
        self.wait(3.5)

        çizgi_BA.add_updater(lambda l: l.become(Line(çizgi_BA.get_start(), cember_B.get_end())))
        self.add(çizgi_BA)
        self.play(*[ShowCreation(i) for i in [cember_B, nokta_E]],
                  Write(E), run_time=1.5)
        self.remove(çizgi_BA)
        self.play(FadeOut(belit_3), run_time=1)
        self.wait(2.1)

        self.play(*[FadeInFromPoint(i, nokta_C) for i in [nokta_C, C]], run_time=1)
        self.wait(2.2)
        self.play(*[ShowCreation(i) for i in [cizgi_CA, cizgi_CB]],
                  Write(belit_1), run_time=1)

        self.wait(0.8)

        self.play(*[FadeToColor(i, DARKER_GREY) for i in [cember_B, cizgi_CB, nokta_E, E]],
                  *[FadeToColor(i, YELLOW) for i in [cizgi_AB, cizgi_CA, A, B, C, nokta_A, nokta_B, nokta_C]],
                   FadeOut(belit_1), run_time=1)
        self.wait(4.1)

        self.play(
            Write(tanım_15),

            TransformFromCopy(cizgi_AB, t_cizgi_AB_2),
            TransformFromCopy(nokta_A, t_nokta_A_AB_2),
            TransformFromCopy(A, t_A_AB_2),
            TransformFromCopy(nokta_B, t_nokta_B_AB_2),
            TransformFromCopy(B, t_B_AB_2),

            TransformFromCopy(cizgi_CA, t_cizgi_CA),
            TransformFromCopy(nokta_A, t_nokta_A_CA),
            TransformFromCopy(A, t_A_CA),
            TransformFromCopy(nokta_C, t_nokta_C_CA),
            TransformFromCopy(C, t_C_CA), run_time=1)

        self.play(*[FadeToColor(i, WHITE) for i in [cizgi_AB, cizgi_CA, cizgi_CB, A, B, C, E, nokta_A, nokta_B, nokta_C, nokta_E, cember_B]], run_time=1)
        self.wait(0.5)

        self.play(*[FadeToColor(i, DARKER_GREY) for i in [çember_A, cizgi_CA, nokta_D, D]],
                  *[FadeToColor(i, YELLOW) for i in [cizgi_AB, cizgi_CB, A, B, C, nokta_A, nokta_B, nokta_C]], run_time=1)
        self.wait(2.9)

        self.play(
            TransformFromCopy(cizgi_AB, t_cizgi_AB_3),
            TransformFromCopy(nokta_A, t_nokta_A_AB_3),
            TransformFromCopy(A, t_A_AB_3),
            TransformFromCopy(nokta_B, t_nokta_B_AB_3),
            TransformFromCopy(B, t_B_AB_3),

            TransformFromCopy(cizgi_CB, t_cizgi_CB),
            TransformFromCopy(nokta_B, t_nokta_B_CB),
            TransformFromCopy(B, t_B_CB),
            TransformFromCopy(nokta_C, t_nokta_C_CB),
            TransformFromCopy(C, t_C_CB),
            run_time=1
        )

        self.play(*[FadeToColor(i, WHITE) for i in [cizgi_AB, cizgi_CA, cizgi_CB, A, B, C, D, nokta_A, nokta_B, nokta_C, nokta_D, çember_A]],
                  FadeOut(tanım_15), run_time=1)
        self.wait(0.8)

        self.play(*[Indicate(i) for i in [t_AB_2, t_CA]], run_time=1)
        self.wait(2.3)

        self.play(*[Indicate(i) for i in [t_CB, t_CA]], run_time=1)
        self.wait(1.7)

        self.play(
            ReplacementTransform(t_cizgi_AB_2, t_cizgi_AB),
            ReplacementTransform(t_nokta_A_AB_2, t_nokta_A_AB),
            ReplacementTransform(t_A_AB_2, t_A_AB),
            ReplacementTransform(t_nokta_B_AB_2, t_nokta_B_AB),
            ReplacementTransform(t_B_AB_2, t_B_AB),

            ReplacementTransform(t_cizgi_AB_3, t_cizgi_AB),
            ReplacementTransform(t_nokta_A_AB_3, t_nokta_A_AB),
            ReplacementTransform(t_A_AB_3, t_A_AB),
            ReplacementTransform(t_nokta_B_AB_3, t_nokta_B_AB),
            ReplacementTransform(t_B_AB_3, t_B_AB),
            run_time=1
        )
        self.wait(4)

        self.play(Write(ortak_kavramlar_1), run_time=1)
        self.play(*[Indicate(i) for i in [t_CB, t_CA]], run_time=1)
        self.play(FadeOut(ortak_kavramlar_1), run_time=1)
        self.wait(3)

        self.play(
            ReplacementTransform(t_cizgi_CA, t_cizgi_AB),
            ReplacementTransform(t_nokta_A_CA, t_nokta_A_AB),
            ReplacementTransform(t_A_CA, t_A_AB),
            ReplacementTransform(t_nokta_C_CA, t_nokta_B_AB),
            ReplacementTransform(t_C_CA, t_B_AB),

            ReplacementTransform(t_cizgi_CB, t_cizgi_AB),
            ReplacementTransform(t_nokta_B_CB, t_nokta_B_AB),
            ReplacementTransform(t_B_CB, t_B_AB),
            ReplacementTransform(t_nokta_C_CB, t_nokta_A_AB),
            ReplacementTransform(t_C_CB, t_A_AB),
            run_time=1
        )
        self.wait(0.8)

        self.play(
            ReplacementTransform(t_cizgi_AB, cizgi_AB),
            ReplacementTransform(t_nokta_A_AB, nokta_A),
            ReplacementTransform(t_A_AB, A),
            ReplacementTransform(t_nokta_B_AB, nokta_B),
            ReplacementTransform(t_B_AB, B),

            ReplacementTransform(t_cizgi_AB.copy(), cizgi_CA),
            ReplacementTransform(t_nokta_A_AB.copy(), nokta_A),
            ReplacementTransform(t_A_AB.copy(), A),
            ReplacementTransform(t_nokta_B_AB.copy(), nokta_C),
            ReplacementTransform(t_B_AB, C),

            ReplacementTransform(t_cizgi_AB.copy(), cizgi_CB),
            ReplacementTransform(t_nokta_B_AB.copy(), nokta_B),
            ReplacementTransform(t_B_AB.copy(), B),
            ReplacementTransform(t_nokta_A_AB.copy(), nokta_C),
            ReplacementTransform(t_A_AB.copy(), C),

            *[FadeToColor(i, DARKER_GREY) for i in [cember_B, çember_A, nokta_D, nokta_E, D, E]], run_time=1.5
        )
        self.wait(2.8)

        self.play(*[FadeOut(i) for i in
                    [çember_A, cember_B, cizgi_CA, cizgi_CB, cizgi_AB, nokta_A, nokta_B, nokta_C, nokta_D, nokta_E, A, B, C, D, E]], run_time=1)
        self.wait(0.5)
        #01:50.5

        # Mor Aşama_____________________________________________________________________________________________________
        moyc = MorYasamCicegi().to_edge(UP)

        self.play(RotatingAndMove(lyc, LEFT * 6), run_time=2.5)
        self.wait()

        self.play(ReplacementTransform(lyc, moyc), run_time=1)
        self.wait(5.5)
        self.play(RotatingAndMove(moyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait(0.5)

        # Killing'in Beliti_____________________________________________________________________________________________

        cizgi_ust = Line(LEFT * 6, RIGHT * 6).set_color(self.ust_renk)
        cizgi_alt = Line(DOWN * 1.5 + LEFT * 6, DOWN * 1.5 + RIGHT * 6).set_color(self.alt_renk)
        cizgi_kesen_ust = Line(self.alt_kesisim, self.ust_kesisim).set_color([self.ust_renk, self.alt_renk])
        cizgi_kesen_alt = Line(self.alt_kesisim, self.ust_kesisim).set_color([self.ust_renk, self.alt_renk])
        t_cizgi_ust = Line(self.orijin_t, UP * 2.5 + LEFT * 1.5).set_color(self.ust_renk)
        t_cizgi_alt = Line(self.orijin_t, UP * 2.5 + LEFT * 1.5).set_color(self.alt_renk).shift(RIGHT * .03)
        t_cizgi_kesen_ust = Line(self.orijin_t, UP * 2.5 + LEFT * 1.5).set_color(self.ust_renk)
        t_cizgi_kesen_alt = Line(self.orijin_t, UP * 2.5 + LEFT * 1.5).set_color(self.alt_renk).shift(RIGHT * .06)
        L1 = Line(LEFT, RIGHT)
        L2 = Line(ORIGIN, UP)
        D = Rectangle().scale(0.1).move_to(UP * .1)
        dik_acı = VGroup(L1, L2, D).move_to(UP * 2 + RIGHT * 2.5).shift(LEFT*1.2)
        esittir = TexMobject("=").move_to(self.orijin_t + UP * 0.5 + RIGHT * 2.7).shift(LEFT*0.6)
        esitttir = TexMobject("=").move_to(self.orijin_t + UP * 0.5 + RIGHT * 2.7).shift(LEFT*0.6)
        kucuktur = TexMobject("<").move_to(self.orijin_t + UP * 0.5 + RIGHT * 2.7).shift(LEFT*0.6)
        buyuktur = TexMobject(">").move_to(self.orijin_t + UP * 0.5 + RIGHT * 2.7).shift(LEFT*0.6)

        self.play(*[ShowCreation(i) for i in [cizgi_AB, nokta_A, nokta_B]],
                  *[Write(j) for j in [A, B]], run_time=1)

        çember_A.set_color(WHITE)
        cember_B.set_color(WHITE)

        r.add_updater(lambda l: l.become(Line(r.get_start(), çember_A.get_end())))
        çizgi_BA.add_updater(lambda l: l.become(Line(çizgi_BA.get_start(), cember_B.get_end())))

        self.add(r, çizgi_BA)

        self.play(*[ShowCreation(i) for i in [çember_A, cember_B]], run_time=1.5)
        self.remove(r, çizgi_BA)
        self.wait(1.7)

        nokta_C.set_color(YELLOW)
        C.set_color(YELLOW)
        self.play(*[FadeInFromPoint(i, nokta_C) for i in [nokta_C, C]], run_time=1)
        self.wait(28.7)
        self.remove(çember_A, cember_B, cizgi_AB, nokta_A, nokta_B, nokta_C, A, B, C)
        #02:37.4

        # 5. Belit____________________________________________________________________________________________________()

        t_cizgi_ust.rotate(-cizgi_kesen_ust.get_angle() + cizgi_ust.get_angle() + PI, about_point=self.orijin_t)
        t_cizgi_alt.rotate(-cizgi_kesen_ust.get_angle(), about_point=self.orijin_t + RIGHT * .03)

        acı_ust = Arc(
            radius=self.yarıcap,
            angle=cizgi_kesen_ust.get_angle() - cizgi_ust.get_angle() - PI,
            start_angle=cizgi_ust.get_angle()
        ).move_arc_center_to(self.ust_kesisim).set_color(self.ust_renk)
        t_acı_ust = Arc(
            radius=self.yarıcap,
            angle=cizgi_kesen_ust.get_angle() - cizgi_ust.get_angle() - PI,
            start_angle=t_cizgi_ust.get_angle()
        ).move_arc_center_to(self.orijin_t).set_color(self.ust_renk)
        acı_alt = Arc(
            radius=self.yarıcap,
            angle=cizgi_kesen_ust.get_angle() - cizgi_alt.get_angle(),
            start_angle=cizgi_alt.get_angle()
        ).move_arc_center_to(self.alt_kesisim).set_color(self.alt_renk)
        t_acı_alt = Arc(
            radius=self.yarıcap,
            angle=t_cizgi_kesen_alt.get_angle() - t_cizgi_alt.get_angle(),
            start_angle=t_cizgi_alt.get_angle()
        ).move_arc_center_to(self.orijin_t).set_color(self.alt_renk)

        self.play(*[ShowCreation(i) for i in [cizgi_ust, cizgi_alt]],
                  Write(belit_5), run_time=1.2)

        self.play(*[ShowCreation(i) for i in [cizgi_kesen_ust, acı_alt, acı_ust]], run_time=0.8)

        acı_ust.add_updater(lambda l: l.become(
            Arc(
                radius=self.yarıcap,
                angle=cizgi_kesen_ust.get_angle() - cizgi_ust.get_angle() - PI,
                start_angle=cizgi_ust.get_angle()
            ).move_arc_center_to(self.ust_kesisim).set_color(self.ust_renk)))
        acı_alt.add_updater(lambda l: l.become(
            Arc(
                radius=self.yarıcap,
                angle=cizgi_kesen_ust.get_angle() - cizgi_alt.get_angle(),
                start_angle=cizgi_alt.get_angle()
            ).move_arc_center_to(self.alt_kesisim).set_color(self.alt_renk)))
        self.add(acı_alt, acı_ust)

        self.play(ReplacementTransform(cizgi_ust.copy(), t_cizgi_ust),
                  ReplacementTransform(cizgi_kesen_ust.copy(), t_cizgi_kesen_ust),
                  ReplacementTransform(acı_ust.copy(), t_acı_ust),
                  ReplacementTransform(cizgi_alt.copy(), t_cizgi_alt),
                  ReplacementTransform(cizgi_kesen_alt.copy(), t_cizgi_kesen_alt),
                  ReplacementTransform(acı_alt.copy(), t_acı_alt),
                  ShowCreation(dik_acı),
                  ShowCreation(esittir), run_time=1
                  )

        t_acı_ust.add_updater(lambda l: l.become(
            Arc(
                radius=self.yarıcap,
                angle=cizgi_kesen_ust.get_angle() - cizgi_ust.get_angle() - PI,
                start_angle=t_cizgi_ust.get_angle()
            ).move_arc_center_to(self.orijin_t).set_color(self.ust_renk)))
        t_acı_alt.add_updater(lambda l: l.become(
            Arc(
                radius=self.yarıcap,
                angle=t_cizgi_kesen_alt.get_angle() - t_cizgi_alt.get_angle(),
                start_angle=t_cizgi_alt.get_angle()
            ).move_arc_center_to(self.orijin_t).set_color(self.alt_renk)))

        self.add(t_acı_ust, t_acı_alt, t_cizgi_ust, t_cizgi_alt)

        self.play(Rotate(cizgi_ust, self.alpha, about_point=self.ust_kesisim),
                  Rotate(t_cizgi_ust, self.alpha, about_point=self.orijin_t),
                  Rotate(cizgi_alt, self.beta, about_point=self.alt_kesisim),
                  Rotate(t_cizgi_alt, self.beta, about_point=self.orijin_t + RIGHT * .03),
                  ReplacementTransform(esittir, kucuktur), run_time=1.2)

        self.play(Rotate(cizgi_ust, -2 * self.alpha, about_point=self.ust_kesisim),
                  Rotate(t_cizgi_ust, -2 * self.alpha, about_point=self.orijin_t),
                  Rotate(cizgi_alt, -2 * self.beta, about_point=self.alt_kesisim),
                  Rotate(t_cizgi_alt, -2 * self.beta, about_point=self.orijin_t + RIGHT * .03),
                  ReplacementTransform(kucuktur, buyuktur), run_time=1.2)

        self.play(Rotate(cizgi_ust, self.alpha, about_point=self.ust_kesisim),
                  Rotate(t_cizgi_ust, self.alpha, about_point=self.orijin_t),
                  Rotate(cizgi_alt, self.beta, about_point=self.alt_kesisim),
                  Rotate(t_cizgi_alt, self.beta, about_point=self.orijin_t + RIGHT * .03),
                  ReplacementTransform(buyuktur, esitttir), run_time=1.2)
        self.wait(0.1)
        self.remove(cizgi_ust, cizgi_alt, cizgi_kesen_ust, cizgi_kesen_alt, t_cizgi_ust, t_cizgi_alt,
                    t_cizgi_kesen_ust, t_cizgi_kesen_alt, acı_ust, t_acı_ust, acı_alt, t_acı_alt, dik_acı, esitttir, belit_5)
        #02:44.1

        # Çemberler Kesişir Mi________________________________________________________________________________________()

        cember_P = Circle().move_to(LEFT * 3)
        cember_Q = Circle().move_to(RIGHT * 3)
        self.add(cember_P, cember_Q)
        self.wait(0.1)
        self.play(cember_P.shift, 1.5 * RIGHT,
                  cember_Q.shift, 1.5 * LEFT, run_time=1)
        self.wait()

        self.play(cember_P.shift, 0.5 * RIGHT,
                  cember_Q.shift, 0.5 * LEFT, run_time=1)
        self.wait()

        self.play(cember_P.shift, 0.5 * RIGHT,
                  cember_Q.shift, 0.5 * LEFT, run_time=1)
        self.wait()
        self.remove(cember_Q, cember_P)

        # Şekil Geri Eklenir____________________________________________________________________________________________
        self.add(çember_A, cember_B, cizgi_AB, nokta_A, nokta_B, nokta_C, A, B, C)
        self.wait(11)

        self.play(*[FadeOut(i) for i in [çember_A, cember_B, cizgi_AB, nokta_A, nokta_B, nokta_C, A, B, C]], run_time=1)
        self.wait(0.6)
        #03:02.8

        # Killing'in Beliti Devam_______________________________________________________________________________________

        belit_6 = TextMobject("6. Belit:", "\r Diyelim ki bir", "\r çizgi", "nin", "\r tamamı,",
                              "\f iki parçaya ayrılmış", "\r bir", "\r figür", "e", "\r dahil olsun.",
                              "\f Eğer bu çizgi,",
                              "\f her bir parçayla en az bir ortak noktaya sahipse",
                              "\f o", "\r aynı zamanda", "\r parçalar arasındaki", "\r sınır", "la",
                              "\f buluşmuş olmalıdır.")

        t_belit_6 = TextMobject("6. Belit:", "\r Diyelim ki bir", "\r çizgi", "nin", "\r tamamı,",
                              "\f iki parçaya ayrılmış", "\r bir", "\r figür", "e", "\r dahil olsun.",
                              "\f Eğer bu çizgi,",
                              "\f her bir parçayla en az bir ortak noktaya sahipse",
                              "\f o", "\r aynı zamanda", "\r parçalar arasındaki", "\r sınır", "la",
                              "\f buluşmuş olmalıdır.")

        t_belit_6.scale(0.5).move_to(RIGHT * 4)

        nokta_A_1, nokta_B_1, nokta_C_x, nokta_D_1, nokta_E_1, nokta_F_1 = list(
            map(Dot, [LEFT * 4, LEFT * 2.75, LEFT*3375 + UP*1.3, LEFT * 4.883 + UP * .883, LEFT * 1.867 + UP * .883, LEFT * 1.5]))
        A_1, B_1, C_x, D_1, E_1, F_1 = list(map(TextMobject, ["A", "B", "C", "D", "E", "F"]))
        A_1.next_to(nokta_A_1, LEFT, 0.1)
        B_1.next_to(nokta_B_1, RIGHT, 0.1)
        C_x.next_to(nokta_C_x, UP, 0.1)
        D_1.next_to(nokta_D_1, UL, 0.1)
        E_1.next_to(nokta_E_1, UR, 0.1)
        F_1.next_to(nokta_F_1, RIGHT, 0.1)
        cizgi_AB_1 = Line(nokta_A_1, nokta_B_1)
        cizgi_BF_1 = Line(nokta_B_1, nokta_F_1)
        cizgi_AF_1 = Line(nokta_A_1, nokta_F_1)
        r_1 = cizgi_AB_1.copy()
        cizgi_BA_1 = Line(nokta_B_1, nokta_A_1)
        cember_A_1 = Circle(radius=1.25).move_to(LEFT * 4)
        cember_B_1 = Circle(radius=1.25).move_to(LEFT * 2.75).rotate(PI, [0, -1, 0])
        duzlem = Circle(radius=4, fill_opacity=0.5).set_color(self.renk_figur).move_to(LEFT * 4)
        duzlemm = Circle(radius=4, fill_opacity=0.3).set_color(self.renk_figur).move_to(LEFT * 4)
        duzlem_ic = Circle(radius=1.22, fill_opacity=0.5).set_color(self.renk_figur).move_to(LEFT * 4)
        duzlem_dis = Annulus(inner_radius=1.27, outer_radius=4, fill_opacity=0.5).move_to(LEFT * 4).set_color(
            self.renk_figur)
        I = TextMobject("I) AE'nin en az bir noktası BD'nin içinde").scale(0.6).move_to(
            DOWN * 1.5 + RIGHT * 3.5).set_color(self.renk_kosul)
        Ii = I.copy().scale(1.14)
        Iii = TextMobject("I) AE'nin en az bir noktası BD'nin içinde").scale(0.6).move_to(
            DOWN * 1.5 + RIGHT * 3.5).set_color(self.renk_kosul)
        II = TextMobject("\r II) AE'nin en az bir noktası BD'nin dışında").scale(0.6).move_to(
            DOWN * 1.9 + RIGHT * 3.5).set_color(self.renk_kosul)
        IIi = II.copy().scale(1.14)
        IIii = TextMobject("\r II) AE'nin en az bir noktası BD'nin dışında").scale(0.6).move_to(
            DOWN * 1.9 + RIGHT * 3.5).set_color(self.renk_kosul)
        kucuktur = TexMobject("<").move_to(self.orijin_t + UP * 0.5 + RIGHT * 2.7)
        t_cizgi_AB_1 = cizgi_AB_1.copy().shift(UP * 1.7 + LEFT * 0.9)
        t_cizgi_AF_1 = cizgi_AF_1.copy().shift(UP * 1.7 + RIGHT * 2.15)
        t_nokta_A_AB_1 = nokta_A_1.copy().shift(UP * 1.7 + LEFT * 0.9).set_color(self.renk_cizgi)
        t_nokta_A_AF_1 = nokta_A_1.copy().shift(UP * 1.7 + RIGHT * 2.15).set_color(self.renk_cizgi)
        t_nokta_B_1 = nokta_B_1.copy().shift(UP * 1.7 + LEFT * 0.9).set_color(self.renk_sınır)
        t_nokta_F_1 = nokta_F_1.copy().shift(UP * 1.7 + RIGHT * 2.15).set_color(self.renk_cizgi)
        t_A_AB_1 = A_1.copy().shift(UP * 1.7 + LEFT * 0.9).set_color(self.renk_cizgi)
        t_A_AF_1 = A_1.copy().shift(UP * 1.7 + RIGHT * 2.15).set_color(self.renk_cizgi)
        t_B_1 = B_1.copy().shift(UP * 1.7 + LEFT * 0.9).set_color(self.renk_sınır)
        t_F_1 = F_1.copy().shift(UP * 1.7 + RIGHT * 2.15).set_color(self.renk_cizgi)
        kucuktur.next_to(nokta_B_1, UP, 1.5)

        s2, s_6, s3__5, s12 = list(
            map(SurroundingRectangle, [t_belit_6[2], t_belit_6[-6], t_belit_6[3:5], t_belit_6[12]]))
        s_3, s5 = list(map(SurroundingRectangle, [t_belit_6[-3], t_belit_6[5]]))
        s7 = SurroundingRectangle(t_belit_6[7]).set_color(self.renk_figur)

        for i in (s2, s_6, s3__5, s12):
            i.set_color(self.renk_cizgi)

        for i in (s_3, s5):
            i.set_color(self.renk_sınır)

        self.play(Write(belit_6), run_time=4)
        self.wait(8.5)
        self.play(ReplacementTransform(belit_6, t_belit_6),
                  *[ShowCreation(i) for i in [cizgi_AB_1, nokta_A_1, nokta_B_1]],
                  *[Write(j) for j in [A_1, B_1]], run_time=1)

        r_1.add_updater(lambda l: l.become(Line(r_1.get_start(), cember_A_1.get_end())))
        cizgi_BA_1.add_updater(lambda l: l.become(Line(cizgi_BA_1.get_start(), cember_B_1.get_end())))
        self.add(r_1, cizgi_BA_1)

        self.play(*[ShowCreation(i) for i in [cember_A_1, cember_B_1, nokta_D_1, nokta_E_1]],
                  *[Write(i) for i in [D_1, E_1]], run_time=1.5)
        self.remove(r_1, cizgi_BA_1)

        self.play(ShowPassingFlash(s2), run_time=1)
        self.wait(3)

        self.play(*[ShowPassingFlash(i) for i in [s2, s_6]],
                  *[FadeToColor(i, self.renk_cizgi) for i in [cember_B_1, t_belit_6[2], t_belit_6[-6], nokta_A_1, nokta_E_1, A_1, E_1]],
                  run_time=1)
        self.wait(5.5)

        self.play(ShowPassingFlash(s_3),
                  *[FadeToColor(i, self.renk_sınır) for i in [cember_A_1, t_belit_6[-3], nokta_B_1, nokta_D_1, B_1, D_1]],
                  run_time=1)
        self.wait(4.5)

        self.play(ShowPassingFlash(s7),
                  *[FadeToColor(t_belit_6[7], self.renk_figur)], run_time=1)
        self.wait()

        self.play(ShowPassingFlash(s3__5),
                  FadeToColor(t_belit_6[3:5], self.renk_cizgi), run_time=1)
        self.wait(3.3)

        self.play(ShowPassingFlash(s5),
                  *[FadeToColor(i, self.renk_sınır) for i in [t_belit_6[5]]], run_time=1)
        self.wait(4.7)

        self.play(FadeIn(duzlem), run_time=1)
        self.wait(2.4)
        self.play(VFadeInThenOut(duzlem_ic), run_time=1.5)
        self.wait(0.7)
        self.play(VFadeInThenOut(duzlem_dis), run_time=1.5)
        self.play(ReplacementTransform(duzlem, duzlemm), run_time=1)
        self.wait(2.6)

        self.play(FadeToColor(t_belit_6[11], self.renk_kosul), run_time=1)
        self.play(Write(I.set_color(self.renk_kosul)), run_time=1)
        self.wait(3.7)
        self.play(Write(II.set_color(self.renk_kosul)), run_time=1)
        self.wait(11.8)

        self.play(ReplacementTransform(I, Ii), run_time=1)
        self.wait(4.3)

        self.play(*[Indicate(i) for i in [A_1, nokta_A_1]],
                  Write(tanım_15), run_time=1)
        self.wait(3)

        self.play(ReplacementTransform(Ii, Iii),
                  FadeOut(tanım_15), run_time=1)


        # I biter, II'yi deneyelim:
        self.play(ReplacementTransform(II, IIi), run_time=1)
        self.wait(1.3)

        self.play(*[ShowCreation(i) for i in [cizgi_BF_1, nokta_F_1.set_color(self.renk_cizgi)]], run_time=1)
        self.wait(0.5)
        self.play(Write(F_1.set_color(self.renk_cizgi)), run_time=1)
        self.wait(5.3)

        self.play(TransformFromCopy(cizgi_AB_1, t_cizgi_AB_1),
                  TransformFromCopy(cizgi_AF_1, t_cizgi_AF_1),
                  TransformFromCopy(nokta_A_1, t_nokta_A_AB_1),
                  TransformFromCopy(nokta_A_1, t_nokta_A_AF_1),
                  TransformFromCopy(nokta_B_1, t_nokta_B_1),
                  TransformFromCopy(nokta_F_1, t_nokta_F_1),
                  TransformFromCopy(A_1, t_A_AB_1),
                  TransformFromCopy(A_1, t_A_AF_1),
                  TransformFromCopy(B_1, t_B_1),
                  TransformFromCopy(F_1, t_F_1), run_time=1)

        self.play(Write(kucuktur),
                  Write(ortak_kavramlar_5), run_time=1)
        self.wait(2.1)

        self.play(Indicate(cember_A_1, color=self.renk_sınır, scale_factor=1.1),
                  FadeOut(ortak_kavramlar_5), run_time=1)
        self.wait(8)
        self.play(*[Indicate(i) for i in [A_1, nokta_A_1]], run_time=1)
        self.wait()
        self.play(*[Indicate(i) for i in [F_1, nokta_F_1]], run_time=1)
        self.wait(3.3)

        self.play(*[FadeOut(i) for i in [t_cizgi_AB_1, t_cizgi_AF_1, t_nokta_A_AB_1, t_nokta_A_AF_1,
                                         t_nokta_B_1, t_nokta_F_1, t_A_AB_1, t_A_AF_1, t_B_1, t_F_1, kucuktur]], run_time=1)
        self.wait(4.7)

        self.play(ReplacementTransform(IIi, IIii), run_time=1)
        self.wait(0.8)

        self.play(*[FadeOut(i) for i in [Iii, IIii]], run_time=1)
        self.wait(11)


        self.play(*[ShowCreation(i) for i in [C_x, nokta_C_x]], run_time=1)
        self.wait()
        self.play(*[FadeOut(i) for i in [t_belit_6, cember_A_1, cember_B_1, cizgi_AB_1, cizgi_BF_1, nokta_A_1, nokta_B_1, nokta_C_x, nokta_D_1,
                    nokta_E_1, nokta_F_1, A_1, B_1, C_x, D_1, E_1, F_1, duzlemm]], run_time=1)
        self.wait(2.3)
        #05:32.4

        # Zeno'nun Argümanı______________________________________________________________________________________________
        zeno = ImageMobject("Zeno_of_Sidon.jpeg")
        nokta_F_2 = Dot(UP)
        F_2 = TextMobject("F")
        F_2.next_to(nokta_F_2, DOWN, 0.2)
        L1_2 = Line().move_to(UP)
        L2_2 = Line().move_to(DOWN)
        cizgi_CF = Line(nokta_C, nokta_F_2)
        cizgi_FA = Line(nokta_F_2, nokta_A)
        cizgi_FB = Line(nokta_F_2, nokta_B)
        acı_F = Arc(start_angle=225 * DEGREES,
                    angle=-135 * DEGREES,
                    radius=0.3
                    ).set_color(BLUE_D).shift(nokta_F_2.get_center())

        self.play(FadeIn(zeno), run_timr=1)
        self.wait(11)
        self.play(FadeOut(zeno), run_time=1)
        self.wait(0.1)

        self.play(*[ShowCreation(i) for i in [cizgi_AB, nokta_A, nokta_B]],
                  *[Write(j) for j in [A, B]], run_time=1)

        r.add_updater(lambda l: l.become(Line(r.get_start(), çember_A.get_end())))
        çizgi_BA.add_updater(lambda l: l.become(Line(çizgi_BA.get_start(), cember_B.get_end())))
        self.add(r, çizgi_BA)
        self.play(*[ShowCreation(i) for i in [çember_A, cember_B]], run_time=1.5)
        self.remove(r, çizgi_BA)
        self.wait(0.6)

        self.play(*[FadeInFromPoint(i, nokta_C) for i in [nokta_C, C]], run_time=1)
        self.wait(1.6)
        self.play(*[ShowCreation(i) for i in [cizgi_CA, cizgi_CB]], run_time=1.8)
        self.wait(7.6)

        self.remove(çember_A, cember_B, cizgi_AB, cizgi_CA, cizgi_CB, nokta_A, nokta_B, nokta_C, A, B, C)
        self.wait(0.5)
        self.play(*[ShowCreation(i) for i in [L1_2, L2_2]], run_time=1)
        self.wait(12)
        self.play(L1_2.shift, DOWN,
                  L2_2.shift, UP, run_time=1)
        self.wait()
        self.remove(L1_2, L2_2)
        self.wait(10.5)

        nokta_C.set_color(WHITE)
        C.set_color(WHITE)

        self.add(r, çizgi_BA)
        self.play(*[ShowCreation(i) for i in [cizgi_AB, nokta_A, nokta_B]],
                  *[Write(j) for j in [A, B]], run_time=1)
        self.play(*[ShowCreation(i) for i in [çember_A, cember_B]], run_time=1.5)
        self.remove(r, çizgi_BA)
        self.play(*[FadeInFromPoint(i, nokta_C) for i in [nokta_C, C]], run_time=1)
        self.wait(3.3)

        self.play(ShowCreation(cizgi_CF), run_time=3.2)
        self.play(ShowCreation(nokta_F_2),
                  Write(F_2), run_time=1)
        self.play(*[ShowCreation(i) for i in [cizgi_FA, cizgi_FB]], run_time=3)
        self.wait(14.3)

        self.play(*[Indicate(i) for i in [nokta_F_2, F_2]], run_time=1)
        self.wait(4.9)

        self.play(*[FadeToColor(i, DARKER_GREY) for i in [çember_A, cember_B, cizgi_AB, cizgi_FB, nokta_B, B]], run_time=1)
        self.play(ShowCreationThenFadeOut(acı_F), run_time=1.2)
        self.play(ShowCreation(cizgi_CA), run_time=1.5)
        self.wait(44.4)
        self.play(*[FadeToColor(i, WHITE) for i in [çember_A, cember_B, cizgi_AB, cizgi_FB, nokta_B, B]],
                  FadeOut(cizgi_CA), run_time=1)
        self.wait()
        self.play(*[FadeToColor(i, YELLOW) for i in [nokta_C, nokta_F_2, C, F_2]], run_time=1)
        self.wait()

        self.play(Write(belit_1_ek), run_time=1)
        self.wait(1.5)

        self.play(FadeToColor(cizgi_CF, YELLOW), run_time=1)
        self.wait(2)
        self.play(FadeOut(belit_1_ek), run_time=1)

        self.wait(4.3)
        self.play(*[FadeToColor(i, WHITE) for i in [cizgi_CF, nokta_C, nokta_F_2, C, F_2]],
                  *[FadeToColor(i, YELLOW) for i in [cizgi_AB, cizgi_FA, cizgi_FB, nokta_A, nokta_B, nokta_F_2, A, B, F_2]],
                  run_time=1)
        self.wait(37.3)

        self.play(Write(belit_2_ek), run_time=1)
        self.wait(2)
        self.play(FadeOut(belit_2_ek), run_time=1)

        self.play(*[FadeOut(i) for i in [çember_A, cember_B, cizgi_AB, cizgi_CF, cizgi_FA, cizgi_FB, nokta_A, nokta_B, nokta_C, nokta_F_2, A,
                    B, C, F_2]], run_time=1)
        self.wait(3)

        nokta_A.set_color(WHITE)
        nokta_B.set_color(WHITE)
        #08:35.8

        #Ortak Yaya Sahip Olunamazlık
        self.wait(60)
        self.play(Write(önerme), run_time=1)
        ss2 = SurroundingRectangle(önerme[-1])
        ss2.set_color(BLUE_D)
        self.play(ShowPassingFlash(ss2), run_time=1)
        self.wait(3)
        self.play(FadeOut(önerme), run_time=1)
        self.wait(16)

        belit_2_ek.move_to(ORIGIN)
        self.play(Write(belit_2_ek), run_time=1)
        self.wait(2)
        self.play(FadeOut(belit_2_ek), run_time=1)
        self.wait()

        self.play(Write(bellit), run_time=1)
        self.wait(4)
        self.play(FadeOut(bellit), run_time=1)


        self.wait(108.2)

        # İkizkenar Üçgen________________________________________________________________________________________________
        nokta_C, nokta_D, nokta_E, nokta_H = list(
            map(Dot, [UP * 1.732, 3 * RIGHT, 3 * LEFT, UP * 3.872]))
        A, B, C, D, E, H = list(map(TextMobject, ["A", "B", "C", "D", "C", "E"]))
        çember_A = Circle(radius=2).move_to(LEFT)
        cember_B = Circle(radius=2).move_to(RIGHT).rotate(PI, [0, -1, 0])
        cember_D = Circle(radius=4).move_to(LEFT)
        cember_E = Circle(radius=4).move_to(RIGHT).rotate(PI, [0, -1, 0])
        cizgi_AB = Line(nokta_A, nokta_B)
        cizgi_AD = Line(nokta_A, nokta_D)
        cizgi_BE = Line(nokta_B, nokta_E)
        cizgi_HA = Line(nokta_H, nokta_A)
        cizgi_HB = Line(nokta_H, nokta_B)
        r = cizgi_AB.copy()
        r_AD = cizgi_AD.copy()
        r_BE = cizgi_BE.copy()
        çizgi_BA = Line(nokta_B, nokta_A)

        A.next_to(nokta_A, LEFT, 0.1)
        B.next_to(nokta_B, RIGHT, 0.1)
        D.next_to(nokta_D, RIGHT, 0.1)
        E.next_to(nokta_E, LEFT, 0.1)
        H.next_to(nokta_H, DR, 0.1)

        self.play(*[ShowCreation(i) for i in [cizgi_AB, nokta_A, nokta_B]],
                  *[Write(j) for j in [A, B]], run_time=1)
        self.wait(4.3)

        r.add_updater(lambda l: l.become(Line(r.get_start(), çember_A.get_end())))
        çizgi_BA.add_updater(lambda l: l.become(Line(çizgi_BA.get_start(), cember_B.get_end())))

       #12:02.3
        self.add(r)
        self.play(ShowCreation(çember_A),
                  Write(tanım_15), run_time=1.5)
        self.remove(r)
        self.wait(2.7)

        self.add(çizgi_BA)
        self.play(ShowCreation(cember_B), run_time=1.5)
        self.remove(çizgi_BA)
        self.play(FadeOut(tanım_15), run_time=1)
        self.wait(1.1)

        self.play(*[ShowCreation(i) for i in [cizgi_AD, cizgi_BE]], run_time=1)
        self.play(*[ShowCreation(i) for i in [nokta_D, nokta_E]],
                  *[Write(i) for i in [D, E, belit_2]], run_time=1)
        self.wait(1.2)

        self.play(FadeOut(belit_2), run_time=1)

        r_AD.add_updater(lambda l: l.become(Line(r_AD.get_start(), cember_D.get_end())))
        self.add(r_AD)
        self.play(ShowCreation(cember_D),
                  Write(tanım_15), run_time=1.5)
        self.remove(r_AD)
        self.wait(3)

        r_BE.add_updater(lambda l: l.become(Line(r_BE.get_start(), cember_E.get_end())))
        self.add(r_BE)
        self.play(ShowCreation(cember_E), run_time=1.5)
        self.remove(r_BE)
        self.play(FadeOut(tanım_15), run_time=1)
        self.wait(3.9)

        belit_6.move_to(UP * 2.3 + RIGHT * 4.2).scale(0.6)
        self.play(ShowCreation(nokta_H),
                  Write(H), run_time=1)

        self.wait(6)

        self.play(*[ShowCreation(i) for i in [cizgi_HA, cizgi_HB]], run_time=1)
        self.wait(20)

        self.play(*[FadeOut(i) for i in [çember_A, cember_B, cember_D, cember_E, cizgi_AB, cizgi_AD, cizgi_BE, cizgi_HA, cizgi_HB,
                    nokta_A, nokta_B, nokta_D, nokta_E, nokta_H, A, B, D, E, H]], run_time=1)

        # Çeşitkenar Üçgen
        nokta_A, nokta_B, nokta_C, nokta_D, nokta_E, nokta_H, nokta_I, nokta_J = list(map(Dot,
                                                                                          [LEFT, RIGHT, UP * 1.732,
                                                                                           3 * RIGHT, 3 * LEFT,
                                                                                           UP * 3.872,
                                                                                           LEFT * 2 + UP * 1.732,
                                                                                           LEFT * 1.5 + UP * 0.866]))
        A, B, C, D, E, H, I, J = list(map(TextMobject, ["A", "B", "C", "D", "E", "F", "C", "D"]))
        çember_A = Circle(radius=2).move_to(LEFT)
        cember_B = Circle(radius=2).move_to(RIGHT).rotate(PI, [0, -1, 0])

        cizgi_AB = Line(nokta_A, nokta_B)
        cizgi_AI = Line(nokta_A, nokta_I)
        cizgi_BJ = Line(nokta_B, nokta_J)
        r = cizgi_AB.copy()
        çizgi_BA = Line(nokta_B, nokta_A)

        A.next_to(nokta_A, LEFT, 0.1)
        B.next_to(nokta_B, RIGHT, 0.1)
        D.next_to(nokta_D, RIGHT, 0.1)
        E.next_to(nokta_E, LEFT, 0.1)
        H.next_to(nokta_H, UP, 0.1)

        I.next_to(nokta_I, LEFT + UP, 0.05)
        J.next_to(nokta_J, RIGHT + UP, 0.05)

        self.wait(3)
        self.play(*[ShowCreation(i) for i in [cizgi_AB, nokta_A, nokta_B]],
                  *[Write(j) for j in [A, B]], run_time=1)

        r.add_updater(lambda l: l.become(Line(r.get_start(), çember_A.get_end())))
        çizgi_BA.add_updater(lambda l: l.become(Line(çizgi_BA.get_start(), cember_B.get_end())))

        self.add(r, çizgi_BA)
        self.play(*[ShowCreation(i) for i in [çember_A, cember_B]], run_time=1.5)
        self.remove(r, çizgi_BA)
        self.wait(0.2)

        self.play(ShowCreation(cizgi_AI), run_time=1)
        self.play(ShowCreation(nokta_I),
                  Write(I), run_time=1)
        self.wait(1.8)

        self.play(ShowCreation(nokta_J),
                  Write(J), run_time=1)
        self.wait(5)

        self.play(ShowCreation(cizgi_BJ), run_time=1)
        self.wait(37)

        self.play(*[FadeOut(i) for i in [nokta_A, nokta_B, nokta_I, nokta_J, A, B,
                                          I, J, çember_A, cember_B, cizgi_AB, cizgi_AI, cizgi_BJ]],
                  run_time=1)
        self.wait(0.2)

        self.play(RotatingAndMove(moyc, LEFT * 6), run_time=2.5)
        self.wait(5)

        self.play(FadeOut(moyc), run_time=1)
        self.wait(0.5)


#   Bütün videolarda "Belit 1" gibi yazıların açıklamalrını kaldır. Zaten kanıt sırasında bunu söylüyoruz.
#   Bu tür lemmaları da yaşamçiçeklerinin hemen altına yerleştir.


class Onerme_II(Scene):

    CONFIG = {
        "mesafe_AB": 0.7,
        "mesafe_BC": 2.4,
        "acı_AB__x": 35 * DEGREES,
        "acı_BD__x": 25 * DEGREES,

        # AB > BC
        "mesafe_AB3": 2.1,
        "mesafe_BC3": 1,
        "acı_AB3__x": 35 * DEGREES,
        "acı_BD3__x": 25 * DEGREES,

        # Doğrultusunda
        "mesafe_AB4": 2.1,
        "mesafe_BC4": 1.5,
        "acı_AB4__x": 0 * DEGREES,
        "acı_BD4__x": 60 * DEGREES
    }

    def construct(self):

        # Giriş
        self.wait(.5)
        self.play(VFadeInThenOut(YaşamÇiçeği(), run_time=4.5))

        # Mavi Aşama____________________________________________________________________________________________________
        mayc = MaviYaşamÇiçeği().to_edge(UP)

        onerme = TextMobject("Verilen", "\r bir noktadan başlamak üzere",
                             "\f verilen", "\r bir doğru-parçasına eşit ",
                             "\f bir doğru-parçası çizmenin yolu")
        onerme_1 = TextMobject("Önerme 1:"
                               "\f Verilen bir doğru-parçası üzerine",
                               "\f eşkenar bir üçgen çizmenin yolu")
        belit_1 = TextMobject("Belit 1: "
                              "\f Herhangi bir noktadan başka herhangi "
                              "\f bir noktaya bir doğru çizilebilir")
        belit_2 = TextMobject("Belit 2:"
                              "\f Bir doğru istenildiği kadar yine bir"
                              "\f doğru olacak şekilde uzatılabilir")
        belit_3 = TextMobject("Belit 3: "
                              "\f Herhangi bir merkez ve bir uzunluk "
                              "\f verildiğinde bir çember çizilebilir")
        tanım_15 = TextMobject("Tanım 15:"
                               "\f İçindeki bir noktadan üzerindeki "
                               "\f her noktaya çizilen doğruların"
                               "\f birbirine eşit olduğu düzlem şekline "
                               "\f çember denir")
        ortak_kavramlar_1 = TextMobject("Ortak Kavramlar 1:"
                                        "\f Aynı şeye eşit olan şeyler"
                                        "\f birbirine de eşittir")
        ortak_kavramlar_3 = TextMobject("Ortak Kavramlar 3:"
                                        "\f Eğer eşit şeylerden eşit şeyler"
                                        "\f çıkarılırsa kalanlar da eşittir")

        onerme_1.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        belit_1.move_to(UP * 2.3 + RIGHT * 4.4).scale(0.6)
        belit_2.move_to(UP * 2.3 + RIGHT * 4.4).scale(0.6)
        belit_3.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        tanım_15.move_to(UP * 2.3 + RIGHT * 4.7).scale(0.6)
        ortak_kavramlar_1.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)
        ortak_kavramlar_3.move_to(UP * 2.3 + RIGHT * 4.5).scale(0.6)

        self.play(FadeInFrom(mayc, UP * .3), run_time=1)

        self.play(Write(onerme, run_time=2),
                  RotatingAndMove(mayc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait()
        self.play(RotatingAndMove(mayc, LEFT * 6), run_time=2.5)
        self.play(FadeOut(onerme), run_time=1)

        # Lacivert Aşama________________________________________________________________________________________________
        lyc = LacivertYaşamÇiçeği().to_edge(UP)

        self.play(ReplacementTransform(mayc, lyc))
        self.play(RotatingAndMove(lyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)

        # Kanıt_________________________________________________________________________________________________________

        A, B, C, D, E, F, G, H, K, L = list(map(TextMobject, ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L"]))

        a = LEFT*math.cos(self.acı_AB__x)*self.mesafe_AB + DOWN*math.sin(self.acı_AB__x)*self.mesafe_AB + RIGHT*0.2
        b = ORIGIN + RIGHT*0.2
        c = UP*self.mesafe_BC + RIGHT*0.2
        d = LEFT*math.cos(self.acı_BD__x)*self.mesafe_AB + UP*math.sin(self.acı_BD__x)*self.mesafe_AB + RIGHT*0.2
        e = a + RIGHT*math.cos(PI*2/3-self.acı_AB__x)*(self.mesafe_BC+0.5) + DOWN*math.sin(PI*2/3-self.acı_AB__x)*(self.mesafe_BC+0.5)
        f = RIGHT*math.cos(self.acı_BD__x)*(self.mesafe_BC+0.5) + DOWN*math.sin(self.acı_BD__x)*(self.mesafe_BC+0.5) + RIGHT*0.2
        g = RIGHT*math.cos(self.acı_BD__x)*(self.mesafe_BC) + DOWN*math.sin(self.acı_BD__x)*self.mesafe_BC + RIGHT*0.2
        h = LEFT*math.cos(self.acı_BD__x)*self.mesafe_BC + UP*math.sin(self.acı_BD__x)*self.mesafe_BC + RIGHT*0.2
        l = a + RIGHT*math.cos(PI*2/3-self.acı_AB__x)*(self.mesafe_BC) + DOWN*math.sin(PI*2/3-self.acı_AB__x)*(self.mesafe_BC)

        cember_GCH = Circle(radius=self.mesafe_BC).move_arc_center_to(RIGHT * 0.2)
        cember_GLK = Circle(radius=self.mesafe_AB + self.mesafe_BC)
        cember_GLK.move_arc_center_to(
            LEFT * math.cos(self.acı_BD__x) * self.mesafe_AB + UP * math.sin(
                self.acı_BD__x) * self.mesafe_AB + + RIGHT * 0.2)

        nokta_A = Dot(a)
        nokta_B = Dot(b)
        nokta_C = Dot(c)
        nokta_D = Dot(d)
        nokta_E = Dot(e)
        nokta_F = Dot(f)
        nokta_G = Dot(g)
        nokta_H = Dot(h)
        nokta_K = Dot(cember_GLK.point_from_proportion(0.38))
        nokta_L = Dot(l)

        cizgi_AB = Line(a, b)
        cizgi_BC = Line(b, c)
        r = cizgi_BC.copy()
        rr = Line(d, g)
        cizgi_AD = Line(a, d)
        cizgi_BD = Line(b, d)
        cizgi_BF = Line(b, f)
        cizgi_AE = Line(a, e)
        cizgi_GF = Line(g, f)
        cizgi_BG = Line(b, g)
        cizgi_AL = Line(a, l)
        cizgi_DG = Line(d, g)
        cizgi_DL = Line(d, l)
        cizgi_LE = Line(l, e)
        cizgi_GF = Line(g, f)

        t_cizgi_BC = cizgi_BC.copy().rotate(-PI/2).move_to(LEFT*4.9 + UP*2.8).shift(LEFT*0.5*self.mesafe_AB).set_color(YELLOW)
        t_cizgi_BG_ust = cizgi_BG.copy().rotate(self.acı_BD__x).move_to(LEFT*4.9 + UP*1.8).shift(LEFT*0.5*self.mesafe_AB).set_color(YELLOW)
        tt_cizgi_BG = t_cizgi_BG_ust.copy().shift(DOWN * 1.8)
        t_cizgi_DG = cizgi_DG.copy().rotate(self.acı_BD__x).move_to(LEFT * 4.9 + DOWN * 1.8).set_color(YELLOW)
        t_cizgi_DL = cizgi_DL.copy().rotate(PI*2/3-self.acı_AB__x).move_to(LEFT * 4.9 + DOWN*2.8).set_color(YELLOW)
        t_nokta_B_BC = Dot(t_cizgi_BC.get_start()).set_color(YELLOW)
        t_nokta_B_BG = Dot(t_cizgi_BG_ust.get_start()).set_color(YELLOW)
        tt_nokta_B_BG = Dot(tt_cizgi_BG.get_start()).set_color(YELLOW)
        t_nokta_C = Dot(t_cizgi_BC.get_end()).set_color(YELLOW)
        t_nokta_D_DL = Dot(t_cizgi_DL.get_start()).set_color(YELLOW)
        t_nokta_D_DG = Dot(t_cizgi_DG.get_start()).set_color(YELLOW)
        t_nokta_G_BG = Dot(t_cizgi_BG_ust.get_end()).set_color(YELLOW)
        tt_nokta_G_BG = Dot(tt_cizgi_BG.get_end()).set_color(YELLOW)
        t_nokta_G_DG = Dot(t_cizgi_DG.get_end()).set_color(YELLOW)
        t_nokta_L = Dot(t_cizgi_DL.get_end()).set_color(YELLOW)
        t_nokta_A = Dot().next_to(t_nokta_D_DL, RIGHT, self.mesafe_AB-0.2).set_color(YELLOW)
        t_nokta_B_t_DG = Dot().next_to(t_nokta_D_DG, RIGHT, self.mesafe_AB-0.2).set_color(YELLOW)
        t_A = A.copy().set_color(YELLOW)
        t_B_t_DG = B.copy().set_color(YELLOW)
        t_B_BC = B.copy().set_color(YELLOW)
        t_B_BG = B.copy().set_color(YELLOW)
        tt_B_BG = B.copy().set_color(YELLOW)
        tt_C_BG = C.copy().set_color(YELLOW)
        t_C = C.copy().set_color(YELLOW)
        t_D_DL = D.copy().set_color(YELLOW)
        t_D_DG = D.copy().set_color(YELLOW)
        t_G_BG = G.copy().set_color(YELLOW)
        t_G_DG = G.copy().set_color(YELLOW)
        tt_G_BG = G.copy().set_color(YELLOW)
        t_L = L.copy().set_color(YELLOW)
        t_cizgi_DB = Line(t_nokta_D_DG, t_nokta_B_t_DG).set_color(YELLOW)
        t_cizgi_DA = Line(t_nokta_D_DL, t_nokta_A).set_color(YELLOW)
        t_cizgi_BG_alt = Line(t_nokta_B_t_DG, t_nokta_G_DG).set_color(YELLOW)
        t_cizgi_AL = Line(t_nokta_A, t_nokta_L).set_color(YELLOW)

        t_BC = VGroup(t_B_BC, t_nokta_B_BC, t_C, t_nokta_C, t_cizgi_BC)
        t_AL = VGroup(t_A, t_nokta_A, t_L, t_nokta_L, t_cizgi_AL)
        t_BG_ust = VGroup(t_B_BG, t_nokta_B_BG, t_G_BG, t_nokta_G_BG, t_cizgi_BG_ust)

        A.next_to(nokta_A, LEFT, 0.1)
        B.next_to(nokta_B, UR, 0.1)
        C.next_to(nokta_C, UR, 0.07)
        D.next_to(nokta_D, UL, 0.07)
        E.next_to(nokta_E, LEFT, 0.1)
        F.next_to(nokta_F, RIGHT, 0.1)
        G.next_to(nokta_G, UR, 0.07)
        H.next_to(nokta_H, UL, 0.07)
        L.next_to(nokta_L, UL, 0.07)
        K.next_to(nokta_K, UL, 0.07)
        t_A.next_to(t_nokta_A, UR, 0.05)
        t_B_t_DG.next_to(t_nokta_B_t_DG, UR, 0.05)
        t_B_BC.next_to(t_nokta_B_BC, LEFT, 0.1)
        t_B_BG.next_to(t_nokta_B_BG, LEFT, 0.1)
        tt_B_BG.next_to(tt_nokta_B_BG, LEFT, 0.1)
        t_C.next_to(t_nokta_C, RIGHT, 0.1)
        t_D_DL.next_to(t_nokta_D_DL, LEFT, 0.1)
        t_D_DG.next_to(t_nokta_D_DG, LEFT, 0.1)
        t_G_BG.next_to(t_nokta_G_BG, RIGHT, 0.1)
        tt_G_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        tt_C_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        t_G_DG.next_to(t_nokta_G_DG, RIGHT, 0.1)
        t_L.next_to(t_nokta_L, RIGHT, 0.1)
#10.5
        self.play(Write(A),
                  ShowCreation(nokta_A), run_time=1)
        self.wait(0.5)
        self.play(*[Write(i) for i in [B, C]],
                  *[ShowCreation(i) for i in [cizgi_BC, nokta_B, nokta_C]], run_time=1)
        self.wait(9)
#22
        self.play(ShowCreation(cizgi_AB),
                  Write(belit_1, run_time=1.5))
        self.wait(0.5)
        self.play(FadeOut(belit_1), run_time=1)
#25
        self.play(*[ShowCreation(i) for i in [cizgi_AD, cizgi_BD, nokta_D]],
                  *[Write(i) for i in [onerme_1, D]], run_time=1.5)
        self.wait()
        self.play(FadeOut(onerme_1), run_time=1)
        self.wait(2)
#30.5
        self.play(*[ShowCreation(i) for i in [cizgi_AE, cizgi_BF]],
                  Write(belit_2, run_time=1.5))
        self.play(*[Write(i) for i in [E, F]],
                  *[ShowCreation(i) for i in [nokta_E, nokta_F]], run_time=1)
        self.play(FadeOut(belit_2), run_time=1)
        self.wait(1.5)
#35.5
        cember_GCH.rotate(PI/2)
        r.add_updater(lambda l: l.become(Line(r.get_start(), cember_GCH.get_end())))
        self.add(r)
        self.play(ShowCreation(cember_GCH),
                  *[Write(i) for i in [belit_3]], run_time=1.5)
        self.remove(r)
        self.play(*[ShowCreation(i) for i in [nokta_G, nokta_H]],
                  *[Write(i) for i in [G, H]], run_time=1)
        self.wait(2.5)
#40.5
        cember_GLK.rotate(-self.acı_BD__x)
        rr.add_updater(lambda l: l.become(Line(rr.get_start(), cember_GLK.get_end())))
        self.add(rr)
        self.play(ShowCreation(cember_GLK), run_time=1.5)
        self.remove(rr)
        self.play(*[ShowCreation(i) for i in [nokta_K, nokta_L]],
                  *[Write(i) for i in [K, L]],
                  FadeOut(belit_3), run_time=1)
        self.wait(3)
#46
        self.remove(cizgi_BF, cizgi_BD, cizgi_AB, nokta_B, cizgi_GF, nokta_G, cember_GCH, cember_GLK, nokta_C)
        self.add(cizgi_AB, cizgi_BD, nokta_B, cizgi_GF, cember_GLK, cember_GCH, nokta_G, nokta_C)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [A, D, E, F, K, L, nokta_L, cizgi_GF, cizgi_AE, cizgi_AD,
                                                         cizgi_AB, cizgi_BD, cember_GLK, nokta_A, nokta_D, nokta_E,
                                                         nokta_F, nokta_K]],
                  *[FadeToColor(i, YELLOW) for i in [B, C, G, cizgi_BC, cizgi_BG, nokta_B, nokta_C, nokta_G]],
                  run_time=1)
        self.wait(4)

        tasıma_q = [cizgi_BC, nokta_B, nokta_C, B, C]
        tasıma_p = [t_cizgi_BC, t_nokta_B_BC, t_nokta_C, t_B_BC, t_C]
        tasıma_r = [cizgi_BG, nokta_B, nokta_G, B, G]
        tasıma_s = [t_cizgi_BG_ust, t_nokta_B_BG, t_nokta_G_BG, t_B_BG, t_G_BG]
#51
        self.play(*[TransformFromCopy(q, p) for q, p in zip(tasıma_q, tasıma_p)],
                  *[TransformFromCopy(r, s) for r, s in zip(tasıma_r, tasıma_s)],
                  run_time=1)
        self.play(*[FadeToColor(i, WHITE) for i in [A, B, C, D, E, F, G, K, L, nokta_A, nokta_B, nokta_C, nokta_D,
                                                    nokta_E, nokta_F, nokta_G, nokta_K, nokta_L, cizgi_GF, cizgi_AE,
                                                    cizgi_AD, cizgi_AB, cizgi_BC, cizgi_BG, cizgi_BD, cember_GLK]],
                  run_time=1)
#53
        self.remove(cizgi_AE, cember_GLK, cember_GCH, nokta_L, nokta_G, cizgi_LE)
        self.add(cizgi_BD, cizgi_LE, cember_GCH, cember_GLK, nokta_L, nokta_G)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [A, B, C, E, F, H, nokta_A, nokta_B, nokta_C, nokta_E, nokta_F,
                                                          nokta_H, cizgi_AB, cizgi_BC, cizgi_LE, cizgi_GF, cember_GCH]],
                  *[FadeToColor(i, YELLOW) for i in [D, L, G, nokta_D, nokta_L, nokta_G, cizgi_DG, cizgi_DL]],
                  run_time=1)
        self.wait(2)

        tasıma_qq = [cizgi_DG, nokta_D, nokta_G, D, G]
        tasıma_pp = [t_cizgi_DG, t_nokta_D_DG, t_nokta_G_DG, t_D_DG, t_G_DG]
        tasıma_rr = [cizgi_DL, nokta_D, nokta_L, D, L]
        tasıma_ss = [t_cizgi_DL, t_nokta_D_DL, t_nokta_L, t_D_DL, t_L]
#56
        self.play(*[TransformFromCopy(qq, pp) for qq, pp in zip(tasıma_qq, tasıma_pp)],
                  *[TransformFromCopy(rr, ss) for rr, ss in zip(tasıma_rr, tasıma_ss)],
                  *[FadeToColor(i, WHITE) for i in [A, B, C, E, F, H, D, L, G, nokta_A, nokta_B, nokta_C, nokta_D,
                                                    nokta_E,  nokta_F, nokta_H,  nokta_D, nokta_L, nokta_G, cizgi_AB,
                                                    cizgi_BC, cizgi_LE, cizgi_GF, cizgi_DL, cizgi_DG, cember_GCH]],
                  run_time=1)

        self.wait(0.5)
#57.5
        self.play(*[Write(i) for i in [t_A, t_B_t_DG]],
                  *[ShowCreation(i) for i in [t_nokta_A, t_nokta_B_t_DG]], run_time=1)

        t_cizgi_DB.set_color(YELLOW)
        t_cizgi_DA.set_color(YELLOW)
        self.add(t_cizgi_DB, t_cizgi_DA, t_cizgi_BG_alt, t_cizgi_AL)

        self.remove(t_cizgi_DG, t_cizgi_DL, t_cizgi_BG_alt, t_cizgi_BG_alt, t_cizgi_AL, cizgi_DL, cizgi_DG, cizgi_BG,
                    cizgi_AL, cizgi_BF, nokta_A, nokta_B, t_nokta_D_DG, t_nokta_D_DL, t_nokta_B_t_DG, t_nokta_A, cizgi_AE)
        self.add(cizgi_AE, cizgi_BF, t_cizgi_BG_alt, t_cizgi_AL, nokta_A, nokta_B, t_nokta_D_DG, t_nokta_D_DL,
                 t_nokta_B_t_DG, t_nokta_A)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [C, E, F, G, H, K, L, cizgi_BC, cizgi_LE, cizgi_GF,
                                                          cizgi_AE, cizgi_BF, nokta_C, nokta_E, nokta_F, nokta_G,
                                                          nokta_H, nokta_K, nokta_L,  cember_GCH, cember_GLK]],
                  *[FadeToColor(i, ORANGE) for i in [t_D_DG, t_B_t_DG, t_nokta_D_DG, t_nokta_B_t_DG, t_cizgi_DB,
                                                     t_D_DL, t_A, t_nokta_D_DL, t_nokta_A, t_cizgi_DA,
                                                     D, A, B, cizgi_AD, cizgi_BD, nokta_D, nokta_A, nokta_B, cizgi_AB]],
                  run_time=1)
        self.wait(2.5)
#02
        B_2 = TextMobject("B").next_to(t_D_DG, ORIGIN).set_color(ORANGE)
        B_3 = TextMobject("A").next_to(t_D_DL, ORIGIN).set_color(ORANGE)
        self.play(*[FadeOut(i) for i in [t_cizgi_DB, t_cizgi_DA]],
                  ReplacementTransform(t_D_DG, B_2),
                  ReplacementTransform(t_D_DL, B_3),
                  t_B_t_DG.next_to, t_D_DG, ORIGIN,
                  t_A.next_to, t_D_DL, ORIGIN,
                  t_cizgi_BG_alt.shift, LEFT * self.mesafe_AB,
                  t_nokta_B_t_DG.shift, LEFT * (self.mesafe_AB-0.05),
                  t_cizgi_AL.shift, LEFT * self.mesafe_AB,
                  t_nokta_A.shift, LEFT * (self.mesafe_AB-0.05),
                  t_G_DG.shift, LEFT * self.mesafe_AB,
                  t_nokta_G_DG.shift, LEFT * self.mesafe_AB,
                  t_L.shift, LEFT * self.mesafe_AB,
                  t_nokta_L.shift, LEFT * self.mesafe_AB,
                  Write(ortak_kavramlar_3, run_time=1.5),
                  run_time=1)
        self.remove(B_2, B_3, t_nokta_D_DL, t_nokta_D_DG)
        self.play(*[FadeToColor(i, YELLOW) for i in [t_B_t_DG, t_A, t_nokta_A, t_nokta_B_t_DG]],
                  *[FadeToColor(i, WHITE) for i in [D, A, B, cizgi_AD, cizgi_BD, cizgi_AB, nokta_D, nokta_A, nokta_B,
                                                    C, E, F, G, H, K, L, cizgi_BC, cizgi_LE, cizgi_GF,
                                                    cizgi_AE, cizgi_BF, nokta_C, nokta_E, nokta_F, nokta_G,
                                                    nokta_H, nokta_K, nokta_L, cember_GCH, cember_GLK]],
                  run_time=1)
        self.play(FadeOut(ortak_kavramlar_3), run_time=1)

        self.play(*[Indicate(i) for i in [t_BC, t_BG_ust]], run_time=1)
        self.wait(2.7)
#09.2
        self.play(*[Indicate(i) for i in [t_BC, t_AL]], run_time=1)
        self.wait(2)

        k = [t_B_BG, t_nokta_B_BG, t_G_BG, t_nokta_G_BG, t_cizgi_BG_ust]
        l = [tt_B_BG, tt_nokta_B_BG, tt_G_BG, tt_nokta_G_BG, tt_cizgi_BG]
        m = [t_B_t_DG, t_nokta_B_t_DG, t_G_DG, t_nokta_G_DG, t_cizgi_BG_alt]
#12.2
        self.play(*[ReplacementTransform(k, l) for k, l in zip(k, l)],
                  *[ReplacementTransform(m, l) for m, l in zip(m, l)], run_time=1)
        self.wait(0.8)
# 14
        self.play(Write(ortak_kavramlar_1), run_time=1.5)
        self.wait()
        self.play(FadeOut(ortak_kavramlar_1), run_time=1)
        self.wait(0.5)

        kk = [t_B_BC, t_nokta_B_BC, t_C, t_nokta_C, t_cizgi_BC]
        ll = [tt_B_BG, tt_nokta_B_BG, tt_C_BG, tt_nokta_G_BG, tt_cizgi_BG]
        mm = [t_A, t_nokta_A, t_L, t_nokta_L, t_cizgi_AL]
#18
        self.play(*[ReplacementTransform(kk, ll) for kk, ll in zip(kk, ll)],
                  *[ReplacementTransform(mm, ll) for mm, ll in zip(mm, ll)],
                  ReplacementTransform(tt_G_BG, tt_C_BG),
                  run_time=1)
        self.remove(tt_G_BG)
        self.wait(2.5)

        bc = [B, nokta_B, C, nokta_C, cizgi_BC]
        al = [A, nokta_A, L, nokta_L, cizgi_AL]
#21.5
        self.play(*[ReplacementTransform(ll, bc) for ll, bc in zip(ll, bc)],
                  *[ReplacementTransform(ll.copy(), al) for ll, al in zip(ll, al)],
                  *[FadeToColor(i, DARKER_GREY) for i in [cember_GLK, cember_GCH, D, E, F, G, H, K, nokta_D, nokta_E,
                                             nokta_F, nokta_G, nokta_H, nokta_K, cizgi_AD, cizgi_BD, cizgi_LE, cizgi_GF,
                                            cizgi_AE, cizgi_AB, cizgi_BF]],
                  run_time=1)
        self.wait(3)

        self.play(*[FadeOut(i) for i in [cember_GLK, cember_GCH, A, B, C, D, E, F, G, H, K, L, nokta_A, nokta_B, nokta_C,
                                       nokta_D, nokta_E, nokta_F, nokta_G, nokta_H, nokta_K, nokta_L, cizgi_AD, cizgi_BD,
                                       cizgi_LE, cizgi_GF, cizgi_AE, cizgi_AB, cizgi_BF, cizgi_BC, cizgi_AL]],
                  run_time=1)

        # Mor Aşama_____________________________________________________________________________________________________
        moyc = MorYaşamÇiçeği().to_edge(UP)
#26.5
        self.play(RotatingAndMove(lyc, LEFT * 6), run_time=2.5)
        self.wait(0.5)

        self.play(ReplacementTransform(lyc, moyc), run_time=1)
        self.play(RotatingAndMove(moyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)

        ihtimaller = TextMobject("İhtimaller").move_to(UP * 3.25).scale(0.9)
        dısında = TextMobject("Dışında").move_to(LEFT * 4.1 + UP * 2.2).scale(0.9)
        uzerinde = TextMobject("Üzerinde").move_to(RIGHT * 4.15 + UP * 2.3).scale(0.9)
        yanlarında = TextMobject("Yanlarında").move_to(LEFT * 5.5 + UP * 1.55).scale(0.9)
        dogrultusunda = TextMobject("Doğrultusunda").move_to(LEFT * 2.5 + UP * 1.5).scale(0.9)
        A_mesafe_kucuk = TextMobject("$ AB < BC $").move_to(LEFT * 5.3 + UP * .6).scale(0.9)
        A_mesafe_esit = TextMobject("$ AB = BC $").move_to(LEFT * 5.3 + UP * 0.1).scale(0.9)
        A_mesafe_buyuk = TextMobject("$ AB > BC $").move_to(LEFT * 5.3 + DOWN * .4).scale(0.9)
        uclarında = TextMobject("Uçlarında").move_to(RIGHT * 2.8 + UP * 1.5).scale(0.9)
        arasında = TextMobject("Arasında").move_to(RIGHT * 5.5 + UP * 1.55).scale(0.9)

        l1 = Line(ORIGIN, LEFT * 3.1).next_to(ihtimaller, LEFT, 0.1).shift(DOWN * 0.05)
        l2 = Line(ORIGIN, DOWN * 0.7).next_to(l1.get_end(), ORIGIN).shift(DOWN * (0.7 / 2) + RIGHT * 0.02)
        ihtimaller_dısında = VGroup(l1, l2)
        l3 = Line(ORIGIN, RIGHT * 3.1).next_to(ihtimaller, RIGHT, 0.1).shift(DOWN * 0.05)
        l4 = Line(ORIGIN, DOWN * 0.7).next_to(l3.get_end(), ORIGIN).shift(DOWN * (0.7 / 2) + LEFT * 0.02)
        ihtimaller_uzerinde = VGroup(l3, l4)
        l5 = Line(ORIGIN, LEFT * 0.6).next_to(dısında, LEFT, 0.1)
        l6 = Line(ORIGIN, DOWN * 0.4).next_to(l5.get_end(), ORIGIN).shift(DOWN * 0.2 + RIGHT * 0.02)
        dısında_yanlarında = VGroup(l5, l6)
        l7 = Line(ORIGIN, RIGHT * 0.6).next_to(dısında, RIGHT, 0.1)
        l8 = Line(ORIGIN, DOWN * 0.4).next_to(l7.get_end(), ORIGIN).shift(DOWN * 0.2 + LEFT * 0.02)
        dısında_dogrultusudna = VGroup(l7, l8)
        l9 = Line(ORIGIN, LEFT * 0.4).next_to(uzerinde, LEFT, 0.1).shift(DOWN * 0.05)
        l10 = Line(ORIGIN, DOWN * 0.4).next_to(l9.get_end(), ORIGIN).shift(DOWN * 0.2 + RIGHT * 0.02)
        uzerinde_uclarında = VGroup(l9, l10)
        l11 = Line(ORIGIN, RIGHT * 0.4).next_to(uzerinde, RIGHT, 0.1).shift(DOWN * 0.05)
        l12 = Line(ORIGIN, DOWN * 0.4).next_to(l11.get_end(), ORIGIN).shift(DOWN * 0.2 + LEFT * 0.02)
        uzerinde_arasında = VGroup(l11, l12)
        l13 = Line(ORIGIN, DOWN).next_to(yanlarında, LEFT, 0.1).shift(DOWN * 0.5)
        l14 = Line(ORIGIN, RIGHT * 0.2).next_to(l13.get_end(), ORIGIN).shift(RIGHT * 0.1 + UP * 0.02)
        yanlarında_A_kucuk = VGroup(l13, l14)
        l15 = Line(ORIGIN, DOWN).next_to(l14.get_start(), ORIGIN)
        l16 = Line(ORIGIN, RIGHT * 0.2).next_to(l15.get_end(), ORIGIN).shift(RIGHT * 0.1 + UP * 0.02)
        A_kucuk_A_esit = VGroup(l15, l16)
        l17 = Line(ORIGIN, DOWN).next_to(l16.get_start(), ORIGIN)
        l18 = Line(ORIGIN, RIGHT * 0.2).next_to(l17.get_end(), ORIGIN).shift(RIGHT * 0.1 + UP * 0.02)
        A_esit_A_buyuk = VGroup(l17, l18)

        nokta = Dot(LEFT * 0.3).set_color(CAMGÖBEĞİ)
        cizgi = Line(UP * .5, DOWN * .5).move_to(RIGHT * .3)
        kare = Square()
        g0 = VGroup(cizgi, nokta, kare)
        soru = TextMobject("?").scale(3).set_color(RED_B)

#33
        self.play(*[ShowCreation(i) for i in [cizgi, nokta, kare]], run_time=1)
        self.play(cizgi.move_to, ORIGIN,
                  nokta.move_to, ORIGIN,
                  run_time=0.6)
        g1 = g0.copy().move_to(LEFT * 2.5 + UP * 2.5)
        self.play(TransformFromCopy(g0, g1),
                  run_time=0.7)

        self.play(cizgi.rotate, -PI / 9,
                  nokta.shift, DOWN * .8 + LEFT * .3,
                  run_time=0.59)
        g2 = g0.copy().move_to(UP * 2.5)
        self.play(TransformFromCopy(g0, g2),
                  run_time=0.5)

        self.play(cizgi.rotate, PI * 11 / 18,
                  nokta.move_to, ORIGIN,
                  run_time=0.58)
        g3 = g0.copy().move_to(RIGHT * 2.5 + UP * 2.5)
        self.play(TransformFromCopy(g0, g3),
                  run_time=0.7)

        self.play(cizgi.rotate, -PI / 2,
                  nokta.shift, DOWN * 0.5,
                  run_time=0.57)
        g4 = g0.copy().move_to(LEFT * 2.5)
        self.play(TransformFromCopy(g0, g4),
                  run_time=0.5)

        self.play(cizgi.rotate, -PI / 2,
                  nokta.move_to, RIGHT * .5,
                  run_time=0.56)
        g5 = g0.copy().move_to(RIGHT * 2.5)
        self.play(TransformFromCopy(g0, g5),
                  run_time=0.5)

        self.play(cizgi.rotate, -PI / 7,
                  nokta.shift, UP * .5 + LEFT * .2,
                  run_time=0.55)
        g6 = g0.copy().move_to(LEFT * 2.5 + DOWN * 2.5)
        self.play(TransformFromCopy(g0, g6),
                  run_time=0.7)

        self.play(cizgi.rotate, -PI / 5,
                  nokta.shift, LEFT * .3,
                  run_time=0.54)
        g7 = g0.copy().move_to(DOWN * 2.5)
        self.play(TransformFromCopy(g0, g7),
                  run_time=0.5)

        self.play(cizgi.rotate, PI / 6,
                  nokta.shift, DOWN * .9 + LEFT * .4,
                  run_time=0.53)
        g8 = g0.copy().move_to(RIGHT * 2.5 + DOWN * 2.5)
        self.play(TransformFromCopy(g0, g8),
                  run_time=0.7)
        self.play(*[FadeOut(i) for i in [nokta, cizgi]])
        self.wait(0.6)
#44
        self.play(FadeIn(soru), run_time=1)
        self.wait(4)
        self.remove(soru, kare, g1, g2, g3, g4, g5, g6, g7, g8)
#49
        for i in [cember_GLK, A, B, C, D, E, F, G, H, K, L,  nokta_C, nokta_D, nokta_E, nokta_F, nokta_G, nokta_H,
                  nokta_K, nokta_L, cizgi_AD, cizgi_BD, cizgi_LE, cizgi_GF, cizgi_AE, cizgi_AB, cizgi_BF, cizgi_BC,
                  cizgi_AL, cember_GCH, nokta_A, nokta_B]:
            i.set_color(WHITE)
            self.add(i)
        self.wait(1.5)
        self.play(*[FadeToColor(k, DARKER_GREY) for k in [cember_GLK, D, E, F, G, K, L, nokta_D, nokta_E, nokta_F,
                                                          nokta_G, nokta_K, nokta_L, cizgi_AD, cizgi_BD,
                                                          cizgi_LE, cizgi_GF, cizgi_AE, cizgi_BF, cizgi_AL]],
                  run_time=1)
        self.wait(0.5)

        AB = VGroup(nokta_A, cizgi_AB)
        A.add_updater(lambda l: l.next_to(nokta_A, LEFT, 0.1))
#52
        self.play(Rotate(AB, -(PI/2 + self.acı_AB__x), about_point=cizgi_AB.get_end()), run_time=1)
        self.wait(1.5)
        self.remove(cember_GLK, cember_GCH, A, B, C, D, E, F, G, H, K, L, nokta_A, nokta_B, nokta_C,
                                       nokta_D, nokta_E, nokta_F, nokta_G, nokta_H, nokta_K, nokta_L, cizgi_AD, cizgi_BD,
                                       cizgi_LE, cizgi_GF, cizgi_AE, cizgi_AB, cizgi_BF, cizgi_BC, cizgi_AL)
#54.5
        self.add(onerme)
        AB_buyuk_ek = TextMobject("\\textbf {\\textit{AB $<$ BC olmak şartıyla,}}").next_to(onerme, UP)
        self.play(DrawBorderThenFill(AB_buyuk_ek), run_time=1)
        self.wait(1.7)

        self.play(*[FadeOut(i) for i in [onerme, AB_buyuk_ek]], run_time=1)
        nokta = Dot().set_color(CAMGÖBEĞİ).move_to(DOWN * .75)
        cizgi = Line(ORIGIN, DOWN * 2).move_to(RIGHT + DOWN * .75)
        cizgi_yatay = cizgi.copy().rotate_in_place(PI / 2).shift(DOWN + LEFT).set_color(GREY)
        e = Ellipse(height=2.5, weight=1.25).rotate(PI).move_to(RIGHT + DOWN * .75)
        sol_e = e.copy().scale(0.9).move_to(DOWN * .75 + LEFT * .1)
        sag_e = sol_e.copy().move_to(DOWN * .75 + RIGHT * 2.1).rotate(PI)
        baglantı = ArcBetweenPoints(sol_e.get_start(), sag_e.get_start(), TAU / 2)
        sol_yan = Rectangle(height=3, width=2, fill_opacity=0.2).set_color(BLUE_D).move_to(DOWN * .75 + LEFT * 0.1)
        sag_yan = sol_yan.copy().move_to(DOWN * .75 + RIGHT * 2.1)
        ust_dogrultu = DashedLine(cizgi.get_start(), RIGHT + UP * 1.5).set_color(PURPLE_E)
        ust_dogrultu_y = Line(cizgi.get_start(), RIGHT + UP * 1.5)
        alt_dogrultu = DashedLine(cizgi.get_end(), RIGHT + DOWN * 3).set_color(PURPLE_E)
        alt_dogrultu_y = Line(RIGHT + DOWN * 3, cizgi.get_end())
        baglantı_2 = ArcBetweenPoints(ust_dogrultu.get_end(), alt_dogrultu.get_end(), TAU / 3)
        cizgi_2 = cizgi.copy().scale(0.85)
#58.2
        self.play(Write(ihtimaller),
                  *[ShowCreation(i) for i in [nokta, cizgi]], run_time=1)
        self.wait(2.5)

        self.play(*[ShowCreation(i) for i in [ihtimaller_dısında, ihtimaller_uzerinde]], run_time=1.5)
#3.2
        self.play(Write(dısında, run_time=1),
                  MoveAlongPath(nokta, e), run_time=1.5)

        self.remove(nokta)
        self.add(nokta)
        self.play(Write(uzerinde, run_time=1),
                  nokta.move_to, cizgi.get_start(), run_time=0.5)
        self.play(MoveAlongPath(nokta, cizgi), run_time=1)
        self.play(nokta.move_to, sol_e.get_start(), run_time=1)
#6.2
        self.play(*[ShowCreation(i) for i in [dısında_yanlarında, dısında_dogrultusudna]],
                  run_time=0.5)
        self.play(Write(yanlarında),
                  *[FadeIn(i) for i in [sol_yan, sag_yan]],
                  MoveAlongPath(nokta, sol_e, rate_func=rush_into), run_time=1)

        self.play(MoveAlongPath(nokta, baglantı), rate_func=linear,
                  run_time=0.66)  # Bu üç satırın run_time'ını ayarlarken dikkat et nokta hızı birbirine bağlı
        self.play(MoveAlongPath(nokta, sag_e), rate_func=rush_from, run_time=1)
        self.play(*[FadeOut(i) for i in [sag_yan, sol_yan]], run_time=1)
#9,86
        self.play(Write(dogrultusunda),
                  *[ShowCreation(i) for i in [ust_dogrultu, alt_dogrultu]], run_time=1)
        self.remove(nokta, ust_dogrultu, alt_dogrultu)
        self.add(ust_dogrultu, alt_dogrultu, nokta)
        self.play(nokta.move_to, ust_dogrultu.get_start(), run_time=1)
        self.play(MoveAlongPath(nokta, ust_dogrultu_y, rate_func=rush_into), run_time=0.75)
        self.play(MoveAlongPath(nokta, baglantı_2), rate_func=linear, run_time=0.6)
        self.play(MoveAlongPath(nokta, alt_dogrultu_y), rate_func=rush_from, run_time=0.75)
        self.play(*[ShowCreation(i) for i in [ust_dogrultu, alt_dogrultu]], rate_func=lambda t: smooth(1 - t),
                  run_time=1)
#14.96
        self.play(*[ShowCreation(i) for i in [uzerinde_uclarında, uzerinde_arasında]], run_time=1)
        self.remove(nokta, cizgi)
        self.add(cizgi, nokta)
        self.play(Write(uclarında),
                  Flash(nokta), run_time=1)
        nokta.next_to(cizgi.get_start(), ORIGIN)
        self.play(Flash(nokta), run_time=1)
#17.96
        self.play(Write(arasında),
                  #MoveAlongPath(nokta, cizgi_2),
                  nokta.move_to, DOWN * 1.75 + RIGHT,
                  run_time=1)
        self.wait(1.8)

        self.play(ShowPassingFlashAround(yanlarında), run_time=1)
        circle = Circle(radius=cizgi.get_length()).move_arc_center_to(cizgi.get_end()).rotate(PI/2)
        ra = cizgi.copy()
        ra.add_updater(lambda l: l.become(Line(circle.get_end(), ra.get_end())))
        mesafe = Line()
        mesafe.add_updater(lambda l: l.become(Line(cizgi.get_end(), nokta.get_center())))
        self.remove(nokta)
        self.add(ra, mesafe, nokta)
        self.wait(3)
#24.76
        self.play(ShowCreation(yanlarında_A_kucuk, rate_func=smooth),
                  ShowCreation(circle, rate_func=smooth, run_time=1.5),
                  Write(A_mesafe_kucuk, rate_func=smooth),
                  nokta.shift, LEFT*1.5, rate_func=rush_into,
                  run_time=1
                  )
        self.remove(ra, circle, nokta)
        self.add(circle, nokta)
        self.play(Write(A_mesafe_esit, rate_func=smooth),
                  ShowCreation(A_kucuk_A_esit, rate_func=smooth),
                  nokta.move_to, circle.point_from_proportion(0.25), rate_func=linear,
                  run_time=1)
        self.play(Write(A_mesafe_buyuk, rate_func=smooth),
                  ShowCreation(A_esit_A_buyuk, rate_func=smooth),
                  nokta.shift, LEFT, run_time=1, rate_func=rush_from)
        self.wait(0.5)
        mesafe.clear_updaters()
        self.play(*[FadeOut(i) for i in [mesafe, circle]], run_time=1)
        self.play(nokta.move_to, DOWN*.75, run_time=1)
        self.wait()

        # Uçlarda_______________________________________________________________________________________________________
#31.76
        self.play(ShowPassingFlashAround(uclarında), run_time=1)
        self.play(FadeToColor(uclarında, YELLOW),
                  nokta.move_to, cizgi.get_start(), run_time=1)
        self.wait(1.5)
#35.26
        self.play(FadeToColor(uclarında, GREY),
                  nokta.move_to, DOWN*.75, run_time=1)
        self.wait()

        # AB = BC_______________________________________________________________________________________________________
#37.26
        self.play(ShowPassingFlashAround(A_mesafe_esit), run_time=1)
        self.play(FadeToColor(A_mesafe_esit, YELLOW),
                  nokta.move_to, circle.point_from_proportion(0.25),
                  VFadeInThenOut(circle, run_time=2),
                  run_time=1)

        self.play(FadeToColor(A_mesafe_esit, GREY),
                  nokta.move_to, DOWN*.75, run_time=1)
        # AB < BC_______________________________________________________________________________________________________
#41.26
        self.play(ShowPassingFlashAround(A_mesafe_kucuk), run_time=1)
        self.play(FadeToColor(A_mesafe_kucuk, YELLOW), run_time=1)
        self.wait(1.5)

        self.play(FadeToColor(A_mesafe_kucuk, GREY), run_time=1)
        self.wait(0.5)

        # AB > BC_______________________________________________________________________________________________________
        A, B, C, D, E, F, G, H, K, L = list(map(TextMobject, ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L"]))

        a = LEFT * math.cos(self.acı_AB3__x) * self.mesafe_AB3 + DOWN * math.sin(
            self.acı_AB3__x) * self.mesafe_AB3 + RIGHT
        b = ORIGIN + RIGHT
        c = UP * self.mesafe_BC3 + RIGHT
        d = LEFT * math.cos(self.acı_BD3__x) * self.mesafe_AB3 + UP * math.sin(
            self.acı_BD3__x) * self.mesafe_AB3 + RIGHT
        e = a + RIGHT * math.cos(PI * 2 / 3 - self.acı_AB3__x) * (self.mesafe_BC3 + 0.5) + DOWN * math.sin(
            PI * 2 / 3 - self.acı_AB3__x) * (self.mesafe_BC3 + 0.5)
        f = RIGHT * math.cos(self.acı_BD3__x) * (self.mesafe_BC3 + 0.5) + DOWN * math.sin(self.acı_BD3__x) * (
                    self.mesafe_BC3 + 0.5) + RIGHT
        g = RIGHT * math.cos(self.acı_BD3__x) * (self.mesafe_BC3) + DOWN * math.sin(
            self.acı_BD3__x) * self.mesafe_BC3 + RIGHT
        h = LEFT * math.cos(self.acı_BD3__x) * self.mesafe_BC3 + UP * math.sin(
            self.acı_BD3__x) * self.mesafe_BC3 + RIGHT
        l = a + RIGHT * math.cos(PI * 2 / 3 - self.acı_AB3__x) * (self.mesafe_BC3) + DOWN * math.sin(
            PI * 2 / 3 - self.acı_AB3__x) * (self.mesafe_BC3)

        cember_GCH = Circle(radius=self.mesafe_BC3).move_arc_center_to(RIGHT)
        cember_GLK = Circle(radius=self.mesafe_AB3 + self.mesafe_BC3)
        cember_GLK.move_arc_center_to(
            LEFT * math.cos(self.acı_BD3__x) * self.mesafe_AB3 + UP * math.sin(
                self.acı_BD3__x) * self.mesafe_AB3 + + RIGHT)

        nokta_A = Dot(a)
        nokta_B = Dot(b)
        nokta_C = Dot(c)
        nokta_D = Dot(d)
        nokta_E = Dot(e)
        nokta_F = Dot(f)
        nokta_G = Dot(g)
        nokta_H = Dot(h)
        nokta_K = Dot(cember_GLK.point_from_proportion(0.38))
        nokta_L = Dot(l)

        cizgi_AB = Line(a, b)
        cizgi_BC = Line(b, c)
        r = cizgi_BC.copy()
        rr = Line(d, g)
        cizgi_AD = Line(a, d)
        cizgi_BD = Line(b, d)
        cizgi_BF = Line(b, f)
        cizgi_AE = Line(a, e)
        cizgi_BG = Line(b, g)
        cizgi_AL = Line(a, l)
        cizgi_DG = Line(d, g)
        cizgi_DL = Line(d, l)
        cizgi_LE = Line(l, e)
        cizgi_GF = Line(g, f)

        t_cizgi_BC = cizgi_BC.copy().rotate(-PI / 2).move_to(LEFT * 4.9 + UP * 1.5).shift(
            LEFT * 0.5 * self.mesafe_AB3).set_color(YELLOW)
        t_cizgi_BG_ust = cizgi_BG.copy().rotate(self.acı_BD3__x).move_to(LEFT * 4.9 + UP * .5).shift(
            LEFT * 0.5 * self.mesafe_AB3).set_color(YELLOW)
        tt_cizgi_BG = t_cizgi_BG_ust.copy().move_to(LEFT*4.9 + DOWN*.65).shift(
            LEFT * 0.5 * self.mesafe_AB3)
        t_cizgi_DG = cizgi_DG.copy().rotate(self.acı_BD3__x).move_to(LEFT * 4.9 + DOWN * 1.8).set_color(YELLOW)
        t_cizgi_DL = cizgi_DL.copy().rotate(PI * 2 / 3 - self.acı_AB3__x).move_to(LEFT * 4.9 + DOWN * 2.8).set_color(
            YELLOW)

        t_nokta_B_BC = Dot(t_cizgi_BC.get_start()).set_color(YELLOW)
        t_nokta_B_BG = Dot(t_cizgi_BG_ust.get_start()).set_color(YELLOW)
        tt_nokta_B_BG = Dot(tt_cizgi_BG.get_start()).set_color(YELLOW)
        t_nokta_C = Dot(t_cizgi_BC.get_end()).set_color(YELLOW)
        t_nokta_D_DL = Dot(t_cizgi_DL.get_start()).set_color(YELLOW)
        t_nokta_D_DG = Dot(t_cizgi_DG.get_start()).set_color(YELLOW)
        t_nokta_G_BG = Dot(t_cizgi_BG_ust.get_end()).set_color(YELLOW)
        tt_nokta_G_BG = Dot(tt_cizgi_BG.get_end()).set_color(YELLOW)
        t_nokta_G_DG = Dot(t_cizgi_DG.get_end()).set_color(YELLOW)
        t_nokta_L = Dot(t_cizgi_DL.get_end()).set_color(YELLOW)
        t_nokta_A = Dot().next_to(t_nokta_D_DL, RIGHT, self.mesafe_AB3 - 0.2).set_color(YELLOW)
        t_nokta_B_t_DG = Dot().next_to(t_nokta_D_DG, RIGHT, self.mesafe_AB3 - 0.2).set_color(YELLOW)
        t_A = A.copy().set_color(YELLOW)
        t_B_t_DG = B.copy().set_color(YELLOW)
        t_B_BC = B.copy().set_color(YELLOW)
        t_B_BG = B.copy().set_color(YELLOW)
        tt_B_BG = B.copy().set_color(YELLOW)
        tt_C_BG = C.copy().set_color(YELLOW)
        t_C = C.copy().set_color(YELLOW)
        t_D_DL = D.copy().set_color(YELLOW)
        t_D_DG = D.copy().set_color(YELLOW)
        t_G_BG = G.copy().set_color(YELLOW)
        t_G_DG = G.copy().set_color(YELLOW)
        tt_G_BG = G.copy().set_color(YELLOW)
        t_L = L.copy().set_color(YELLOW)
        t_cizgi_DB = Line(t_nokta_D_DG, t_nokta_B_t_DG).set_color(YELLOW)
        t_cizgi_DA = Line(t_nokta_D_DL, t_nokta_A).set_color(YELLOW)
        t_cizgi_BG_alt = Line(t_nokta_B_t_DG, t_nokta_G_DG).set_color(YELLOW)
        t_cizgi_AL = Line(t_nokta_A, t_nokta_L).set_color(YELLOW)

        t_BC = VGroup(t_B_BC, t_nokta_B_BC, t_C, t_nokta_C, t_cizgi_BC)
        t_AL = VGroup(t_A, t_nokta_A, t_L, t_nokta_L, t_cizgi_AL)
        t_BG_ust = VGroup(t_B_BG, t_nokta_B_BG, t_G_BG, t_nokta_G_BG, t_cizgi_BG_ust)

        A.next_to(nokta_A, LEFT, 0.1)
        B.next_to(nokta_B, UR, 0.1)
        C.next_to(nokta_C, UR, 0.07)
        D.next_to(nokta_D, UL, 0.07)
        E.next_to(nokta_E, LEFT, 0.1)
        F.next_to(nokta_F, RIGHT, 0.1)
        G.next_to(nokta_G, UR, 0.07)
        H.next_to(nokta_H, UP, 0.1)
        L.next_to(nokta_L, UL, 0.07)
        K.next_to(nokta_K, UL, 0.07)
        t_A.next_to(t_nokta_A, UR, 0.05)
        t_B_t_DG.next_to(t_nokta_B_t_DG, UR, 0.05)
        t_B_BC.next_to(t_nokta_B_BC, LEFT, 0.1)
        t_B_BG.next_to(t_nokta_B_BG, LEFT, 0.1)
        tt_B_BG.next_to(tt_nokta_B_BG, LEFT, 0.1)
        t_C.next_to(t_nokta_C, RIGHT, 0.1)
        t_D_DL.next_to(t_nokta_D_DL, LEFT, 0.1)
        t_D_DG.next_to(t_nokta_D_DG, LEFT, 0.1)
        t_G_BG.next_to(t_nokta_G_BG, RIGHT, 0.1)
        tt_G_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        tt_C_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        t_G_DG.next_to(t_nokta_G_DG, RIGHT, 0.1)
        t_L.next_to(t_nokta_L, RIGHT, 0.1)
#46.26
        self.play(ShowPassingFlashAround(A_mesafe_buyuk), run_time=1)
        self.play(FadeToColor(A_mesafe_buyuk, YELLOW),
                  nokta.move_to, cizgi.get_end() + LEFT*3,
                  run_time=1)
        self.wait(6)
#54.26
        self.play(FadeToColor(A_mesafe_buyuk, WHITE), run_time=1)
        self.play(
            *[FadeOutAndShift(i, UP) for i in [ihtimaller, dısında, uzerinde, yanlarında, dogrultusunda, uclarında,
                                               arasında, A_mesafe_esit, A_mesafe_kucuk, ihtimaller_dısında,
                                               ihtimaller_uzerinde, dısında_yanlarında, dısında_dogrultusudna,
                                               uzerinde_arasında, uzerinde_uclarında, yanlarında_A_kucuk,
                                               A_kucuk_A_esit, A_esit_A_buyuk, nokta, cizgi]],
            A_mesafe_buyuk.shift, UP * 3, run_time=1)

        self.play(*[Write(i) for i in [A, B, C]],
                  *[ShowCreation(i) for i in [cizgi_BC, nokta_B, nokta_C, nokta_A]],
                  run_time=1)
        self.play(ShowCreation(cizgi_AB), run_time=1)
        self.play(*[ShowCreation(i) for i in [cizgi_AD, cizgi_BD, nokta_D]],
                  *[Write(i) for i in [D]], run_time=1)
        self.play(*[Write(i) for i in [E, F]],
                  *[ShowCreation(i) for i in [cizgi_AE, cizgi_BF, nokta_E, nokta_F]],
                  run_time=1)
        cember_GCH.rotate(PI / 2)
        r.add_updater(lambda l: l.become(Line(r.get_start(), cember_GCH.get_end())))
        self.add(r)
        self.play(ShowCreation(cember_GCH), run_time=1.5)
        self.remove(r)
        self.play(*[ShowCreation(i) for i in [nokta_G, nokta_H]],
                  *[Write(i) for i in [G, H]], run_time=1)
        cember_GLK.rotate(-self.acı_BD3__x)
        rr.add_updater(lambda l: l.become(Line(rr.get_start(), cember_GLK.get_end())))
        self.add(rr)
        self.play(ShowCreation(cember_GLK), run_time=1.5)
        self.remove(rr)
        self.play(*[ShowCreation(i) for i in [nokta_K, nokta_L]],
                  *[Write(i) for i in [K, L]], run_time=1)

        self.remove(cizgi_BF, cizgi_BD, cizgi_AB, nokta_B, cizgi_GF, nokta_G, cember_GCH, cember_GLK, nokta_C, nokta_H, H)
        self.add(cizgi_AB, cizgi_BD, nokta_B, cizgi_GF, cember_GLK, cember_GCH, nokta_G, nokta_C, nokta_H, H)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [A, D, E, F, K, L, nokta_L, cizgi_GF, cizgi_AE, cizgi_AD,
                                                          cizgi_AB, cizgi_BD, cember_GLK, nokta_A, nokta_D, nokta_E,
                                                          nokta_F, nokta_K]],
                  *[FadeToColor(i, YELLOW) for i in [B, C, G, cizgi_BC, cizgi_BG, nokta_B, nokta_C, nokta_G]],
                  run_time=1)

        tasıma_q = [cizgi_BC, nokta_B, nokta_C, B, C]
        tasıma_p = [t_cizgi_BC, t_nokta_B_BC, t_nokta_C, t_B_BC, t_C]
        tasıma_r = [cizgi_BG, nokta_B, nokta_G, B, G]
        tasıma_s = [t_cizgi_BG_ust, t_nokta_B_BG, t_nokta_G_BG, t_B_BG, t_G_BG]

        self.play(*[TransformFromCopy(q, p) for q, p in zip(tasıma_q, tasıma_p)],
                  *[TransformFromCopy(r, s) for r, s in zip(tasıma_r, tasıma_s)],
                  run_time=1)
        self.play(*[FadeToColor(i, WHITE) for i in [A, B, C, D, E, F, G, K, L, nokta_A, nokta_B, nokta_C, nokta_D,
                                                    nokta_E, nokta_F, nokta_G, nokta_K, nokta_L, cizgi_GF, cizgi_AE,
                                                    cizgi_AD, cizgi_AB, cizgi_BC, cizgi_BG, cizgi_BD, cember_GLK]],
                  run_time=1)

        self.remove(cizgi_AE, cember_GLK, cember_GCH, nokta_L, nokta_G, cizgi_LE, )
        self.add(cizgi_LE, cember_GCH, cember_GLK, cizgi_BD, nokta_L, nokta_G)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [A, B, C, E, F, H, nokta_A, nokta_B, nokta_C, nokta_E, nokta_F,
                                                          nokta_H, cizgi_AB, cizgi_BC, cizgi_LE, cizgi_GF, cember_GCH]],
                  *[FadeToColor(i, YELLOW) for i in [D, L, G, nokta_D, nokta_L, nokta_G, cizgi_DG, cizgi_DL]],
                  run_time=1)

        tasıma_qq = [cizgi_DG, nokta_D, nokta_G, D, G]
        tasıma_pp = [t_cizgi_DG, t_nokta_D_DG, t_nokta_G_DG, t_D_DG, t_G_DG]
        tasıma_rr = [cizgi_DL, nokta_D, nokta_L, D, L]
        tasıma_ss = [t_cizgi_DL, t_nokta_D_DL, t_nokta_L, t_D_DL, t_L]

        self.play(*[TransformFromCopy(qq, pp) for qq, pp in zip(tasıma_qq, tasıma_pp)],
                  *[TransformFromCopy(rr, ss) for rr, ss in zip(tasıma_rr, tasıma_ss)],
                  run_time=1)
        self.play(*[FadeToColor(i, WHITE) for i in [A, B, C, E, F, H, D, L, G, nokta_A, nokta_B, nokta_C, nokta_D,
                                                    nokta_E, nokta_F, nokta_H, nokta_D, nokta_L, nokta_G, cizgi_AB,
                                                    cizgi_BC, cizgi_LE, cizgi_GF, cizgi_DL, cizgi_DG, cember_GCH]],
                  run_time=1)

        self.play(*[Write(i) for i in [t_A, t_B_t_DG]],
                  *[ShowCreation(i) for i in [t_nokta_A, t_nokta_B_t_DG]], run_time=1)

        t_cizgi_DB.set_color(YELLOW)
        t_cizgi_DA.set_color(YELLOW)
        self.add(t_cizgi_DB, t_cizgi_DA, t_cizgi_BG_alt, t_cizgi_AL)

        self.remove(t_cizgi_DG, t_cizgi_DL, t_cizgi_BG_alt, t_cizgi_BG_alt, t_cizgi_AL, cizgi_DL, cizgi_DG, cizgi_BG,
                    cizgi_AL, cizgi_BF, nokta_A, nokta_B, t_nokta_D_DG, t_nokta_D_DL, t_nokta_B_t_DG, t_nokta_A,
                    cizgi_AE, cember_GCH, cizgi_AB, nokta_H, cizgi_BD)
        self.add(cizgi_AE, cizgi_BF, t_cizgi_BG_alt, t_cizgi_AL, nokta_A, nokta_B, nokta_H, t_nokta_D_DG, t_nokta_D_DL,
                 t_nokta_B_t_DG, t_nokta_A, cember_GCH, cizgi_AB, cizgi_BD)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [C, E, F, G, H, K, L, cizgi_BC, cizgi_LE, cizgi_GF,
                                                          cizgi_AE, cizgi_BF, nokta_C, nokta_E, nokta_F, nokta_G,
                                                          nokta_H, nokta_K, nokta_L, cember_GCH, cember_GLK]],
                  *[FadeToColor(i, ORANGE) for i in [t_D_DG, t_B_t_DG, t_nokta_D_DG, t_nokta_B_t_DG, t_cizgi_DB,
                                                     t_D_DL, t_A, t_nokta_D_DL, t_nokta_A, t_cizgi_DA,
                                                     D, A, B, cizgi_AD, cizgi_BD, nokta_D, nokta_A, nokta_B, cizgi_AB]],
                  run_time=1)

        B_2 = TextMobject("B").next_to(t_D_DG, ORIGIN).set_color(ORANGE)
        B_3 = TextMobject("A").next_to(t_D_DL, ORIGIN).set_color(ORANGE)
        self.play(*[FadeOut(i) for i in [t_cizgi_DB, t_cizgi_DA]],
                  ReplacementTransform(t_D_DG, B_2),
                  ReplacementTransform(t_D_DL, B_3),
                  t_B_t_DG.next_to, t_D_DG, ORIGIN,
                  t_A.next_to, t_D_DL, ORIGIN,
                  t_cizgi_BG_alt.shift, LEFT * self.mesafe_AB3,
                  t_nokta_B_t_DG.shift, LEFT * (self.mesafe_AB3 - 0.05),
                  t_cizgi_AL.shift, LEFT * self.mesafe_AB3,
                  t_nokta_A.shift, LEFT * (self.mesafe_AB3 - 0.05),
                  t_G_DG.shift, LEFT * self.mesafe_AB3,
                  t_nokta_G_DG.shift, LEFT * self.mesafe_AB3,
                  t_L.shift, LEFT * self.mesafe_AB3,
                  t_nokta_L.shift, LEFT * self.mesafe_AB3,
                  run_time=1)
        self.remove(B_2, B_3, t_nokta_D_DL, t_nokta_D_DG)

        self.play(*[FadeToColor(i, YELLOW) for i in [t_B_t_DG, t_A, t_nokta_A, t_nokta_B_t_DG]],
                  *[FadeToColor(i, WHITE) for i in [D, A, B, cizgi_AD, cizgi_BD, cizgi_AB, nokta_D, nokta_A, nokta_B,
                                                    C, E, F, G, H, K, L, cizgi_BC, cizgi_LE, cizgi_GF,
                                                    cizgi_AE, cizgi_BF, nokta_C, nokta_E, nokta_F, nokta_G,
                                                    nokta_H, nokta_K, nokta_L, cember_GCH, cember_GLK]],
                  run_time=1)

        self.play(*[Indicate(i) for i in [t_BC, t_BG_ust]], run_time=1)
        k = [t_B_BG, t_nokta_B_BG, t_G_BG, t_nokta_G_BG, t_cizgi_BG_ust]
        l = [tt_B_BG, tt_nokta_B_BG, tt_G_BG, tt_nokta_G_BG, tt_cizgi_BG]
        m = [t_B_t_DG, t_nokta_B_t_DG, t_G_DG, t_nokta_G_DG, t_cizgi_BG_alt]
        self.play(*[ReplacementTransform(k, l) for k, l in zip(k, l)],
                  *[ReplacementTransform(m, l) for m, l in zip(m, l)], run_time=1)

        self.play(*[Indicate(i) for i in [t_BC, t_AL]], run_time=1)

        kk = [t_B_BC, t_nokta_B_BC, t_C, t_nokta_C, t_cizgi_BC]
        ll = [tt_B_BG, tt_nokta_B_BG, tt_C_BG, tt_nokta_G_BG, tt_cizgi_BG]
        mm = [t_A, t_nokta_A, t_L, t_nokta_L, t_cizgi_AL]
        self.play(*[ReplacementTransform(kk, ll) for kk, ll in zip(kk, ll)],
                  *[ReplacementTransform(mm, ll) for mm, ll in zip(mm, ll)],
                  ReplacementTransform(tt_G_BG, tt_C_BG), run_time=1)
        self.remove(tt_G_BG)

        bc = [B, nokta_B, C, nokta_C, cizgi_BC]
        al = [A, nokta_A, L, nokta_L, cizgi_AL]
        self.play(*[ReplacementTransform(ll, bc) for ll, bc in zip(ll, bc)],
                  *[ReplacementTransform(ll.copy(), al) for ll, al in zip(ll, al)],

                  *[FadeToColor(i, DARKER_GREY) for i in [cember_GLK, cember_GCH, D, E, F, G, H, K, nokta_D, nokta_E,
                                                          nokta_F, nokta_G, nokta_H, nokta_K, cizgi_AD, cizgi_BD,
                                                          cizgi_LE, cizgi_GF,
                                                          cizgi_AE, cizgi_AB, cizgi_BF]],
                  run_time=1)
#19.26
        self.wait(16)

        self.play(
            *[FadeOut(i) for i in [cember_GLK, cember_GCH, A, B, C, D, E, F, G, H, K, L, nokta_A, nokta_B, nokta_C,
                                   nokta_D, nokta_E, nokta_F, nokta_G, nokta_H, nokta_K, nokta_L, cizgi_AD, cizgi_BD,
                                   cizgi_LE, cizgi_GF, cizgi_AE, cizgi_AB, cizgi_BF, cizgi_BC, cizgi_AL, A_mesafe_buyuk]],
            run_time=1)

        # Doğrultusunda_________________________________________________________________________________________________

        A, B, C, D, E, F, G, H, K, L = list(map(TextMobject, ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L"]))

        a = RIGHT * self.mesafe_AB4 + LEFT * .5 + DOWN * .5
        b = ORIGIN + LEFT * .5 + DOWN * .5
        c = RIGHT * self.mesafe_BC4 + LEFT * .5 + DOWN * .5
        d = RIGHT * math.cos(self.acı_BD4__x) * self.mesafe_AB4 + UP * math.sin(
            self.acı_BD4__x) * self.mesafe_AB4 + LEFT * .5 + DOWN * .5
        e = a + LEFT * math.cos(PI * 2 / 3 - self.acı_AB4__x) * (self.mesafe_BC4 + 0.5) + DOWN * math.sin(
            PI * 2 / 3 - self.acı_AB4__x) * (self.mesafe_BC4 + 0.5)
        f = LEFT * math.cos(self.acı_BD4__x) * (self.mesafe_BC4 + 0.5) + DOWN * math.sin(self.acı_BD4__x) * (
                self.mesafe_BC4 + 0.5) + LEFT * .5 + DOWN * .5
        g = LEFT * math.cos(self.acı_BD4__x) * (self.mesafe_BC4) + DOWN * math.sin(
            self.acı_BD4__x) * self.mesafe_BC4 + LEFT * .5 + DOWN * .5
        h = LEFT * math.cos(self.acı_BD4__x) * self.mesafe_BC4 + UP * math.sin(
            self.acı_BD4__x) * self.mesafe_BC4 + LEFT * .5 + DOWN * .5
        l = a + LEFT * math.cos(PI * 2 / 3 - self.acı_AB4__x) * (self.mesafe_BC4) + DOWN * math.sin(
            PI * 2 / 3 - self.acı_AB4__x) * (self.mesafe_BC4)

        cember_GCH = Circle(radius=self.mesafe_BC4).move_arc_center_to(b)
        cember_GLK = Circle(radius=self.mesafe_AB4 + self.mesafe_BC4).move_arc_center_to(d)

        nokta_A = Dot(a)
        nokta_B = Dot(b)
        nokta_C = Dot(c)
        nokta_D = Dot(d)
        nokta_E = Dot(e)
        nokta_F = Dot(f)
        nokta_G = Dot(g)
        nokta_H = Dot(h)
        nokta_K = Dot(cember_GLK.point_from_proportion(0.48))
        nokta_L = Dot(l)

        cizgi_AB = Line(a, b)
        cizgi_BC = Line(b, c)
        r = cizgi_BC.copy()
        rr = Line(d, g)
        cizgi_AD = Line(a, d)
        cizgi_BD = Line(b, d)
        cizgi_BF = Line(b, f)
        cizgi_AE = Line(a, e)
        cizgi_GF = Line(g, f)
        cizgi_BG = Line(b, g)
        cizgi_AL = Line(a, l)
        cizgi_DG = Line(d, g)
        cizgi_DL = Line(d, l)
        cizgi_LE = Line(l, e)
        cizgi_GF = Line(g, f)

        t_cizgi_BC = cizgi_BC.copy().move_to(LEFT * 4.7 + UP * 1.5).shift(
            LEFT * 0.5 * self.mesafe_AB4).set_color(YELLOW)
        t_cizgi_BG_ust = cizgi_BG.copy().rotate(PI - self.acı_BD4__x).move_to(LEFT * 4.7 + UP * .5).shift(
            LEFT * 0.5 * self.mesafe_AB4).set_color(YELLOW)
        tt_cizgi_BG = t_cizgi_BG_ust.copy().move_to(LEFT*4.7 + DOWN * .6).shift(
            LEFT * 0.5 * self.mesafe_AB4)
        t_cizgi_DG = cizgi_DG.copy().rotate(PI - self.acı_BD4__x).move_to(LEFT * 4.7 + DOWN * 1.8).set_color(YELLOW)
        t_cizgi_DL = cizgi_DL.copy().rotate(self.acı_BD4__x).move_to(LEFT * 4.7 + DOWN * 2.8).set_color(
            YELLOW)
        t_nokta_B_BC = Dot(t_cizgi_BC.get_start()).set_color(YELLOW)
        t_nokta_B_BG = Dot(t_cizgi_BG_ust.get_start()).set_color(YELLOW)
        tt_nokta_B_BG = Dot(tt_cizgi_BG.get_start()).set_color(YELLOW)
        t_nokta_C = Dot(t_cizgi_BC.get_end()).set_color(YELLOW)
        t_nokta_D_DL = Dot(t_cizgi_DL.get_start()).set_color(YELLOW)
        t_nokta_D_DG = Dot(t_cizgi_DG.get_start()).set_color(YELLOW)
        t_nokta_G_BG = Dot(t_cizgi_BG_ust.get_end()).set_color(YELLOW)
        tt_nokta_G_BG = Dot(tt_cizgi_BG.get_end()).set_color(YELLOW)
        t_nokta_G_DG = Dot(t_cizgi_DG.get_end()).set_color(YELLOW)
        t_nokta_L = Dot(t_cizgi_DL.get_end()).set_color(YELLOW)
        t_nokta_A = Dot().next_to(t_nokta_D_DL, RIGHT, self.mesafe_AB4 - 0.2).set_color(YELLOW)
        t_nokta_B_t_DG = Dot().next_to(t_nokta_D_DG, RIGHT, self.mesafe_AB4 - 0.2).set_color(YELLOW)
        t_A = A.copy().set_color(YELLOW)
        t_B_t_DG = B.copy().set_color(YELLOW)
        t_B_BC = B.copy().set_color(YELLOW)
        t_B_BG = B.copy().set_color(YELLOW)
        tt_B_BG = B.copy().set_color(YELLOW)
        tt_C_BG = C.copy().set_color(YELLOW)
        t_C = C.copy().set_color(YELLOW)
        t_D_DL = D.copy().set_color(YELLOW)
        t_D_DG = D.copy().set_color(YELLOW)
        t_G_BG = G.copy().set_color(YELLOW)
        t_G_DG = G.copy().set_color(YELLOW)
        tt_G_BG = G.copy().set_color(YELLOW)
        t_L = L.copy().set_color(YELLOW)
        t_cizgi_DB = Line(t_nokta_D_DG, t_nokta_B_t_DG).set_color(YELLOW)
        t_cizgi_DA = Line(t_nokta_D_DL, t_nokta_A).set_color(YELLOW)
        t_cizgi_BG_alt = Line(t_nokta_B_t_DG, t_nokta_G_DG).set_color(YELLOW)
        t_cizgi_AL = Line(t_nokta_A, t_nokta_L).set_color(YELLOW)

        t_BC = VGroup(t_B_BC, t_nokta_B_BC, t_C, t_nokta_C, t_cizgi_BC)
        t_AL = VGroup(t_A, t_nokta_A, t_L, t_nokta_L, t_cizgi_AL)
        t_BG_ust = VGroup(t_B_BG, t_nokta_B_BG, t_G_BG, t_nokta_G_BG, t_cizgi_BG_ust)

        sol_dogrultu = DashedLine(cizgi_BC.get_start(), LEFT * 1.4 + DOWN * .5).set_color(PURPLE_E)
        sag_dogrultu = DashedLine(cizgi_BC.get_end(), RIGHT * 2.5 + DOWN * .5).set_color(PURPLE_E)

        A.next_to(nokta_A, UR, 0.03)
        B.next_to(nokta_B, UL, 0.03)
        C.next_to(nokta_C, DR, 0.03)
        D.next_to(nokta_D, UP, 0.1)
        E.next_to(nokta_E, DR, 0.07)
        F.next_to(nokta_F, DL, 0.07)
        G.next_to(nokta_G, UP, 0.07)
        H.next_to(nokta_H, UL, 0.07)
        L.next_to(nokta_L, UP, 0.07)
        K.next_to(nokta_K, UL, 0.07)
        t_A.next_to(t_nokta_A, UR, 0.05)
        t_B_t_DG.next_to(t_nokta_B_t_DG, UR, 0.05)
        t_B_BC.next_to(t_nokta_B_BC, LEFT, 0.1)
        t_B_BG.next_to(t_nokta_B_BG, LEFT, 0.1)
        tt_B_BG.next_to(tt_nokta_B_BG, LEFT, 0.1)
        t_C.next_to(t_nokta_C, RIGHT, 0.1)
        t_D_DL.next_to(t_nokta_D_DL, LEFT, 0.1)
        t_D_DG.next_to(t_nokta_D_DG, LEFT, 0.1)
        t_G_BG.next_to(t_nokta_G_BG, RIGHT, 0.1)
        tt_G_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        tt_C_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        t_G_DG.next_to(t_nokta_G_DG, RIGHT, 0.1)
        t_L.next_to(t_nokta_L, RIGHT, 0.1)


        A_mesafe_buyuk.move_to(LEFT * 5.3 + DOWN * .4)
        self.add(ihtimaller, dısında, uzerinde, yanlarında, dogrultusunda, uclarında, arasında, A_mesafe_esit,
                 A_mesafe_kucuk, ihtimaller_dısında, ihtimaller_uzerinde, dısında_yanlarında, dısında_dogrultusudna,
                 uzerinde_arasında, uzerinde_uclarında, yanlarında_A_kucuk, A_kucuk_A_esit, A_esit_A_buyuk,
                 A_mesafe_buyuk)

        self.play(*[FadeToColor(i, GREY) for i in [A_mesafe_buyuk, yanlarında]], run_time=1)
#37.26
        self.play(ShowPassingFlashAround(dogrultusunda), run_time=1)
        self.play(
            *[FadeOutAndShift(i, UP) for i in [ihtimaller, dısında, uzerinde, yanlarında, uclarında,
                                               arasında, A_mesafe_esit, A_mesafe_kucuk, ihtimaller_dısında,
                                               ihtimaller_uzerinde, dısında_yanlarında, dısında_dogrultusudna,
                                               uzerinde_arasında, uzerinde_uclarında, yanlarında_A_kucuk,
                                               A_kucuk_A_esit, A_esit_A_buyuk, A_mesafe_buyuk]],
            dogrultusunda.move_to, UP * 3 + LEFT * 5.3,
            run_time=1)

        self.play(*[Write(i) for i in [A, B, C]],
                  *[ShowCreation(i) for i in [sol_dogrultu, sag_dogrultu, cizgi_BC, nokta_B, nokta_C,  nokta_A]],
                  run_time=1)
        self.play(ShowCreation(cizgi_AB), run_time=1)
        self.play(*[ShowCreation(i) for i in [cizgi_AD, cizgi_BD, nokta_D]],
                  *[Write(i) for i in [D]], run_time=1)

        self.play(*[Write(i) for i in [E, F]],
                  *[ShowCreation(i) for i in [cizgi_AE, cizgi_BF, nokta_E, nokta_F]], run_time=1)

        r.add_updater(lambda l: l.become(Line(r.get_start(), cember_GCH.get_end())))
        self.add(r)
        self.play(ShowCreation(cember_GCH), run_time=1.5)
        self.remove(r)
        self.play(*[ShowCreation(i) for i in [nokta_G, nokta_H]],
                  *[Write(i) for i in [G, H]], run_time=1)

        cember_GLK.rotate(-self.acı_BD4__x)
        rr.add_updater(lambda l: l.become(Line(rr.get_start(), cember_GLK.get_end())))
        self.add(rr)
        self.play(ShowCreation(cember_GLK), run_time=1.5)
        self.remove(rr)
        self.play(*[ShowCreation(i) for i in [nokta_K, nokta_L]],
                  *[Write(i) for i in [K, L]], run_time=1)

        self.remove(cizgi_BF, cizgi_BD, cizgi_AB, nokta_B, cizgi_GF, nokta_G, cember_GCH, cember_GLK, nokta_C, cizgi_BC)
        self.add(cizgi_AB, cizgi_BD, nokta_B, cizgi_GF, cember_GLK, cember_GCH, nokta_G, nokta_C, cizgi_BC)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [A, D, E, F, K, L, nokta_L, cizgi_GF, cizgi_AE, cizgi_AD,
                                                          cizgi_AB, cizgi_BD, cember_GLK, nokta_A, nokta_D, nokta_E,
                                                          nokta_F, nokta_K]],
                  *[FadeToColor(i, YELLOW) for i in [B, C, G, cizgi_BC, cizgi_BG, nokta_B, nokta_C, nokta_G]],
                  run_time=1)

        tasıma_q = [cizgi_BC, nokta_B, nokta_C, B, C]
        tasıma_p = [t_cizgi_BC, t_nokta_B_BC, t_nokta_C, t_B_BC, t_C]
        tasıma_r = [cizgi_BG, nokta_B, nokta_G, B, G]
        tasıma_s = [t_cizgi_BG_ust, t_nokta_B_BG, t_nokta_G_BG, t_B_BG, t_G_BG]

        self.play(*[TransformFromCopy(q, p) for q, p in zip(tasıma_q, tasıma_p)],
                  *[TransformFromCopy(r, s) for r, s in zip(tasıma_r, tasıma_s)],
                  run_time=1)
        self.play(*[FadeToColor(i, WHITE) for i in [A, B, C, D, E, F, G, K, L, nokta_A, nokta_B, nokta_C, nokta_D,
                                                    nokta_E, nokta_F, nokta_G, nokta_K, nokta_L, cizgi_GF, cizgi_AE,
                                                    cizgi_AD, cizgi_AB, cizgi_BC, cizgi_BG, cizgi_BD, cember_GLK]],
                  run_time=1)

        self.remove(cizgi_AE, cember_GLK, cember_GCH, nokta_L, nokta_G, cizgi_LE)
        self.add(cizgi_BD, cizgi_LE, cember_GCH, cember_GLK, nokta_L, nokta_G)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [A, B, C, E, F, H, nokta_A, nokta_B, nokta_C, nokta_E, nokta_F,
                                                          nokta_H, cizgi_AB, cizgi_BC, cizgi_LE, cizgi_GF, cember_GCH]],
                  *[FadeToColor(i, YELLOW) for i in [D, L, G, nokta_D, nokta_L, nokta_G, cizgi_DG, cizgi_DL]],
                  run_time=1)

        tasıma_qq = [cizgi_DG, nokta_D, nokta_G, D, G]
        tasıma_pp = [t_cizgi_DG, t_nokta_D_DG, t_nokta_G_DG, t_D_DG, t_G_DG]
        tasıma_rr = [cizgi_DL, nokta_D, nokta_L, D, L]
        tasıma_ss = [t_cizgi_DL, t_nokta_D_DL, t_nokta_L, t_D_DL, t_L]

        self.play(*[TransformFromCopy(qq, pp) for qq, pp in zip(tasıma_qq, tasıma_pp)],
                  *[TransformFromCopy(rr, ss) for rr, ss in zip(tasıma_rr, tasıma_ss)],
                  run_time=1)
        self.play(*[FadeToColor(i, WHITE) for i in [A, B, C, E, F, H, D, L, G, nokta_A, nokta_B, nokta_C, nokta_D,
                                                    nokta_E, nokta_F, nokta_H, nokta_D, nokta_L, nokta_G, cizgi_AB,
                                                    cizgi_BC, cizgi_LE, cizgi_GF, cizgi_DL, cizgi_DG, cember_GCH]],
                  run_time=1)

        self.play(*[Write(i) for i in [t_A, t_B_t_DG]],
                  *[ShowCreation(i) for i in [t_nokta_A, t_nokta_B_t_DG]],
                  run_time=1)

        t_cizgi_DB.set_color(YELLOW)
        t_cizgi_DA.set_color(YELLOW)
        self.add(t_cizgi_DB, t_cizgi_DA, t_cizgi_BG_alt, t_cizgi_AL)

        self.remove(t_cizgi_DG, t_cizgi_DL, t_cizgi_BG_alt, t_cizgi_BG_alt, t_cizgi_AL, cizgi_DL, cizgi_DG, cizgi_BG,
                    cizgi_AL, cizgi_BF, nokta_A, nokta_B, t_nokta_D_DG, t_nokta_D_DL, t_nokta_B_t_DG, t_nokta_A,
                    cizgi_AE, cizgi_AB, nokta_C, cizgi_BD, cember_GCH)
        self.add(cizgi_AE, cizgi_BF, t_cizgi_BG_alt, t_cizgi_AL, nokta_A, nokta_B, t_nokta_D_DG, t_nokta_D_DL,
                 t_nokta_B_t_DG, t_nokta_A, nokta_C, cember_GCH, cizgi_BD, cizgi_AB)
        self.play(*[FadeToColor(i, DARKER_GREY) for i in [C, E, F, G, H, K, L, cizgi_BC, cizgi_LE, cizgi_GF,
                                                          cizgi_AE, cizgi_BF, nokta_C, nokta_E, nokta_F, nokta_G,
                                                          nokta_H, nokta_K, nokta_L, cember_GCH, cember_GLK]],
                  *[FadeToColor(i, ORANGE) for i in [t_D_DG, t_B_t_DG, t_nokta_D_DG, t_nokta_B_t_DG, t_cizgi_DB,
                                                     t_D_DL, t_A, t_nokta_D_DL, t_nokta_A, t_cizgi_DA,
                                                     D, A, B, cizgi_AD, cizgi_BD, nokta_D, nokta_A, nokta_B, cizgi_AB]],
                  run_time=1)

        B_2 = TextMobject("B").next_to(t_D_DG, ORIGIN).set_color(ORANGE)
        B_3 = TextMobject("A").next_to(t_D_DL, ORIGIN).set_color(ORANGE)
        self.play(*[FadeOut(i) for i in [t_cizgi_DB, t_cizgi_DA]],
                  ReplacementTransform(t_D_DG, B_2),
                  ReplacementTransform(t_D_DL, B_3),
                  t_B_t_DG.next_to, t_D_DG, ORIGIN,
                  t_A.next_to, t_D_DL, ORIGIN,
                  t_cizgi_BG_alt.shift, LEFT * self.mesafe_AB4,
                  t_nokta_B_t_DG.shift, LEFT * (self.mesafe_AB4 - 0.05),
                  t_cizgi_AL.shift, LEFT * self.mesafe_AB4,
                  t_nokta_A.shift, LEFT * (self.mesafe_AB4 - 0.05),
                  t_G_DG.shift, LEFT * self.mesafe_AB4,
                  t_nokta_G_DG.shift, LEFT * self.mesafe_AB4,
                  t_L.shift, LEFT * self.mesafe_AB4,
                  t_nokta_L.shift, LEFT * self.mesafe_AB4, run_time=1)

        self.remove(B_2, B_3, t_nokta_D_DL, t_nokta_D_DG)

        self.play(*[FadeToColor(i, YELLOW) for i in [t_B_t_DG, t_A, t_nokta_A, t_nokta_B_t_DG]],
                  *[FadeToColor(i, WHITE) for i in [D, A, B, cizgi_AD, cizgi_BD, cizgi_AB, nokta_D, nokta_A, nokta_B,
                                                    C, E, F, G, H, K, L, cizgi_BC, cizgi_LE, cizgi_GF,
                                                    cizgi_AE, cizgi_BF, nokta_C, nokta_E, nokta_F, nokta_G,
                                                    nokta_H, nokta_K, nokta_L, cember_GCH, cember_GLK]],
                  run_time=1)

        self.play(*[Indicate(i) for i in [t_BC, t_BG_ust]], run_time=1)

        k = [t_B_BG, t_nokta_B_BG, t_G_BG, t_nokta_G_BG, t_cizgi_BG_ust]
        l = [tt_B_BG, tt_nokta_B_BG, tt_G_BG, tt_nokta_G_BG, tt_cizgi_BG]
        m = [t_B_t_DG, t_nokta_B_t_DG, t_G_DG, t_nokta_G_DG, t_cizgi_BG_alt]
        self.play(*[ReplacementTransform(k, l) for k, l in zip(k, l)],
                  *[ReplacementTransform(m, l) for m, l in zip(m, l)], run_time=1)

        self.play(*[Indicate(i) for i in [t_BC, t_AL]], run_time=1)

        kk = [t_B_BC, t_nokta_B_BC, t_C, t_nokta_C, t_cizgi_BC]
        ll = [tt_B_BG, tt_nokta_B_BG, tt_C_BG, tt_nokta_G_BG, tt_cizgi_BG]
        mm = [t_A, t_nokta_A, t_L, t_nokta_L, t_cizgi_AL]
        self.play(*[ReplacementTransform(kk, ll) for kk, ll in zip(kk, ll)],
                  *[ReplacementTransform(mm, ll) for mm, ll in zip(mm, ll)],
                  ReplacementTransform(tt_G_BG, tt_C_BG), run_time=1)
        self.remove(tt_G_BG)

        bc = [B, nokta_B, C, nokta_C, cizgi_BC]
        al = [A, nokta_A, L, nokta_L, cizgi_AL]
        self.play(*[ReplacementTransform(ll, bc) for ll, bc in zip(ll, bc)],
                  *[ReplacementTransform(ll.copy(), al) for ll, al in zip(ll, al)],
                  *[FadeToColor(i, DARKER_GREY) for i in [cember_GLK, cember_GCH, D, E, F, G, H, K, nokta_D, nokta_E,
                                                          nokta_F, nokta_G, nokta_H, nokta_K, cizgi_AD, cizgi_BD,
                                                          cizgi_LE, cizgi_GF,
                                                          cizgi_AE, cizgi_AB, sag_dogrultu, sol_dogrultu,cizgi_BF]],
                  run_time=1)
#3.26
        self.wait(4.5)

        self.play(*[FadeOut(i) for i in [cember_GLK, cember_GCH, A, B, C, D, E, F, G, H, K, L, nokta_A, nokta_B, nokta_C,
                                         nokta_D, nokta_E, nokta_F, nokta_G, nokta_H, nokta_K, nokta_L, cizgi_AD, cizgi_BD,
                                         cizgi_LE, cizgi_GF, cizgi_AE, cizgi_AB, cizgi_BF, cizgi_BC, cizgi_AL,
                                         sag_dogrultu, sol_dogrultu, dogrultusunda]], run_time=1)

        # Geri Dönüş___________________________________________________________________________________________________

        dogrultusunda.move_to(LEFT * 2.5 + UP * 1.5)
        self.add(ihtimaller, dısında, uzerinde, yanlarında, dogrultusunda, uclarında, arasında, A_mesafe_esit,
                 A_mesafe_kucuk, ihtimaller_dısında, ihtimaller_uzerinde, dısında_yanlarında, dısında_dogrultusudna,
                 uzerinde_arasında, uzerinde_uclarında, yanlarında_A_kucuk, A_kucuk_A_esit, A_esit_A_buyuk,
                 A_mesafe_buyuk)

        self.wait(0.5)
        self.play(FadeToColor(dogrultusunda, GREY), run_time=1)
#10.26
        self.play(ShowPassingFlashAround(arasında), run_time=1)
        self.play(FadeToColor(arasında, YELLOW), run_time=1)
        self.wait()
        self.play(FadeToColor(arasında, GREY), run_time=1)

        self.wait(20)

        self.play(*[FadeOut(i) for i in [ihtimaller, dısında, uzerinde, yanlarında, dogrultusunda, uclarında, arasında, A_mesafe_esit,
                 A_mesafe_kucuk, ihtimaller_dısında, ihtimaller_uzerinde, dısında_yanlarında, dısında_dogrultusudna,
                 uzerinde_arasında, uzerinde_uclarında, yanlarında_A_kucuk, A_kucuk_A_esit, A_esit_A_buyuk,
                 A_mesafe_buyuk]])
        self.wait(0.5)

        A, B, C, D, E, F, G, H, K, L = list(map(TextMobject, ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L"]))

        a = LEFT*math.cos(self.acı_AB__x)*self.mesafe_AB + DOWN*math.sin(self.acı_AB__x)*self.mesafe_AB + RIGHT*0.2
        b = ORIGIN + RIGHT*0.2
        c = UP*self.mesafe_BC + RIGHT*0.2
        d = LEFT*math.cos(self.acı_BD__x)*self.mesafe_AB + UP*math.sin(self.acı_BD__x)*self.mesafe_AB + RIGHT*0.2
        e = a + RIGHT*math.cos(PI*2/3-self.acı_AB__x)*(self.mesafe_BC+0.5) + DOWN*math.sin(PI*2/3-self.acı_AB__x)*(self.mesafe_BC+0.5)
        f = RIGHT*math.cos(self.acı_BD__x)*(self.mesafe_BC+0.5) + DOWN*math.sin(self.acı_BD__x)*(self.mesafe_BC+0.5) + RIGHT*0.2
        g = RIGHT*math.cos(self.acı_BD__x)*(self.mesafe_BC) + DOWN*math.sin(self.acı_BD__x)*self.mesafe_BC + RIGHT*0.2
        h = LEFT*math.cos(self.acı_BD__x)*self.mesafe_BC + UP*math.sin(self.acı_BD__x)*self.mesafe_BC + RIGHT*0.2
        l = a + RIGHT*math.cos(PI*2/3-self.acı_AB__x)*(self.mesafe_BC) + DOWN*math.sin(PI*2/3-self.acı_AB__x)*(self.mesafe_BC)

        cember_GCH = Circle(radius=self.mesafe_BC).move_arc_center_to(RIGHT * 0.2)
        cember_GLK = Circle(radius=self.mesafe_AB + self.mesafe_BC)
        cember_GLK.move_arc_center_to(
            LEFT * math.cos(self.acı_BD__x) * self.mesafe_AB + UP * math.sin(
                self.acı_BD__x) * self.mesafe_AB + + RIGHT * 0.2)

        nokta_A = Dot(a)
        nokta_B = Dot(b)
        nokta_C = Dot(c)
        nokta_D = Dot(d)
        nokta_E = Dot(e)
        nokta_F = Dot(f)
        nokta_G = Dot(g)
        nokta_H = Dot(h)
        nokta_K = Dot(cember_GLK.point_from_proportion(0.38))
        nokta_L = Dot(l)

        cizgi_AB = Line(a, b)
        cizgi_BC = Line(b, c)
        r = cizgi_BC.copy()
        rr = Line(d, g)
        cizgi_AD = Line(a, d)
        cizgi_BD = Line(b, d)
        cizgi_BF = Line(b, f)
        cizgi_AE = Line(a, e)
        cizgi_GF = Line(g, f)
        cizgi_BG = Line(b, g)
        cizgi_AL = Line(a, l)
        cizgi_DG = Line(d, g)
        cizgi_DL = Line(d, l)
        cizgi_LE = Line(l, e)
        cizgi_GF = Line(g, f)

        t_cizgi_BC = cizgi_BC.copy().rotate(-PI/2).move_to(LEFT*4.9 + UP*2.8).shift(LEFT*0.5*self.mesafe_AB).set_color(YELLOW)
        t_cizgi_BG_ust = cizgi_BG.copy().rotate(self.acı_BD__x).move_to(LEFT*4.9 + UP*1.8).shift(LEFT*0.5*self.mesafe_AB).set_color(YELLOW)
        tt_cizgi_BG = t_cizgi_BG_ust.copy().shift(DOWN * 1.8)
        t_cizgi_DG = cizgi_DG.copy().rotate(self.acı_BD__x).move_to(LEFT * 4.9 + DOWN * 1.8).set_color(YELLOW)
        t_cizgi_DL = cizgi_DL.copy().rotate(PI*2/3-self.acı_AB__x).move_to(LEFT * 4.9 + DOWN*2.8).set_color(YELLOW)
        t_nokta_B_BC = Dot(t_cizgi_BC.get_start()).set_color(YELLOW)
        t_nokta_B_BG = Dot(t_cizgi_BG_ust.get_start()).set_color(YELLOW)
        tt_nokta_B_BG = Dot(tt_cizgi_BG.get_start()).set_color(YELLOW)
        t_nokta_C = Dot(t_cizgi_BC.get_end()).set_color(YELLOW)
        t_nokta_D_DL = Dot(t_cizgi_DL.get_start()).set_color(YELLOW)
        t_nokta_D_DG = Dot(t_cizgi_DG.get_start()).set_color(YELLOW)
        t_nokta_G_BG = Dot(t_cizgi_BG_ust.get_end()).set_color(YELLOW)
        tt_nokta_G_BG = Dot(tt_cizgi_BG.get_end()).set_color(YELLOW)
        t_nokta_G_DG = Dot(t_cizgi_DG.get_end()).set_color(YELLOW)
        t_nokta_L = Dot(t_cizgi_DL.get_end()).set_color(YELLOW)
        t_nokta_A = Dot().next_to(t_nokta_D_DL, RIGHT, self.mesafe_AB-0.2).set_color(YELLOW)
        t_nokta_B_t_DG = Dot().next_to(t_nokta_D_DG, RIGHT, self.mesafe_AB-0.2).set_color(YELLOW)
        t_A = A.copy().set_color(YELLOW)
        t_B_t_DG = B.copy().set_color(YELLOW)
        t_B_BC = B.copy().set_color(YELLOW)
        t_B_BG = B.copy().set_color(YELLOW)
        tt_B_BG = B.copy().set_color(YELLOW)
        tt_C_BG = C.copy().set_color(YELLOW)
        t_C = C.copy().set_color(YELLOW)
        t_D_DL = D.copy().set_color(YELLOW)
        t_D_DG = D.copy().set_color(YELLOW)
        t_G_BG = G.copy().set_color(YELLOW)
        t_G_DG = G.copy().set_color(YELLOW)
        tt_G_BG = G.copy().set_color(YELLOW)
        t_L = L.copy().set_color(YELLOW)
        t_cizgi_DB = Line(t_nokta_D_DG, t_nokta_B_t_DG).set_color(YELLOW)
        t_cizgi_DA = Line(t_nokta_D_DL, t_nokta_A).set_color(YELLOW)
        t_cizgi_BG_alt = Line(t_nokta_B_t_DG, t_nokta_G_DG).set_color(YELLOW)
        t_cizgi_AL = Line(t_nokta_A, t_nokta_L).set_color(YELLOW)

        t_BC = VGroup(t_B_BC, t_nokta_B_BC, t_C, t_nokta_C, t_cizgi_BC)
        t_AL = VGroup(t_A, t_nokta_A, t_L, t_nokta_L, t_cizgi_AL)
        t_BG_ust = VGroup(t_B_BG, t_nokta_B_BG, t_G_BG, t_nokta_G_BG, t_cizgi_BG_ust)

        A.next_to(nokta_A, LEFT, 0.1)
        B.next_to(nokta_B, UR, 0.1)
        C.next_to(nokta_C, UR, 0.07)
        D.next_to(nokta_D, UL, 0.07)
        E.next_to(nokta_E, LEFT, 0.1)
        F.next_to(nokta_F, RIGHT, 0.1)
        G.next_to(nokta_G, UR, 0.07)
        H.next_to(nokta_H, UL, 0.07)
        L.next_to(nokta_L, UL, 0.07)
        K.next_to(nokta_K, UL, 0.07)
        t_A.next_to(t_nokta_A, UR, 0.05)
        t_B_t_DG.next_to(t_nokta_B_t_DG, UR, 0.05)
        t_B_BC.next_to(t_nokta_B_BC, LEFT, 0.1)
        t_B_BG.next_to(t_nokta_B_BG, LEFT, 0.1)
        tt_B_BG.next_to(tt_nokta_B_BG, LEFT, 0.1)
        t_C.next_to(t_nokta_C, RIGHT, 0.1)
        t_D_DL.next_to(t_nokta_D_DL, LEFT, 0.1)
        t_D_DG.next_to(t_nokta_D_DG, LEFT, 0.1)
        t_G_BG.next_to(t_nokta_G_BG, RIGHT, 0.1)
        tt_G_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        tt_C_BG.next_to(tt_nokta_G_BG, RIGHT, 0.1)
        t_G_DG.next_to(t_nokta_G_DG, RIGHT, 0.1)
        t_L.next_to(t_nokta_L, RIGHT, 0.1)

        self.play(*[Write(i) for i in [A, B, C]],
                  *[ShowCreation(i) for i in [cizgi_BC, nokta_B, nokta_C, nokta_A]],
                  run_time=1)
        self.wait(0.5)
#37.26
        self.play(ShowCreation(cizgi_AB), run_time=1)
        self.play(Write(belit_1), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(belit_1), run_time=1)
#41.26
        self.play(*[ShowCreation(i) for i in [cizgi_AD, cizgi_BD, nokta_D]],
                  Write(D), run_time=1)

        self.wait(3)
#45.26
        cember_GCH.rotate(PI/2)
        r.add_updater(lambda l: l.become(Line(r.get_start(), cember_GCH.get_end())))
        self.add(r)
        self.play(ShowCreation(cember_GCH),
                  Write(belit_3),
                  run_time=1.5)
        self.remove(r)
        self.play(*[ShowCreation(i) for i in [nokta_G, nokta_H]],
                  *[Write(i) for i in [G, H]],
                   FadeOut(belit_3),
                  run_time=1)
        self.wait(5.5)
#53.26
        self.play(*[ShowCreation(i) for i in [cizgi_BF]], run_time=1)
        self.play(*[Write(i) for i in [F]],
                  *[ShowCreation(i) for i in [nokta_F]], run_time=1)
        self.wait()
#56.26
        cember_GLK.rotate(-self.acı_BD__x)
        rr.add_updater(lambda l: l.become(Line(rr.get_start(), cember_GLK.get_end())))
        self.add(rr)
        self.play(ShowCreation(cember_GLK),
                  *[ShowCreation(i) for i in [nokta_K, nokta_L]],
                  *[Write(i) for i in [K, L]], run_time=1.5)
        self.remove(rr)
        self.wait(4.5)
#02.26
        self.play(*[ShowCreation(i) for i in [cizgi_AE]], run_time=1)
        self.play(*[Write(i) for i in [E]],
                  *[ShowCreation(i) for i in [nokta_E]], run_time=1)
        self.wait(7)

        self.remove(cember_GCH, cember_GLK, A, B, C, D, E, F, G, K, L, H, nokta_A, nokta_B, nokta_C, nokta_D, nokta_E,
                    nokta_F, nokta_G, nokta_K, nokta_L, nokta_H, cizgi_AB, cizgi_BD, cizgi_AD, cizgi_BC, cizgi_AE, cizgi_BF)
        self.add(onerme, AB_buyuk_ek)
#11.26
        ret = ÇizikAtmak(AB_buyuk_ek)
        self.play(ShowCreation(ret), run_time=1)

        herhangi1 = TextMobject("\\textsl{herhangi}").next_to(onerme[0], RIGHT * 0.5).shift(DOWN * 0.05)
        herhangi2 = TextMobject("\\textsl{herhangi}").next_to(onerme[2], RIGHT * 0.5).shift(DOWN * 0.05)
        verilen1 = onerme[1].copy().next_to(herhangi1, RIGHT * 0.5)
        verilen2 = onerme[3].copy().next_to(herhangi2, RIGHT * 0.5)

        self.play(ShowCreation(herhangi1, run_time=1.1),
                  ShowCreation(herhangi2, run_time=1.1),
                  ReplacementTransform(onerme[1], verilen1),
                  ReplacementTransform(onerme[3], verilen2),
                  *[FadeOut(i) for i in [ret, AB_buyuk_ek]])
        self.wait(1.5)

        self.play(*[FadeOut(i) for i in [onerme, herhangi1, herhangi2, verilen1, verilen2]], run_time=1)
        self.wait(0.5)
#16.36
        proclus = ImageMobject("proclus_kitap.png")
        tamani = ImageMobject("tamani_kitap.png")
        proclus.scale(4)
        tamani.scale(4)
        self.play(FadeIn(proclus), run_time=1)
        self.wait(3)
        self.play(FadeOut(proclus), run_time=1)
#21.36
        self.play(FadeIn(tamani), run_time=1)
        self.wait(10)
#32.26
        self.play(FadeOut(tamani), run_time=1)
        self.wait(2)

        self.play(RotatingAndMove(moyc, LEFT * 6), run_time=2.5)
        self.wait(2.5)
        self.play(FadeOut(moyc), run_time=1)


class Onerme_III(Scene):

    CONFIG = {
        "uzunluk_AB": 2.5,
        "uzunluk_C": 1.75
    }

    def construct(self):
        # Giriş
        self.wait(.5)
        self.play(VFadeInThenOut(YaşamÇiçeği(), run_time=4.5))

        # Mavi Aşama____________________________________________________________________________________________________
        mayc = MaviYaşamÇiçeği().to_edge(UP)

        self.play(FadeInFrom(mayc, UP * .3), run_time=1)

        onerme = TextMobject("\f Farklı uzunlukta iki doğru-parçası",
                             "\f verildiğinde uzun olandan, kısa olana eşit",
                             "\f bir doğru-parçası çıkarmanın yolu")

        onerme_1 = TextMobject("Önerme 1:"
                               "\f Eşkenar üçgen çizmek")
        onerme_2 = TextMobject("Önerme 2:"
                               "\f Doğru-parçasını taşımak")
        belit_1 = TextMobject("Belit 1: "
                              "\f Herhangi bir noktadan başka herhangi "
                              "\f bir noktaya bir doğru çizilebilir")
        belit_2 = TextMobject("Belit 2:"
                              "\f Bir doğru istenildiği kadar yine bir"
                              "\f doğru olacak şekilde uzatılabilir")
        belit_3 = TextMobject("Belit 3: "
                              "\f Herhangi bir merkez ve"
                              "\f bir uzunluk verildiğinde"
                              "\f bir çember çizilebilir")
        tanım_15 = TextMobject("Tanım 15:"
                               "\f İçindeki bir noktadan  "
                               "\f üzerindeki her noktaya "
                               "\f çizilen doğruların birbirine "
                               "\f eşit olduğu düzlem şekline çember denir")
        ortak_kavramlar_1 = TextMobject("Ortak Kavramlar 1:"
                                        "\f Aynı şeye eşit olan şeyler"
                                        "\f birbirine de eşittir")
        ortak_kavramlar_3 = TextMobject("Ortak Kavramlar 3:"
                                        "\f Eğer eşit şeylerden eşit şeyler"
                                        "\f çıkarılırsa kalanlar da eşittir")

#0--------------------------------------------------------------------------------------

        self.play(RotatingAndMove(mayc, RIGHT * 6),
                  Write(onerme), axis=[0, 0, -1],
                  run_time=2.5)
        self.wait(1)
        self.play(FadeOut(onerme),
                  RotatingAndMove(mayc, LEFT * 6),
                  run_time=2.5)

        # Lacivert Aşama________________________________________________________________________________________________
        lyc = LacivertYaşamÇiçeği().to_edge(UP)

        self.play(ReplacementTransform(mayc, lyc), run_time=1)
        self.wait(0.1)
        self.play(RotatingAndMove(lyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)

        # Kanıt_________________________________________________________________________________________________________

        A, B, C, D, E, F = list(map(TextMobject, ["A", "B", "C", "D", "E", "F"]))
        t_A_DA_alt, t_A_DA_ust, t_A_DA, t_A_AE = list(map(TextMobject, ["A", "A", "A", "A"]))
        t_C, t_D_DA_alt, t_D_DA_ust, t_D_DA, t_E = list(map(TextMobject, ["C", "D", "D", "D", "E"]))

        a = LEFT
        b = a + RIGHT * self.uzunluk_AB
        c1 = LEFT * .75 + UP * 2.25
        c2 = c1 + RIGHT * self.uzunluk_C
        t_d = LEFT * 5.5
        t_a = t_d + RIGHT * self.uzunluk_C

        cember = Circle(radius=self.uzunluk_C).move_arc_center_to(a)

        nokta_A, nokta_B, nokta_C1, nokta_C2, nokta_D, nokta_E, nokta_F = list(map(Dot, [a, b, c1, c2,
                                                                     cember.point_from_proportion(0.3),
                                                                     cember.point_from_proportion(0),
                                                                     cember.point_from_proportion(0.85)]))

        cizgi_C = Line(c1, c2)
        cizgi_AB = Line(a, b)
        cizgi_DA = Line(cember.point_from_proportion(0.3), a)
        cizgi_AE = Line(a, cember.point_from_proportion(0))
        cizgi_EB = Line(cember.point_from_proportion(0), b)
        t_cizgi_DA = Line(t_d, t_a)
        t_cizgi_C = t_cizgi_DA.copy().next_to(t_cizgi_DA, UP, 2.5)
        t_cizgi_DA_ust = t_cizgi_DA.copy().next_to(t_cizgi_DA, UP, 1.5)
        t_cizgi_DA_alt = t_cizgi_DA.copy().next_to(t_cizgi_DA, DOWN, 1.5)
        t_cizgi_AE = t_cizgi_DA.copy().next_to(t_cizgi_DA, DOWN, 2.5)

        t_nokta_A_DA_alt = Dot(t_cizgi_DA_alt.get_end())
        t_nokta_A_DA_ust = Dot(t_cizgi_DA_ust.get_end())
        t_nokta_A_DA = Dot(t_cizgi_DA.get_end())
        t_nokta_A_AE = Dot(t_cizgi_AE.get_start())
        t_nokta_D_DA_alt = Dot(t_cizgi_DA_alt.get_start())
        t_nokta_D_DA_ust = Dot(t_cizgi_DA_ust.get_start())
        t_nokta_D_DA = Dot(t_cizgi_DA.get_start())
        t_nokta_E = Dot(t_cizgi_AE.get_end())
        t_nokta_C1 = Dot(t_cizgi_C.get_start())
        t_nokta_C2 = Dot(t_cizgi_C.get_end())

        A.next_to(nokta_A, LEFT, 0.1)
        B.next_to(nokta_B, RIGHT, 0.1)
        C.next_to(cizgi_C, UP, 0.1)
        D.next_to(nokta_D, UL, 0.03)
        E.next_to(nokta_E, UR, 0.03)
        F.next_to(nokta_F, DR, 0.03)
        t_A_DA_alt.next_to(t_nokta_A_DA_alt, RIGHT, 0.1)
        t_A_DA_ust.next_to(t_cizgi_DA_ust, RIGHT, 0.1)
        t_A_DA.next_to(t_cizgi_DA, RIGHT, 0.1)
        t_A_AE.next_to(t_nokta_A_AE, LEFT, 0.1)
        t_C.next_to(t_cizgi_C, UP, 0.1)
        t_D_DA_alt.next_to(t_nokta_D_DA_alt, LEFT, 0.1)
        t_D_DA_ust.next_to(t_nokta_D_DA_ust, LEFT, 0.1)
        t_D_DA.next_to(t_nokta_D_DA, LEFT, 0.1)
        t_E.next_to(t_nokta_E, RIGHT, 0.1)

        v_cizgi_AE = VGroup(cizgi_AE, nokta_A, A, nokta_E, E)
        v_t_cizgi_AE = VGroup(t_cizgi_AE, t_nokta_A_AE, t_A_AE, t_nokta_E, t_E).set_color(YELLOW)
        v_cizgi_DA = VGroup(cizgi_DA, nokta_D, D, nokta_A, A)
        v_t_cizgi_DA_alt = VGroup(t_cizgi_DA_alt, t_nokta_D_DA_alt, t_D_DA_alt, t_nokta_A_DA_alt, t_A_DA_alt).set_color(YELLOW)
        v_t_cizgi_DA_ust = VGroup(t_cizgi_DA_ust, t_nokta_D_DA_ust, t_D_DA_ust, t_nokta_A_DA_ust, t_A_DA_ust).set_color(YELLOW)
        v_t_cizgi_DA = VGroup(t_cizgi_DA, t_nokta_D_DA, t_D_DA, t_nokta_A_DA, t_A_DA).set_color(YELLOW)
        v_cizgi_C = VGroup(cizgi_C, nokta_C1, nokta_C2, C)
        v_t_cizgi_C = VGroup(t_cizgi_C, t_nokta_C1, t_nokta_C2, t_C).set_color(YELLOW)

        self.play(*[ShowCreation(i) for i in [cizgi_C, cizgi_AB, nokta_A, nokta_B, nokta_C1, nokta_C2]],
                  *[Write(i) for i in [A, B, C]], run_time=1)
        self.wait(10.3)
#20.9

        nokta = nokta_A.copy()
        onerme_2.scale(0.6).next_to(lyc, LEFT, buff=0.2)
        self.play(TransformFromCopy(cizgi_C, cizgi_DA),
                  TransformFromCopy(nokta_C1, nokta_D),
                  TransformFromCopy(nokta_C2, nokta),
                  *[Write(i) for i in [onerme_2]], run_time=1)
        self.play(Write(D), run_time=1)
        self.remove(nokta)
        self.add(nokta_A)
#22.9
        self.play(FadeOut(onerme_2), run_time=1)

        self.play(TransformFromCopy(v_cizgi_DA, v_t_cizgi_DA_ust),
                  TransformFromCopy(v_cizgi_C, v_t_cizgi_C), run_time=1)
        self.wait(0.1)

        cember.rotate(PI + cizgi_DA.get_angle())
        r = Line(a, cember.point_from_proportion(0.3))
        r.add_updater(lambda l: l.become(Line(r.get_start(), cember.get_end())))
        self.add(r)
        belit_3.scale(0.6).next_to(lyc, LEFT, buff=0.2)
#25
        self.play(ShowCreation(cember),
                  *[Write(i) for i in [belit_3]], run_time=1.25)
        self.remove(r)
        self.play(*[ShowCreation(i) for i in [nokta_E, nokta_F]],
                  *[Write(i) for i in [E, F]],
                  FadeOut(belit_3), run_time=1)
#27.25
        self.play(*[Indicate(i) for i in [nokta_A, A]], run_time=1)
        self.remove(cizgi_AB, nokta_E, nokta_D, cember)
        self.add(cizgi_EB, cizgi_AE, cember, nokta_D, nokta_E)
        self.wait(0.5)
        tanım_15.scale(0.6).next_to(lyc, LEFT, buff=0.1).shift(DOWN*0.2 + RIGHT)

        self.play(*[FadeToColor(i, YELLOW) for i in [cizgi_AE, cizgi_DA, nokta_A, nokta_D, nokta_E, A, D, E]],
                  *[FadeToColor(i, DARKER_GREY) for i in [cizgi_C, C, nokta_C1, nokta_C2, cizgi_EB, nokta_B, B]],
                  Write(tanım_15), run_time=1)
        self.wait(0.75)
# 30.5
        self.play(TransformFromCopy(v_cizgi_AE, v_t_cizgi_AE),
                  TransformFromCopy(v_cizgi_DA, v_t_cizgi_DA_alt),
                  FadeOut(tanım_15), run_time=1)

        self.play(*[FadeToColor(i, WHITE) for i in [cizgi_AE, cizgi_DA, nokta_A, nokta_D, nokta_E, A, D, E, cizgi_C, C,
                                                    nokta_C1, nokta_C2, cizgi_EB, nokta_B, B]],
                  run_time=1)
        self.wait(0.5)
#33
        self.play(*[Indicate(i) for i in [v_t_cizgi_C, v_t_cizgi_DA_ust]], run_time=1)
        self.wait(4.5)
#38.5
        self.play(ReplacementTransform(v_t_cizgi_DA_ust, v_t_cizgi_DA),
                  ReplacementTransform(v_t_cizgi_DA_alt, v_t_cizgi_DA), run_time=1)
        self.wait()

        ortak_kavramlar_1.scale(0.6).next_to(lyc, LEFT, buff=0.2)

#40.5
        self.play(ReplacementTransform(v_t_cizgi_C, v_t_cizgi_DA),
                  ReplacementTransform(v_t_cizgi_AE, v_t_cizgi_DA),
                  Write(ortak_kavramlar_1), run_time=1)
        self.wait(1.5)

        self.remove(nokta_E)
#43
        self.play(ReplacementTransform(v_t_cizgi_DA, v_cizgi_C),
                  ReplacementTransform(v_t_cizgi_DA.copy(), v_cizgi_AE),
                  *[FadeToColor(i, DARKER_GREY) for i in [cember, D, F, B, nokta_D, nokta_F, nokta_B, cizgi_DA, cizgi_EB]],
                  nokta_E.add,
                  FadeOut(ortak_kavramlar_1), run_time=1)
        self.wait(4.5)

        self.play(*[FadeOut(i) for i in [cember, D, F, nokta_D, nokta_F, cizgi_DA, v_cizgi_C, v_cizgi_AE, cizgi_EB,
                                         nokta_B, B]], run_time=1)
#49.5
        self.play(RotatingAndMove(lyc, LEFT * 6), run_time=2.5)
        self.wait(10.5)

#1:02.5
        self.play(FadeOut(lyc), run_time=1)
        self.wait(0.5)


class Onerme_IV(Scene):

    CONFIG = {
        "mayc": MaviYasamCicegi().to_edge(UP),
        "lyc": LacivertYasamCicegi().to_edge(UP),
        "moyc": MorYasamCicegi().to_edge(UP),

        "a": UP * 1.25 + LEFT * 1.2,
        "b": DOWN + LEFT * 1.5 + LEFT * 1.2,
        "c": DOWN + RIGHT * .5 + LEFT * 1.2,
        "d": UP * 1.25 + LEFT * 1.2 + RIGHT * 3.1,
        "e": DOWN + LEFT * 1.5 + LEFT * 1.2 + RIGHT * 3.1,
        "f": DOWN + RIGHT * .5 + LEFT * 1.2 + RIGHT * 3.1,

        "renk_AB": [BLUE_D, BLUE_B],
        "renk_AC": [BLUE_E, BLUE_D],
        "renk_BC": [BLUE_E, DARK_BLUE],
        "renk_acı_A": PURPLE_C,
        "renk_acı_B": PINK,
        "renk_acı_C": LIGHT_PINK,

        "mesafe_AB_2": 0.7,
        "mesafe_BC_2": 2.4,
        "acı_AB_2__x": 35 * DEGREES,
        "acı_BD_2__x": 25 * DEGREES,

        "uzunluk_AB_3": 2.5,
        "uzunluk_C_3": 1.75,
    }

#   [RENK_D, RENK_B] olacak şekilde yeni renk paletleri belirle.

    def construct(self):
        self.wait(0.1)
        self.giris()
        self.mavi_asama()
        self.lacivert_asama()
        self.mor_asama()
        self.hata_ilk_cumle()
        self.hata_ikinci_cumle()
        self.hilbert()
        self.ah_euclid_ah()
        self.cikis()

    def giris(self):

        hilbert_soz = TextMobject("\\textit{Matematiksel bir teori, yolda tanıştığın ilk kişiye açıklayabileceğin"
                                  "\f kadar net yapılmadıkça tamamlanmış sayılmaz."
                                  "\f -David Hilbert}").scale(0.8).move_to(DOWN*2.3)
        self.wait(.5)
        self.play(VFadeInThenOut(YasamCicegi().scale(0.8).move_to(UP)),
                  VFadeInThenOut(hilbert_soz),
                  run_time=4)
        self.wait()

    def mavi_asama(self):
        self.play(FadeInFrom(self.mayc, UP * .3), run_time=1)
        self.wait()
        self.play(RotatingAndMove(self.mayc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait()

        Hilbert = ImageMobject("hilbert.jpg").move_to(LEFT*1.6).scale(2)
        Grundlagen_der_Geometrie = ImageMobject("grundlagen.jpg").move_to(RIGHT*1.6).scale(2)
        self.play(FadeIn(Hilbert))
        self.wait(0.3)
        self.play(FadeIn(Grundlagen_der_Geometrie))
        self.wait(0.3)

        self.play(*[FadeOut(i) for i in [Hilbert, Grundlagen_der_Geometrie]])
        self.wait()

        onerme = TextMobject(
            "Eğer iki üçgenin karşılıklı iki kenarı ve bu eşit kenarlar"
            "\f arasındaki açıları birbirine eşitse üçüncü kenarları da"
            "\f birbirine eşit olur. Üçgenler bu durumda eşittir ve"
            "\f kalan açılar da birbirine eşittir. Yani eşit kenarların"
            "\f karşılarındaki açılar birbirine eşit olur.")

        self.play(Write(onerme), run_time=3.5)
        self.wait()
        self.play(FadeOut(onerme))
        self.wait(0.2)

        self.play(RotatingAndMove(self.mayc, LEFT * 6), run_time=2.5)
        self.wait()

    def lacivert_asama(self):
        self.play(ReplacementTransform(self.mayc, self.lyc), run_time=1)
        self.play(RotatingAndMove(self.lyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait()

        belit_1_ek = TextMobject("Belit 1 Ek:"
                                 "\f Verilmiş iki noktayı"
                                 "\f içeren sadece tek bir"
                                 "\f doğru vardır").scale(0.57)
        ortak_kavramlar_4 = TextMobject("Ortak Kavram 4:",
                                        "\f Birbiriyle örtüşen şeyler"
                                        "\f birbirine eşittirler").scale(0.6)

        belit_1_ek.next_to(self.lyc, LEFT, buff=0.2)
        ortak_kavramlar_4.next_to(self.lyc, LEFT, buff=0.2)

        nokta_A, nokta_B, nokta_C, nokta_D, nokta_E, nokta_F = list(map(Dot, [self.a, self.b, self.c, self.d, self.e, self.f]))
        A, B, C, D, E, F = list(map(TextMobject, ["A", "B", "C", "D", "E", "F"]))

        cizgi_AB = Line(self.a, self.b)
        cizgi_AC = Line(self.a, self.c)
        cizgi_BC = Line(self.b, self.c)
        cizgi_DE = Line(self.d, self.e)
        cizgi_DF = Line(self.d, self.f)
        cizgi_EF = Line(self.e, self.f)

        acı_A = Arc(cizgi_AB.get_angle(), cizgi_AC.get_angle() - cizgi_AB.get_angle(), radius=0.4) \
            .move_arc_center_to(self.a).set_color(self.renk_acı_A)
        acı_B = Arc(cizgi_BC.get_angle(), PI + cizgi_AB.get_angle(), radius=0.4) \
            .move_arc_center_to(self.b).set_color(self.renk_acı_B)
        acı_C = Arc(PI - cizgi_BC.get_angle(), cizgi_AC.get_angle(), radius=0.4) \
            .move_arc_center_to(self.c).set_color(self.renk_acı_C)
        acı_D = Arc(cizgi_DE.get_angle(), cizgi_DF.get_angle() - cizgi_DE.get_angle(), radius=0.4)\
            .move_arc_center_to(self.d).set_color(self.renk_acı_A)
        acı_E = Arc(cizgi_EF.get_angle(), PI + cizgi_DE.get_angle(), radius=0.4) \
            .move_arc_center_to(self.e).set_color(self.renk_acı_B)
        acı_F = Arc(PI - cizgi_EF.get_angle(), cizgi_DF.get_angle(), radius=0.4) \
            .move_arc_center_to(self.f).set_color(self.renk_acı_C)

        yay_BC = ArcBetweenPoints(self.b, self.c, TAU/9).shift(RIGHT*1.6).set_color(self.renk_BC)

        A.next_to(nokta_A, UP, 0.05)
        B.next_to(nokta_B, LEFT, 0.05)
        C.next_to(nokta_C, RIGHT, 0.05)
        D.next_to(nokta_D, UP, 0.05)
        E.next_to(nokta_E, LEFT, 0.05)
        F.next_to(nokta_F, RIGHT, 0.05)

        ucgen_BAC = VGroup(A, B, C, cizgi_AB, cizgi_AC, cizgi_BC, nokta_A, nokta_B, nokta_C)
        ucgen_EDF = VGroup(D, E, F, cizgi_DE, cizgi_DF, cizgi_EF, nokta_D, nokta_E, nokta_F)

        self.play(*[Write(i) for i in [A, B, C, D, E, F]],
                  *[ShowCreation(i) for i in [cizgi_AB, cizgi_AC, cizgi_BC, cizgi_DE, cizgi_DF, cizgi_EF, nokta_A,
                                              nokta_B, nokta_C, nokta_D, nokta_E, nokta_F]])

        self.play(*[FadeToColor(i, self.renk_AB) for i in [cizgi_AB, cizgi_DE]])
        self.play(*[FadeToColor(i, self.renk_AC) for i in [cizgi_AC, cizgi_DF]])
        self.remove(ucgen_BAC, ucgen_EDF)
        self.play(*[ShowCreation(i) for i in [acı_A, acı_D]],
                  *[i.add for i in [ucgen_BAC, ucgen_EDF]])
        self.wait(0.5)

        self.play(*[FadeToColor(i, self.renk_BC) for i in [cizgi_BC, cizgi_EF]])
        self.remove(ucgen_BAC, ucgen_EDF)
        self.play(*[ShowCreation(i) for i in [acı_B, acı_E]],
                  *[i.add for i in [ucgen_BAC, ucgen_EDF]])
        self.remove(ucgen_BAC, ucgen_EDF)
        self.play(*[ShowCreation(i) for i in [acı_C, acı_F]],
                  *[i.add for i in [ucgen_BAC, ucgen_EDF]])
        self.play(*[FadeOut(i) for i in [acı_B, acı_C, acı_E, acı_F]])

        self.play(ucgen_BAC.shift, RIGHT*3.1,
                  acı_A.shift, RIGHT*3.1,
                  A.next_to, nokta_D, UL*0.05,
                  D.next_to, nokta_D, UR*0.05,
                  B.next_to, nokta_E, UL*0.05,
                  E.next_to, nokta_E, DL*0.05,
                  C.next_to, nokta_F, UR*0.05,
                  F.next_to, nokta_F, DR*0.05)
        self.wait(0.5)

        self.play(ucgen_BAC.shift, LEFT*1.5,
                  ucgen_EDF.shift, LEFT*1.5,
                  acı_A.shift, LEFT*1.5,
                  acı_D.shift, LEFT*1.5)
        self.wait(0.2)

        self.play(Flash(nokta_A))
        self.wait(0.1)

        self.play(FadeToColor(cizgi_DE, WHITE), run_time=0.5)
        self.play(FadeToColor(cizgi_DE, self.renk_AB), run_time=0.5)
        self.wait(0.1)

        self.play(Flash(nokta_B))
        self.wait(0.1)

        self.play(FadeToColor(cizgi_DF, WHITE), run_time=0.5)
        self.play(FadeToColor(cizgi_DF, self.renk_AC), run_time=0.5)
        self.wait(0.1)

        self.play(FadeToColor(acı_D, WHITE), run_time=0.5)
        self.play(FadeToColor(acı_D, self.renk_acı_A), run_time=0.5)
        self.wait(0.1)

        self.play(Flash(nokta_C))
        self.wait(0.1)

        self.play(Flash(nokta_B))
        self.wait(0.1)

        self.play(FadeToColor(cizgi_EF, WHITE), run_time=0.5)
        self.play(FadeToColor(cizgi_EF, self.renk_BC), run_time=0.5)
        self.wait(0.1)

        self.remove(nokta_E, nokta_F, nokta_B, nokta_C)
        self.play(*[ShowCreationThenFadeOut(i) for i in [belit_1_ek, yay_BC]],
                  *[i.add for i in [nokta_E, nokta_F, nokta_B, nokta_C]],
                  run_time=3)
        self.wait(0.1)

        self.play(Write(ortak_kavramlar_4))
        self.wait()
        self.play(FadeOut(ortak_kavramlar_4))

        acı_B.shift(RIGHT*1.6)
        acı_C.shift(RIGHT*1.6)
        acı_E.shift(LEFT*1.5)
        acı_F.shift(LEFT*1.5)

        self.play(*[FadeToColor(i, self.renk_BC) for i in [cizgi_BC, cizgi_EF]])

        self.remove(cizgi_EF, cizgi_DE, cizgi_AB, cizgi_BC, nokta_A, nokta_B, nokta_C, nokta_D, nokta_E, nokta_F)
        self.play(*[ShowCreation(i) for i in [acı_B, acı_E]],
                  *[i.add for i in [cizgi_EF, cizgi_DE, cizgi_AB, cizgi_BC, nokta_A, nokta_B, nokta_C, nokta_D, nokta_E,
                                    nokta_F]])
        self.remove(cizgi_EF, cizgi_BC, cizgi_DF, cizgi_AC, nokta_A, nokta_B, nokta_C, nokta_D, nokta_E, nokta_F)
        self.play(*[ShowCreation(i) for i in [acı_C, acı_F]],
                  *[i.add for i in [cizgi_EF, cizgi_BC, cizgi_DF, cizgi_AC, nokta_A, nokta_B, nokta_C, nokta_D, nokta_E,
                                    nokta_F]])

        self.play(*[FadeOut(i) for i in [ucgen_EDF, ucgen_BAC, acı_B, acı_E, acı_C, acı_F, acı_A, acı_D]])

        self.play(RotatingAndMove(self.lyc, LEFT * 6), run_time=2.5)
        self.wait()

    def mor_asama(self):
        self.play(ReplacementTransform(self.lyc, self.moyc), run_time=1)
        self.play(RotatingAndMove(self.moyc, RIGHT * 6), axis=[0, 0, -1], run_time=2.5)
        self.wait()

    def hata_ilk_cumle(self):

        ilk_cumle = TextMobject("...ABC üçgeni DEF üçgeni üzerine yerleştirildiğinde, ve A noktası",
                                "\f D noktasına kondurulduğunda, ve ", "AB doğrusu da DE’nin üzerine ",
                                "\f konduğunda;", "\r AB, DE’ye eşit olduğundan", "\r B noktası E ile çakışır... ").scale(0.75)
        karşıt_ortak_kavram_4 = TextMobject("Birbirine eşit şeyler birbiriyle örtüşür").scale(0.75)
        ortak_kavram_4 = TextMobject("Ortak Kavram 4:", "\r Birbiriyle örtüşen şeyler birbirine eşittirler").scale(0.75)
        kok4 = TextMobject("Karşıt Ortak Kavram 4: ")
        tanım_1 = TextMobject("Nokta: Parçası olmayıp konumu olandır").scale(0.75)
        belit_1_ek = TextMobject("\\textbf{Belit 1 Ek:}"
                                 "\r Verilmiş iki noktayı içeren sadece"
                                 "\r tek bir doğru vardır"
                                 "\r veya"
                                 "\f Eğer iki doğru ortak iki noktaya "
                                 "\r sahipse çakışıklardır").scale(0.75)
        belit_2_ek = TextMobject("\\textbf{Belit 2 Ek:}"
                                 "\r İki doğru ortak bir parçaya sahip"
                                 "\r olamaz").scale(0.75)
        ortak_kavramlar_5 = TextMobject("\\textbf{Ortak Kavramlar 5:}"
                                        "\r Bütün, parçalarından büyüktür").scale(0.75)
        Özdeşlik_İlkesi = TextMobject("Özdeşlik İlkesi: Her şey kendisiyle aynıdır").scale(0.75)
        onerme_3 = TextMobject("Önerme 3:"
                               "\f Verilen uzunlukta çizgiyi kesmek").scale(0.6)

        onerme_3.next_to(self.moyc, LEFT, buff=0.2)

        nokta_A, nokta_B, nokta_C, nokta_D, nokta_E, nokta_F = list(map(Dot, [self.a, self.b, self.c, self.d, self.e, self.f]))
        A, B, C, D, E, F = list(map(TextMobject, ["A", "B", "C", "D", "E", "F"]))

        cizgi_AB = Line(self.a, self.b)
        cizgi_AC = Line(self.a, self.c)
        cizgi_BC = Line(self.b, self.c)
        cizgi_DE = Line(self.d, self.e)
        cizgi_DF = Line(self.d, self.f)
        cizgi_EF = Line(self.e, self.f)

        A.next_to(nokta_A, UP, 0.05)
        B.next_to(nokta_B, LEFT, 0.05)
        C.next_to(nokta_C, RIGHT, 0.05)
        D.next_to(nokta_D, UP, 0.05)
        E.next_to(nokta_E, LEFT, 0.05)
        F.next_to(nokta_F, RIGHT, 0.05)

        ucgen_BAC = VGroup(A, B, C, cizgi_AB, cizgi_AC, cizgi_BC, nokta_A, nokta_B, nokta_C)
        ucgen_EDF = VGroup(D, E, F, cizgi_DE, cizgi_DF, cizgi_EF, nokta_D, nokta_E, nokta_F)

        self.play(Write(ilk_cumle))
        self.wait()

        alt_çizgi = Line(ilk_cumle[3], ilk_cumle[5], buff=0.1).next_to(ilk_cumle[4], DOWN, 0.05).set_color(YELLOW)
        alt_çizgi.add_updater(lambda l: l.next_to(ilk_cumle[4], DOWN, 0.05))

        self.play(ShowCreation(alt_çizgi))
        self.wait(0.5)

        self.play(ilk_cumle.shift, UP*1.5)
        self.play(Write(karşıt_ortak_kavram_4))
        self.wait(0.5)

        self.play(ilk_cumle.shift, UP * .7,
                  karşıt_ortak_kavram_4.shift, UP * .7)
        self.play(Write(ortak_kavram_4))
        kok4.next_to(karşıt_ortak_kavram_4, LEFT, 0.2).scale(0.75).shift(RIGHT*2)
        self.play(Write(kok4),
                  karşıt_ortak_kavram_4.shift, RIGHT*1.3, run_time=1.2)
        self.wait(0.2)

        ekran = Rectangle(fill_opacity=1, color=BLACK).scale(10)
        l1 = Line(ORIGIN, RIGHT)
        l1.move_to(LEFT * 3 + UP * .75)
        l2 = Line(ORIGIN, RIGHT).move_to(LEFT * 3 + DOWN * .75)
        açı1 = VGroup(l1.copy(), l1.copy().rotate(PI/3, about_point=l1.get_start() + RIGHT*0.015)).move_to(UP * .75)
        açı2 = VGroup(l1.copy(), l1.copy().rotate(PI/3, about_point=l1.get_start() + RIGHT*0.015)).move_to(DOWN * .75)
        yay1 = Arc(PI/4, PI/2).move_to(RIGHT*3 + UP*.75)
        yay2 = Arc(PI/4, PI/2).move_to(RIGHT*3 + DOWN*.75)

        self.add(ekran, l1, l2, açı1, açı2, yay1, yay2, self.moyc)
        self.play(l2.shift, UP * 1.5,
                  açı2.shift, UP * 1.5,
                  yay2.shift, UP * 1.5)
        self.wait(0.5)

        self.add(ekran, self.moyc)

        # I. Önerme'ye değiniş__________________________________________________________________________________________

        nokta_AA, nokta_BB, nokta_CC, nokta_DD, nokta_EE = list(
            map(Dot, [LEFT, RIGHT, UP * 1.732, LEFT * 2 + UP * 1.732, RIGHT * 2 + UP * 1.732]))
        AA, BB, CC, DD, EE = list(map(TextMobject, ["A", "B", "C", "D", "E"]))
        çember_AA = Circle(radius=2).move_to(LEFT)
        cember_BB = Circle(radius=2).move_to(RIGHT).rotate(PI, [0, -1, 0])
        cizgi_AABB = Line(nokta_AA, nokta_BB)
        r = cizgi_AABB.copy()
        çizgi_BBAA = Line(nokta_BB, nokta_AA)
        cizgi_CCFF = Line(nokta_CC, UP)
        cizgi_FFAA = Line(UP, nokta_AA)
        cizgi_FFBB = Line(UP, nokta_BB)

        AA.next_to(nokta_AA, LEFT, 0.1)
        BB.next_to(nokta_BB, RIGHT, 0.1)
        CC.next_to(nokta_CC, UP, 0.1)
        DD.next_to(nokta_DD, UL, 0.1)
        EE.next_to(nokta_EE, UR, 0.1)

        r.add_updater(lambda l: l.become(Line(r.get_start(), çember_AA.get_end())))
        çizgi_BBAA.add_updater(lambda l: l.become(Line(çizgi_BBAA.get_start(), cember_BB.get_end())))

        self.play(*[ShowCreation(i) for i in [cizgi_AABB, nokta_AA, nokta_BB]],
                  *[Write(j) for j in [AA, BB]], run_time=1)
        self.add(r, çizgi_BBAA)
        self.play(*[ShowCreation(i) for i in [çember_AA, cember_BB, nokta_CC]],
                  Write(CC), run_time=1.5)
        self.remove(r, çizgi_BBAA)
        self.play(ShowCreation(cizgi_CCFF), rate_func=rush_into, run_time=0.5)
        self.play(*[ShowCreation(i) for i in [cizgi_FFAA, cizgi_FFBB]], rate_func=rush_from, run_time=1)
        self.wait(0.1)

        self.play(*[FadeOut(i) for i in [çember_AA, cember_BB, cizgi_FFBB, cizgi_AABB, cizgi_FFAA, cizgi_CCFF, nokta_AA,
                                         nokta_BB, nokta_CC, AA, BB, CC]])

        # Russell_______________________________________________________________________________________________________

        ilk_cumle.move_to(ORIGIN)
        self.remove(ilk_cumle, alt_çizgi)
        self.play(FadeInFrom(ilk_cumle, UP))
        self.wait(0.5)

        alt_çizgi_2 = Line(color=YELLOW)
        alt_çizgi_2.next_to(ilk_cumle[2], DOWN, 0.05).set_length(5.1)
        alt_çizgi_3 = Line(color=YELLOW)
        alt_çizgi_3.next_to(ilk_cumle[3], DOWN, 0.05).set_length(2.1)

        self.play(ShowCreation(alt_çizgi_2), rate_func=rush_into)
        self.play(ShowCreation(alt_çizgi_3), rate_func=rush_from)
        self.wait(0.1)

        self.remove(ilk_cumle, alt_çizgi_2, alt_çizgi_3)

        cizgi_DE_1 = cizgi_AB.copy()
        self.add(ucgen_EDF, ucgen_BAC)
        self.play(cizgi_DE_1.shift, RIGHT * (0.5), run_time=3.5, rate_func=rush_into)
        #       RIGHT * (x) Toplam x = 3.1 olmalıdır. run_time=t Toplam t = ..Taşıma boyunca....geçersiz hamledir...
        tanım_1.move_to(DOWN * 1.5)
        self.play(FadeInFrom(tanım_1, DOWN, rate_func=smooth),
                  ucgen_BAC.shift, UP,
                  ucgen_EDF.shift, UP,
                  cizgi_DE_1.shift, RIGHT * (0.1) + UP, run_time=0.4, rate_func=linear)
        self.play(cizgi_DE_1.shift, RIGHT * (1.1), run_time=4.4,
                  rate_func=linear)
        Özdeşlik_İlkesi.move_to(DOWN * 1.5)
        self.play(FadeInFrom(Özdeşlik_İlkesi, DOWN, rate_func=smooth),
                  FadeOutAndShift(tanım_1, UP),
                  cizgi_DE_1.shift, RIGHT * (0.1), run_time=0.4, rate_func=linear)
        self.play(cizgi_DE_1.shift, RIGHT * (1.3), run_time=8, rate_func=rush_from)  # Bu komut son bekleme süresidir.
        self.wait()
        self.remove(cizgi_DE_1)
        self.play(FadeOut(Özdeşlik_İlkesi),
                  ucgen_BAC.shift, DOWN,
                  ucgen_EDF.shift, DOWN)

        self.play(*[Indicate(i) for i in [nokta_B, nokta_E]])
        self.wait()

        self.play(*[FadeOut(i) for i in [D, E, F, cizgi_DE, cizgi_DF, cizgi_EF, nokta_D, nokta_E, nokta_F]])
        dogru_cizgi_DE = cizgi_DE.copy().scale(8)
        self.play(*[ShowCreation(i) for i in [nokta_D, nokta_E]],
                  ShowCreation(dogru_cizgi_DE, run_time=1.75))
        cizgi_DE_2 = cizgi_DE.copy().set_color(self.renk_AB)
        nokta_D_2 = nokta_D.copy().set_color(self.renk_AB)
        nokta_E_2 = nokta_E.copy().set_color(self.renk_AB)
        self.play(Write(onerme_3),
                  TransformFromCopy(cizgi_AB, cizgi_DE_2),
                  TransformFromCopy(nokta_A, nokta_D_2),
                  TransformFromCopy(nokta_B, nokta_E_2),
                  FadeToColor(cizgi_AB, self.renk_AB))
        self.play(FadeOut(onerme_3))
        self.wait()

        self.play(*[FadeOut(i) for i in [dogru_cizgi_DE, nokta_D, nokta_E, cizgi_DE_2, nokta_D_2, nokta_E_2]])
        belit_1_ek.move_to(DOWN*1.75)
        belit_2_ek.next_to(belit_1_ek.get_left() + DOWN*.7, buff=0)
        ortak_kavramlar_5.next_to(belit_1_ek.get_left() + DOWN*1.2, buff=0)
        self.play(*[FadeInFrom(i, DOWN) for i in [belit_1_ek, belit_2_ek, ortak_kavramlar_5]])
        self.wait()

        ekran_c = ekran.copy()
        self.add(ekran_c, self.moyc)
        cizgi_AB.set_color(WHITE)

    def hata_ikinci_cumle(self):

        ikinci_cümle = TextMobject("AB, DE ile çakıştığında AC doğrusu da DF ile çakışır ",
                                   "\f çünkü BAC açısı EDF açısına eşittir").scale(0.75)
        üçüncü_cümle = TextMobject("AC, DF’ye eşit olduğundan,", "\r C noktası da F noktasıyla çakışacaktır").scale(0.75)

        nokta_A, nokta_B, nokta_C, nokta_D, nokta_E, nokta_F = list(
            map(Dot, [self.a, self.b, self.c, self.d, self.e, self.f]))
        A, B, C, D, E, F = list(map(TextMobject, ["A", "B", "C", "D", "E", "F"]))

        cizgi_AB = Line(self.a, self.b)
        cizgi_AC = Line(self.a, self.c)
        cizgi_BC = Line(self.b, self.c)
        cizgi_DE = Line(self.d, self.e)
        cizgi_DF = Line(self.d, self.f)
        cizgi_EF = Line(self.e, self.f)

        acı_A = Arc(cizgi_AB.get_angle(), cizgi_AC.get_angle() - cizgi_AB.get_angle(), radius=0.4) \
            .move_arc_center_to(self.a).set_color(self.renk_acı_A)
        acı_D = Arc(cizgi_DE.get_angle(), cizgi_DF.get_angle() - cizgi_DE.get_angle(), radius=0.4) \
            .move_arc_center_to(self.d).set_color(self.renk_acı_A)

        A.next_to(nokta_A, UP, 0.05)
        B.next_to(nokta_B, LEFT, 0.05)
        C.next_to(nokta_C, RIGHT, 0.05)
        D.next_to(nokta_D, UP, 0.05)
        E.next_to(nokta_E, LEFT, 0.05)
        F.next_to(nokta_F, RIGHT, 0.05)

        ucgen_BAC = VGroup(A, B, C, cizgi_AB, cizgi_AC, cizgi_BC, nokta_A, nokta_B, nokta_C)
        ucgen_EDF = VGroup(D, E, F, cizgi_DE, cizgi_DF, cizgi_EF, nokta_D, nokta_E, nokta_F)

        l1 = Line(ORIGIN, RIGHT)
        l1.move_to(LEFT * 3 + UP * .75)
        l2 = Line(ORIGIN, RIGHT).move_to(LEFT * 3 + DOWN * .75)
        açı1 = VGroup(l1.copy(), l1.copy().rotate(PI * 0.6666, about_point=l1.get_start() + RIGHT * 0.015)).move_to(UP * .75)
        açı2 = VGroup(l1.copy(), l1.copy().rotate(PI / 3, about_point=l1.get_start() + RIGHT * 0.015)).move_to(
            DOWN * .75)

        self.play(Write(ikinci_cümle))

        alt_çizgi = Line(ikinci_cümle[1].get_left(), ikinci_cümle[1].get_right(), buff=0).next_to(ikinci_cümle[1], DOWN, 0.05).set_color(YELLOW)
        alt_çizgi.add_updater(lambda l: l.next_to(ikinci_cümle[1], DOWN, 0.05))

        alt_çizgi_2 = Line(üçüncü_cümle[0].get_left(), üçüncü_cümle[0].get_right(), buff=0).next_to(üçüncü_cümle[0], DOWN, 0.05).set_color(YELLOW)

        self.play(ShowCreation(alt_çizgi))
        self.wait()

        self.remove(ikinci_cümle, alt_çizgi)
        self.add(acı_A, ucgen_BAC, ucgen_EDF)
        cizgi_DE_1 = cizgi_DE.copy()
        cizgi_DF_1 = cizgi_DF.copy()
        acı_D_1 = acı_D.copy()

        p = [acı_A, cizgi_AB, cizgi_AC]
        q = [acı_D_1, cizgi_DE_1, cizgi_DF_1]
        self.play(*[TransformFromCopy(k, l) for k, l in zip(p, q)])
        self.wait()
        self.remove(cizgi_DE_1, cizgi_DF_1)

        self.remove(ucgen_EDF, ucgen_BAC, acı_A, acı_D_1)
        self.add(açı1, açı2)
        self.wait()
        açı2_1 = açı2.copy()
        self.play(TransformFromCopy(açı1, açı2_1))
        self.remove(açı2_1)
        self.wait()
        self.play(*[FadeOut(i) for i in [açı1, açı2]])

        self.play(FadeInFrom(ikinci_cümle, DOWN))
        self.wait()
        self.play(FadeOut(ikinci_cümle))

        self.play(Write(üçüncü_cümle))
        self.play(ShowCreation(alt_çizgi_2))
        self.wait()
        self.play(*[FadeOut(i) for i in [üçüncü_cümle, alt_çizgi_2]])
        self.wait()

        ekran = EkraniOrt()
        self.add(ekran, self.moyc)

    def hilbert(self):

        tanım_ışın = TextMobject(
            "Işın, bir doğru üzerindeki bir \\textit{P} noktası ile bu doğru üzerinde \\textit{P}'nin aynı"
        )
        tanım_ışın_d = TextMobject(
            "yanında kalan tüm noktalara denir"
        )
        tanım_açı = TextMobject(
            "$ \\alpha $", "\r herhangi bir düzlem;", "\r \\textit{h},", "\r \\textit{k}", ";", "\r $ \\alpha $",
            "\r düzleminde bulunan ve iki farklı doğrunun"
            "\f parçalarını oluşturmak üzere", "\r \\textit{P}", "\r noktasından yayılan herhangi iki ayrı ışın"
        )

        tanım_açı_d = TextMobject(
            "olsun. Bu iki", "\r \\textit{h},", "\r \\textit{k}",
            "\r ışınının oluşturduğu sistemi açı olarak adlandırırz. [...]"
        )

        belit_IV_4_d_0 = TextMobject("Belit IV.4:")
        belit_IV_4_d_1 = TextMobject(
            "(", "\\textit{h}", ",", "\r \\textit{k}", ") açısı", "\r $ \\alpha $", "\r düzleminde;",
            "\r \\textbf{\\textit{a'}}", "\r doğrusu", "\r $ \\alpha $'", "\r düzleminde verilmiş olsun.", "\r Ayrıca"
            "\f diyelim ki", "\r $ \\alpha $'", "\r düzleminde,", "\r \\textbf{\\textit{a'}}",
            "\r doğrusunun belirli bir parçası atansın.", "\r Bunu,",
            "\f \\textbf{\\textit{a'}}", "\r doğrusunun", "\r \\textbf{\\textit{P'}}", "\r noktasından yayılan",
            "\r \\textit{h'}", "\r ışını olarak gösterilsin.", "\r O halde", "\r $ \\alpha $'",
            "\r düzleminde (", "\\textit{h}", ",", "\r \\textit{k}", ")",
            "\r açısını (", "\\textit{h'}", ",", "\r \\textit{k'}", ")",
            "\r açısına eşit kılacak biricik", "\r \\textit{k'}", "\r ışını vardır. [...]"
        )

        h_k_açısı = TextMobject("$ \\angle $(", "\\textit{h}", ",", "\r \\textit{k}", ")")
        k_h_açısı = TextMobject("$ \\angle $(", "\\textit{k}", ",", "\r \\textit{h}", ")")
        h_k_eşittir_h_üssü_k_üssü = TextMobject(
            "$ \\angle $(", "\\textit{h}", ",", "\r \\textit{k}", ")",
            "\r $ \\equiv $",
            "\r $ \\angle $(", "\\textit{h'}", ",", "\r \\textit{k'}", ")"
        )
        h_k_eşittir_h_k = TextMobject(
            "$ \\angle $(", "\\textit{h}", ",", "\r \\textit{k}", ")",
            "\r $ \\equiv $",
            "\r $ \\angle $(", "\\textit{h}", ",", "\r \\textit{k}", ")"
        )
        h_k_eşittir_h_k_çift_üssü = TextMobject(
            "$ \\angle $(", "\\textit{h''}", ",", "\r \\textit{k''}", ")",
            "\r $ \\equiv $",
            "\r $ \\angle $(", "\\textit{h}", ",", "\r \\textit{k}", ")"
        )
        belit_IV_5_d_0 = TextMobject("Belit IV.5:")
        belit_IV_6_d_0 = TextMobject("Belit IV.6:")
        belit_IV_6_d_1 = TextMobject(
            "Eğer \\textit{ABC} ve \\textit{A'B'C'} üçgenlerinde,"
        )
        belit_IV_6_d_2 = TextMobject(
            "\\textit{AB}", "\r $ \\equiv $", "\r \\textit{A'B'}", ", ",
            "\r \\textit{AC}", "\r $ \\equiv $", "\r \\textit{A'C'}", ",",
            "\r $ \\angle $", "\\textit{A}", "\r $ \\equiv $", "\r $\\angle $", "\\textit{A'}",
            "\r eşlikleri geçerli ise",  # EŞLİK?
        )
        belit_IV_6_d_3 = TextMobject(
            "$ \\angle $", "\\textit{B}", "\r $ \\equiv $", "\r $\\angle $", "\\textit{B'}", "\r ve",
            "\r $ \\angle $", "\\textit{C}", "\r $ \\equiv $", "\r $\\angle $", "\\textit{C'}",
            "\r eşlikleri de geçerlidir"  # EŞLİK?
        )
        teorem_d_0 = TextMobject("Teorem:")
        teorem_d_3 = TextMobject(
            "$\\triangle $\\textit{ABC}    $ \\equiv $   $\\triangle $\\textit{A'B'C'} eşliği de geçerlidir"
        )
        BC_eşittir_B_üssü_C_üssü = TextMobject(
            "\\textit{BC}", "\r $ \\equiv $ ", "\r \\textit{B'C'}"
        )
        açı_BAD_üssü_eşittir_açı_A = TextMobject(
            "$ \\angle $", "\\textit{B'A'D'}", "\r $ \\equiv $", "\r $\\angle $", "\\textit{A}"
        )
        açı_A_eşittir_açı_BAC_üssü = TextMobject(
            "$ \\angle $", "\\textit{A}", "\r $ \\equiv $", "\r $\\angle $", "\\textit{B'A'C'}"
        )

        kenar_a = TextMobject("\\textit{a}").set_color(self.renk_AB)
        kenar_b = TextMobject("\\textit{b}").set_color(self.renk_AC)
        kenar_c = TextMobject("\\textit{c}").set_color(self.renk_BC)
        acı_alpha = TexMobject("\\alpha").set_color(self.renk_acı_A).scale(0.9)

        cos_teoremi = TexMobject("\\textit{c}",
                                 "\r =",
                                 "\r \\textit{a}", "^{2}", "\r + ", "\r \\textit{b}", "^{2}",
                                 "\r +",
                                 "\r 2", "\\textit{a}", "\\textit{b}", "\\cos", "\\alpha"
                                 )
        cos_teoremi[0].set_color(self.renk_BC)
        cos_teoremi[2].set_color(self.renk_AB)
        cos_teoremi[5].set_color(self.renk_AC)
        cos_teoremi[9].set_color(self.renk_AB)
        cos_teoremi[10].set_color(self.renk_AC)
        cos_teoremi[12].set_color(self.renk_acı_A)

        h_k_açısı[1].set_color(YELLOW)
        h_k_açısı[3].set_color(ORANGE)
        k_h_açısı[3].set_color(YELLOW)
        k_h_açısı[1].set_color(ORANGE)
        h_k_eşittir_h_üssü_k_üssü[1].set_color(YELLOW)
        h_k_eşittir_h_üssü_k_üssü[3].set_color(ORANGE)
        h_k_eşittir_h_üssü_k_üssü[7].set_color(YELLOW)
        h_k_eşittir_h_üssü_k_üssü[9].set_color(ORANGE)
        h_k_eşittir_h_k[1].set_color(YELLOW)
        h_k_eşittir_h_k[3].set_color(ORANGE)
        h_k_eşittir_h_k[7].set_color(YELLOW)
        h_k_eşittir_h_k[9].set_color(ORANGE)
        h_k_eşittir_h_k_çift_üssü[1].set_color(YELLOW)
        h_k_eşittir_h_k_çift_üssü[3].set_color(ORANGE)
        h_k_eşittir_h_k_çift_üssü[7].set_color(YELLOW)
        h_k_eşittir_h_k_çift_üssü[9].set_color(ORANGE)

        tanım_ışın.scale(0.75)
        tanım_ışın_d.scale(0.75)
        tanım_ışın.move_to(UP*1.5)
        tanım_ışın_d.next_to(tanım_ışın.get_left() + DOWN*.5, buff=0)
        tanım_açı.scale(0.75)
        tanım_açı_d.scale(0.75)
        tanım_açı.move_to(UP * 2.25)
        tanım_açı_d.next_to(tanım_açı.get_left() + DOWN * .7, buff=0)
        belit_IV_4_d_0.scale(0.75)
        belit_IV_4_d_1.scale(0.75)
        belit_IV_4_d_0.move_to(LEFT * 5.2 + UP * 2.9)
        belit_IV_4_d_1.next_to(belit_IV_4_d_0.get_left() + DOWN * 1.2, buff=0)
        h_k_eşittir_h_üssü_k_üssü.move_to(UP*2.1 + RIGHT*0.15)
        h_k_eşittir_h_k.move_to(UP*1.7)
        belit_IV_5_d_0.scale(0.9)
        belit_IV_5_d_0.move_to(LEFT * 5.2 + UP * 2.1)
        belit_IV_6_d_0.scale(0.75)
        belit_IV_6_d_1.scale(0.75)
        belit_IV_6_d_2.scale(0.75)
        belit_IV_6_d_3.scale(0.75)
        belit_IV_6_d_0.move_to(LEFT * 5.2 + UP * 2.8)
        belit_IV_6_d_1.next_to(belit_IV_6_d_0.get_left() + DOWN * 0.5, buff=0)
        belit_IV_6_d_2.next_to(belit_IV_6_d_1.get_left() + DOWN * 0.5, buff=0)
        belit_IV_6_d_3.next_to(belit_IV_6_d_2.get_left() + DOWN * 0.5, buff=0)
        for i in [1, 21, 26, 31]:
            belit_IV_4_d_1[i].set_color([YELLOW_C, YELLOW_A])

        for j in [3, 28, 33, 36]:
            belit_IV_4_d_1[j].set_color([ORANGE_C, ORANGE_A])

        for k in [5, 9, 12, 24]:
            belit_IV_4_d_1[k].set_color([BLUE_D, BLUE_B])
        belit_IV_6_d_2[0].set_color(self.renk_AB)
        belit_IV_6_d_2[2].set_color(self.renk_AB)
        belit_IV_6_d_2[4].set_color(self.renk_AC)
        belit_IV_6_d_2[6].set_color(self.renk_AC)
        belit_IV_6_d_2[9].set_color(self.renk_acı_A)
        belit_IV_6_d_2[12].set_color(self.renk_acı_A)
        belit_IV_6_d_3[1].set_color(self.renk_acı_B)
        belit_IV_6_d_3[4].set_color(self.renk_acı_B)
        belit_IV_6_d_3[7].set_color(self.renk_acı_C)
        belit_IV_6_d_3[10].set_color(self.renk_acı_C)
        teorem_d_0.scale(0.75)
        teorem_d_1 = belit_IV_6_d_1.copy()
        teorem_d_2 = belit_IV_6_d_2.copy()
        teorem_d_3.scale(0.75)
        teorem_d_0.move_to(LEFT * 5.2 + UP * 2.8)
        teorem_d_1.next_to(teorem_d_0.get_left() + DOWN * 0.5, buff=0)
        teorem_d_2.next_to(teorem_d_1.get_left() + DOWN * 0.5, buff=0)
        teorem_d_3.next_to(teorem_d_2.get_left() + DOWN * 0.5, buff=0)
        BC_eşittir_B_üssü_C_üssü[0].set_color(self.renk_BC)
        BC_eşittir_B_üssü_C_üssü[2].set_color(self.renk_BC)
        açı_BAD_üssü_eşittir_açı_A[1].set_color(self.renk_acı_A)
        açı_BAD_üssü_eşittir_açı_A[4].set_color(self.renk_acı_A)
        açı_A_eşittir_açı_BAC_üssü[1].set_color(self.renk_acı_A)
        açı_A_eşittir_açı_BAC_üssü[4].set_color(self.renk_acı_A)


        teorem = VGroup(teorem_d_0, teorem_d_1, teorem_d_2, teorem_d_3)
        belit_IV_4 = VGroup(belit_IV_4_d_0, belit_IV_4_d_1)
        belit_IV_5 = VGroup(belit_IV_5_d_0)
        belit_IV_6 = VGroup(belit_IV_6_d_0, belit_IV_6_d_1, belit_IV_6_d_2, belit_IV_6_d_3)

        BC_eşittir_B_üssü_C_üssü.move_to(UP * 2.1)
        açı_A_eşittir_açı_BAC_üssü.move_to(UP * 1.8 + RIGHT * 2)
        açı_BAD_üssü_eşittir_açı_A.move_to(UP * 1.8 + LEFT * 2)

        ekran = EkraniOrt()
        line = Line(LEFT * 7.5, RIGHT * 7.5).move_to(DOWN*.3)
        dot_p = Dot(line.point_from_proportion(0.4), color=YELLOW)
        P = TextMobject("\\textit{P}")
        P_üssü = TextMobject("\\textit{P'}")
        PA_ışını = TextMobject("\\textit{h}")
        PA_ışını.next_to(line.point_from_proportion(0.55) + UP * 0.4)
        alpha = TextMobject("$ \\alpha $").move_to(LEFT * 6.3 + UP * 0.7).set_color([BLUE_D, BLUE_B])
        alpha_üssü = TextMobject("$ \\alpha $'").set_color([BLUE_D, BLUE_B])
        line_1 = Line(LEFT * 6 + DOWN * .5, LEFT + DOWN * 3)
        line_1_1 = line_1.copy().shift(RIGHT * 7)
        line_2 = Line(LEFT * 6 + DOWN * 1.7, LEFT + DOWN * .1)
        line_2_1 = line_2.copy().shift(RIGHT * 7)
        dot_p_1 = Dot(line_1.point_from_proportion(0.293))
        dot_p_üssü_1 = dot_p_1.copy().shift(RIGHT * 7)
        l1 = DashedLine(LEFT * 6 + UP * .85, LEFT + UP * .85)
        l2 = DashedLine(l1.get_end(), l1.get_end() + DOWN * 4.5)
        l3 = DashedLine(l2.get_end(), l1.get_start() + DOWN * 4.5)
        l4 = DashedLine(l3.get_end(), l1.get_start())
        l1_1 = DashedLine(LEFT * 6 + UP * .5, LEFT + UP * .5)
        l2_1 = DashedLine(l1_1.get_end(), l1_1.get_end() + DOWN * 4)
        l3_1 = DashedLine(l2_1.get_end(), l1_1.get_start() + DOWN * 4)
        l4_1 = DashedLine(l3_1.get_end(), l1_1.get_start())
        l_üst_sol = DashedLine(LEFT * 6 + UP * 0.5, LEFT * 0.03 + UP * 0.5).set_color(BLUE_D)
        l_üst_sağ = DashedLine(RIGHT * 0.03 + UP * 0.5, RIGHT * 6 + UP * 0.5).set_color(BLUE_D)
        l_alt_sol = DashedLine(LEFT * 0.03 + DOWN * 3.5, LEFT * 6 + DOWN * 3.5).set_color(BLUE_D)
        l_alt_sağ = DashedLine(RIGHT * 6 + DOWN * 3.5, RIGHT * 0.03 + DOWN * 3.5).set_color(BLUE_D)
        duzlem = VGroup(l1, l2, l3, l4).set_color(BLUE_D)
        duzlem_1 = VGroup(l1_1, l2_1, l3_1, l4_1).set_color(BLUE_D)
        duzlem_2 = duzlem_1.copy().shift(RIGHT * 7)
        h_ışını = Line(dot_p_1.get_center(), line_2.get_end()).set_color(YELLOW)
        h_üssü_ışını = Line(dot_p_üssü_1.get_center(), line_2_1.get_end()).set_color(YELLOW)
        h_üssü_ışını_uzantı = DashedLine(dot_p_üssü_1.get_center(), LEFT * 4.625 + DOWN * 3.5).set_color(YELLOW)
        h_üssü_ışını_alt_taraf = Polygon(
            h_üssü_ışını_uzantı.get_end() + RIGHT * 0.3 + UP * 0.05,
            duzlem_2[2].get_start() + LEFT * 0.05 + UP * 0.05,
            h_üssü_ışını.get_end() + LEFT * 0.05 + DOWN * 0.06,
            color=BLUE_D,
            fill_opacity=0.5
        )
        anti_h_ışını = Line(dot_p_1.get_center(), line_2.get_start()).set_color(DARKER_GREY)
        k_ışını = Line(dot_p_1.get_center(), line_1.get_end()).set_color(ORANGE)
        k_üssü_ışını = Line(dot_p_üssü_1.get_center(), line_1_1.get_end()).set_color(ORANGE)
        anti_k_ışını = Line(dot_p_1.get_center(), line_1.get_start()).set_color(DARKER_GREY)
        h = TextMobject("\\textit{h}").set_color(YELLOW_C)
        h_üssü = TextMobject("\\textit{h'}").set_color(YELLOW_C)
        k = TextMobject("\\textit{k}").set_color(ORANGE_C)
        k_üssü = TextMobject("\\textit{k'}").set_color(ORANGE_C)
        a_üssü = TextMobject("\\textit{a'}")

        for i in [0, 5]:
            tanım_açı[i].set_color([BLUE_D, BLUE_B])
        tanım_açı[2].set_color([YELLOW_C, YELLOW_A])
        tanım_açı[3].set_color([ORANGE_C, ORANGE_A])
        tanım_açı_d[1].set_color([YELLOW_C, YELLOW_A])
        tanım_açı_d[2].set_color([ORANGE_C, ORANGE_A])

        h_k_açısı.next_to(dot_p_1, RIGHT, 6).shift(UP * .5)
        k_h_açısı.next_to(dot_p_1, RIGHT, 6).shift(DOWN * .5)
        P.next_to(dot_p, DOWN, 0.1)
        P_üssü.next_to(dot_p_üssü_1, DOWN, 0.1)
        h.next_to(h_ışını.point_from_proportion(0.3), UP, 0.2)
        h_üssü.next_to(h_üssü_ışını.point_from_proportion(0.3), UP, 0.2)
        k.next_to(k_ışını.point_from_proportion(0.3), DOWN, 0.2)
        k_üssü.next_to(k_üssü_ışını.point_from_proportion(0.3), DOWN, 0.2)
        a_üssü.next_to(line_2_1.point_from_proportion(0.15), UP, 0.2)

        nokta_A, nokta_B, nokta_C, nokta_A_üssü, nokta_B_üssü, nokta_C_üssü = list(
            map(Dot, [self.a, self.b, self.c, self.d, self.e, self.f]))
        A, B, C, A_üssü, B_üssü, C_üssü, D_üssü = list(map(TextMobject, ["A", "B", "C", "A'", "B'", "C'", "D'"]))

        cizgi_AB_text = TextMobject("\\textit{AB}").set_color(self.renk_AB)
        cizgi_AB_üssü_text = TextMobject("\\textit{A'B'}").set_color(self.renk_AB)
        cizgi_AC_text = TextMobject("\\textit{AC}").set_color(self.renk_AC)
        cizgi_AC_üssü_text = TextMobject("\\textit{A'C'}").set_color(self.renk_AC)
        cizgi_BC_text = TextMobject("\\textit{BC}").set_color(self.renk_BC)
        cizgi_BC_üssü_text = TextMobject("\\textit{B'C'}").set_color(self.renk_BC)
        acı_A_text = TextMobject("$ \\angle $", "\\textit{A}").set_color(self.renk_acı_A)
        # Bunu geçici olarak koyuyorum. HATALI GÖSTERİM. Bu, sanki A ışını varmış anlamına gelir.
        acı_A_üssü_text = TextMobject("$ \\angle $\\textit{A'}").set_color(self.renk_acı_A)
        acı_B_text = TextMobject("$ \\angle $\\textit{B}").set_color(self.renk_acı_B)
        acı_B_üssü_text = TextMobject("$ \\angle $\\textit{B'}").set_color(self.renk_acı_B)
        acı_C_text = TextMobject("$ \\angle $\\textit{C}").set_color(self.renk_acı_C)
        acı_C_üssü_text = TextMobject("$ \\angle $\\textit{C'}").set_color(self.renk_acı_C)

        cizgi_AB = Line(self.a, self.b).set_color(self.renk_AB)
        cizgi_AC = Line(self.a, self.c).set_color(self.renk_AC)
        cizgi_BC = Line(self.b, self.c).set_color(self.renk_BC)
        cizgi_AB_üssü = Line(self.d, self.e).set_color(self.renk_AB)
        cizgi_AC_üssü = Line(self.d, self.f).set_color(self.renk_AC)
        cizgi_BC_üssü = Line(self.e, self.f).set_color(self.renk_BC)

        acı_A = Arc(cizgi_AB.get_angle(), cizgi_AC.get_angle() - cizgi_AB.get_angle(), radius=0.4) \
            .move_arc_center_to(self.a).set_color(self.renk_acı_A)
        acı_B = Arc(cizgi_BC.get_angle(), PI + cizgi_AB.get_angle(), radius=0.4) \
            .move_arc_center_to(self.b).set_color(self.renk_acı_B)
        acı_C = Arc(PI - cizgi_BC.get_angle(), cizgi_AC.get_angle(), radius=0.4) \
            .move_arc_center_to(self.c).set_color(self.renk_acı_C)
        acı_A_üssü = Arc(cizgi_AB_üssü.get_angle(), cizgi_AC_üssü.get_angle() - cizgi_AB_üssü.get_angle(), radius=0.4) \
            .move_arc_center_to(self.d).set_color(self.renk_acı_A)
        acı_B_üssü = Arc(cizgi_BC_üssü.get_angle(), PI + cizgi_AB_üssü.get_angle(), radius=0.4) \
            .move_arc_center_to(self.e).set_color(self.renk_acı_B)
        acı_C_üssü = Arc(PI - cizgi_BC_üssü.get_angle(), cizgi_AC_üssü.get_angle(), radius=0.4) \
            .move_arc_center_to(self.f).set_color(self.renk_acı_C)

        acılar_ABC = VGroup(acı_A, acı_B, acı_C)
        acılar_ABC_üssü = VGroup(acı_A_üssü, acı_B_üssü, acı_C_üssü)
        noktalar_ABC = VGroup(nokta_A, nokta_B, nokta_C)
        noktalar_ABC_üssü = VGroup(nokta_A_üssü, nokta_B_üssü, nokta_C_üssü)

        A.next_to(nokta_A, UP, 0.1)
        B.next_to(nokta_B, LEFT, 0.1)
        C.next_to(nokta_C, RIGHT, 0.1)
        A_üssü.next_to(nokta_A_üssü, UP * 0.1)
        A_üssü.shift(RIGHT*0.05 + UP * 0.1)
        B_üssü.next_to(nokta_B_üssü, LEFT, 0.1)
        C_üssü.next_to(nokta_C_üssü, RIGHT, 0.1)

        ucgen_ABC = VGroup(A, B, C, cizgi_AB, cizgi_AC, cizgi_BC, nokta_A, nokta_B, nokta_C)
        ucgen_ABC_üssü = VGroup(A_üssü, B_üssü, C_üssü, cizgi_AB_üssü, cizgi_AC_üssü, cizgi_BC_üssü, nokta_A_üssü,
                                nokta_B_üssü, nokta_C_üssü)

        ucgen_ABC.shift(LEFT * 0.5 + DOWN)
        ucgen_ABC_üssü.shift(RIGHT * 0.5 + DOWN)
        acılar_ABC.shift(LEFT * 0.5 + DOWN)
        acılar_ABC_üssü.shift(RIGHT * 0.5 + DOWN)

        self.play(Write(tanım_ışın, rate_func=rush_into),
                  ShowCreation(line, run_time=2))
        self.play(Write(tanım_ışın_d, rate_func=rush_from),
                  ShowCreation(dot_p),
                  Write(P))
        for i in range(66, 166):
            small_dot = SmallDot(color=YELLOW)
            small_dot.move_to(line.point_from_proportion(i / 165))
            self.play(small_dot.add, run_time=0.013)
        self.wait()

        self.play(Write(PA_ışını))
        self.wait()
        self.add(ekran, self.moyc)

        self.play(Write(tanım_açı, rate_func=rush_into),
                  ShowCreation(duzlem),
                  Write(alpha))
        P.next_to(dot_p_1, DOWN, 0.1)
        self.play(Write(tanım_açı_d, rate_func=rush_from),
                  *[ShowCreation(i) for i in [line_1, line_2]])
        self.remove(duzlem, P)
        self.add(duzlem)
        self.play(Write(P),
                  ShowCreation(dot_p_1))
        dot_p_1_1 = dot_p_1.copy()
        self.play(*[ShowCreation(i) for i in [h_ışını, k_ışını,
                                              anti_h_ışını, anti_k_ışını]],
                  dot_p_1_1.add,
                  Write(h),
                  Write(k))
        self.remove(duzlem, line_1, line_2, dot_p_1_1, dot_p_1)
        self.add(duzlem, dot_p_1)
        self.wait()

        self.play(TransformFromCopy(h, h_k_açısı[1]),
                  TransformFromCopy(k, h_k_açısı[3]),
                  *[FadeInFrom(i, LEFT) for i in [h_k_açısı[0], h_k_açısı[2], h_k_açısı[4]]])

        self.play(TransformFromCopy(h, k_h_açısı[3]),
                  TransformFromCopy(k, k_h_açısı[1]),
                  *[FadeInFrom(i, LEFT) for i in [k_h_açısı[0], k_h_açısı[2], k_h_açısı[4]]])
        self.wait()

        self.remove(ekran)
        self.add(ekran, self.moyc)

        alpha.move_to(LEFT * 6.3 + UP * 0.34)
        alpha_üssü.move_to(RIGHT * 0.65 + UP * 0.34)

        self.remove(alpha, P, h, k, dot_p_1, h_ışını, k_ışını)
        self.play(Write(belit_IV_4_d_0), rate_func=rush_into)
        self.play(Write(belit_IV_4_d_1[0:11], rate_func=rush_from),
                  *[ShowCreation(i) for i in [h_ışını, k_ışını, dot_p_1, duzlem_1]],
                  *[Write(i) for i in [alpha, P, h, k]])
        self.play(TransformFromCopy(alpha, alpha_üssü),
                  TransformFromCopy(h_ışını, line_2_1),
                  FadeInFrom(a_üssü, LEFT),
                  TransformFromCopy(duzlem_1, duzlem_2))
        self.wait()

        self.play(Write(belit_IV_4_d_1[11:16]))
        self.remove(duzlem_2)
        self.play(ShowCreation(h_üssü_ışını, run_time=1.5),
                  ShowCreation(dot_p_üssü_1),
                  duzlem_2.add)
        self.wait()

        self.play(*[Write(i) for i in [P_üssü, h_üssü, belit_IV_4_d_1[16:23]]])
        self.wait()

        self.play(Write(belit_IV_4_d_1[23:-2]))
        self.remove(duzlem_2)
        self.remove(dot_p_üssü_1)
        self.play(ShowCreation(k_üssü_ışını),
                  Write(k_üssü),
                  duzlem_2.add,
                  dot_p_üssü_1.add)
        self.wait()

        self.play(Write(belit_IV_4_d_1[-2:]))
        self.wait()

        self.play(*[FadeOut(i) for i in [line_2_1, a_üssü]],
                  *[FadeOutAndShift(k, UP) for k in [belit_IV_4_d_0, belit_IV_4_d_1]],
                  TransformFromCopy(h, h_k_eşittir_h_üssü_k_üssü[1]),
                  TransformFromCopy(k, h_k_eşittir_h_üssü_k_üssü[3]),
                  TransformFromCopy(h_üssü, h_k_eşittir_h_üssü_k_üssü[7]),
                  TransformFromCopy(k_üssü, h_k_eşittir_h_üssü_k_üssü[9]),
                  *[FadeInFrom(i, DOWN) for i in [h_k_eşittir_h_üssü_k_üssü[0],
                                                  h_k_eşittir_h_üssü_k_üssü[2],
                                                  h_k_eşittir_h_üssü_k_üssü[4],
                                                  h_k_eşittir_h_üssü_k_üssü[5],
                                                  h_k_eşittir_h_üssü_k_üssü[6],
                                                  h_k_eşittir_h_üssü_k_üssü[8],
                                                  h_k_eşittir_h_üssü_k_üssü[10]]]
                  )
        self.wait()
        self.play(h_k_eşittir_h_üssü_k_üssü.shift, UP * 0.3,
                  FadeInFrom(h_k_eşittir_h_k, DOWN))
        self.wait()

        self.play(FadeOutAndShift(duzlem_1[1], RIGHT),
                  FadeOutAndShift(duzlem_2[3], LEFT),
                  FadeOutAndShift(alpha_üssü, LEFT),
                  *[FadeOut(i) for i in [k_üssü, k_üssü_ışını]],
                  Transform(duzlem_1[0], l_üst_sol),
                  Transform(duzlem_2[0], l_üst_sağ),
                  Transform(duzlem_1[2], l_alt_sol),
                  Transform(duzlem_2[2], l_alt_sağ)
                  )

        self.remove(l_alt_sol, dot_p_üssü_1)
        self.play(ShowCreation(h_üssü_ışını_uzantı),
                  l_alt_sol.add,
                  dot_p_üssü_1.add)
        self.play(VFadeInThenOut(h_üssü_ışını_alt_taraf),
                  FadeOut(h_üssü_ışını_uzantı))
        self.wait()

        k_üssü_ışını_c = k_üssü_ışını.copy()
        k_üssü_ışını_c.rotate(h_üssü_ışını.get_angle() - k_üssü_ışını.get_angle(),
                              about_point=dot_p_üssü_1.get_center())
        dkdrtgn = Rectangle(color=BLACK, fill_opacity=1).scale(2).rotate(PI/2).next_to(duzlem_2[1], RIGHT, 0.04)
        dkkdrtgn = Rectangle(color=BLACK, fill_opacity=1).next_to(duzlem_2[2].get_start(), DOWN, 0.04)

        self.remove(dot_p_üssü_1)
        self.play(Rotate(k_üssü_ışını_c, -h_üssü_ışını.get_angle() + k_üssü_ışını.get_angle(),
                         about_point=dot_p_üssü_1.get_center()),
                  dot_p_üssü_1.add,
                  dkdrtgn.add,
                  )
        self.wait()
        k_üssü_ışını_cc = k_üssü_ışını_c.copy()
        self.remove(dot_p_üssü_1)
        self.play(Rotate(k_üssü_ışını_cc, -10 * DEGREES, about_point=dot_p_üssü_1.get_center()),
                  dot_p_üssü_1.add,
                  dkkdrtgn.add)
        self.wait()

        self.remove(ekran, h_k_eşittir_h_k_çift_üssü, h_k_eşittir_h_üssü_k_üssü, dkkdrtgn)
        self.add(ekran, self.moyc)

        h_k_eşittir_h_üssü_k_üssü.move_to(RIGHT * 2.5)
        h_k_eşittir_h_k_çift_üssü.move_to(LEFT * 2.5)

        self.play(Write(belit_IV_5_d_0))
        self.play(Write(h_k_eşittir_h_üssü_k_üssü))
        self.wait()
        self.play(Write(h_k_eşittir_h_k_çift_üssü))
        self.wait()
        h_k_açısı.move_to(ORIGIN)
        x = [6, 7, 8, 9, 10]
        y = [0, 1, 2, 3, 4]
        self.play(
            *[ReplacementTransform(h_k_eşittir_h_k_çift_üssü[x_i], h_k_açısı[y_i]) for x_i, y_i in zip(x, y)],
            *[ReplacementTransform(h_k_eşittir_h_üssü_k_üssü[y_i], h_k_açısı[y_i]) for x_i, y_i in zip(x, y)],
            h_k_eşittir_h_k_çift_üssü[5].shift, RIGHT * 0.5,
            h_k_eşittir_h_üssü_k_üssü[5].shift, LEFT * 0.55
        )
        self.remove(h_k_açısı)
        self.wait()

        self.remove(ekran)
        self.add(ekran, self.moyc)

        ucgen_ABC.set_color(WHITE)
        ucgen_ABC_üssü.set_color(WHITE)

        self.play(Write(belit_IV_6_d_0))
        self.play(
            Write(belit_IV_6_d_1),
            *[Write(ucgen_ABC[i]) for i in range(0, 3)],
            *[Write(ucgen_ABC_üssü[i]) for i in range(0, 3)],
            *[ShowCreation(ucgen_ABC[i]) for i in range(3, 9)],
            *[ShowCreation(ucgen_ABC_üssü[i]) for i in range(3, 9)]
        )
        self.wait()

        self.remove(noktalar_ABC, noktalar_ABC_üssü, cizgi_AB, cizgi_AB_üssü, cizgi_AC, cizgi_AC_üssü)
        self.play(
            Write(belit_IV_6_d_2),
            *[ShowCreation(i) for i in [acı_A, acı_A_üssü]],
            cizgi_AB.set_color, self.renk_AB,
            cizgi_AB_üssü.set_color, self.renk_AB,
            cizgi_AC.set_color, self.renk_AC,
            cizgi_AC_üssü.set_color, self.renk_AC,
            noktalar_ABC.add,
            noktalar_ABC_üssü.add
        )

        self.wait()

        self.remove(ucgen_ABC, ucgen_ABC_üssü)
        self.play(
            Write(belit_IV_6_d_3),
            *[ShowCreation(acılar_ABC[i]) for i in [1, 2]],
            *[ShowCreation(acılar_ABC_üssü[i]) for i in [1, 2]],
            ucgen_ABC.add,
            ucgen_ABC_üssü.add
        )
        self.wait()

        self.remove(ekran, ucgen_ABC, ucgen_ABC_üssü)
        self.add(ekran, self.moyc)

        ucgen_ABC.set_color(WHITE)
        ucgen_ABC_üssü.set_color(WHITE)

        self.play(Write(teorem_d_0))
        self.play(
            Write(teorem_d_1),
            *[Write(ucgen_ABC[i]) for i in range(0, 3)],
            *[Write(ucgen_ABC_üssü[i]) for i in range(0, 3)],
            *[ShowCreation(ucgen_ABC[i]) for i in range(3, 9)],
            *[ShowCreation(ucgen_ABC_üssü[i]) for i in range(3, 9)]
        )
        self.wait()

        self.remove(*[ucgen_ABC[i] for i in range(3, 5)],
                    *[ucgen_ABC_üssü[i] for i in range(3, 5)],
                    *[acılar_ABC[i] for i in range(0, 3)],
                    *[acılar_ABC_üssü[i] for i in range(0, 3)],
                    noktalar_ABC, noktalar_ABC_üssü)
        self.play(
            Write(teorem_d_2),
            *[ShowCreation(i) for i in [acı_A, acı_A_üssü]],
            cizgi_AB.set_color, self.renk_AB,
            cizgi_AB_üssü.set_color, self.renk_AB,
            cizgi_AC.set_color, self.renk_AC,
            cizgi_AC_üssü.set_color, self.renk_AC,
            noktalar_ABC.add,
            noktalar_ABC_üssü.add,
        )

        self.wait()

        self.play(Write(teorem_d_3))
        self.wait()

        self.remove(ucgen_ABC, ucgen_ABC_üssü)
        self.play(
            FadeOutAndShift(teorem, UP),
            FadeInFrom(belit_IV_6, DOWN),
            *[ShowCreation(acılar_ABC[i]) for i in [1, 2]],
            *[ShowCreation(acılar_ABC_üssü[i]) for i in [1, 2]],
            ucgen_ABC.add,
            ucgen_ABC_üssü.add
        )
        self.wait()

        self.play(FadeOutAndShift(belit_IV_6, UP),
                  FadeInFrom(BC_eşittir_B_üssü_C_üssü),
                  cizgi_BC.set_color, self.renk_BC,
                  cizgi_BC_üssü.set_color, self.renk_BC)
        self.wait()

        değil = ÇizikAtmak(BC_eşittir_B_üssü_C_üssü[1]).scale(1.15)

        nokta_D_üssü = Dot(cizgi_BC_üssü.point_from_proportion(0.7))

        D_üssü.next_to(nokta_D_üssü, DOWN, 0.1)

        cizgi_B_üssü_D_üssü = Line(nokta_B_üssü.get_center(), nokta_D_üssü.get_center()).set_color(self.renk_BC)
        cizgi_D_üssü_C_üssü = Line(nokta_D_üssü.get_center(), nokta_C_üssü.get_center())
        cizgi_A_üssü_D_üssü = Line(nokta_A_üssü.get_center(), nokta_D_üssü.get_center())

        ucgen_ABD_üssü = VGroup(A_üssü, B_üssü, D_üssü, cizgi_AB_üssü, cizgi_A_üssü_D_üssü, cizgi_B_üssü_D_üssü,
                                nokta_A_üssü, nokta_B_üssü, nokta_D_üssü)
        noktalar_ABD_üssü = VGroup(nokta_D_üssü, nokta_B_üssü, nokta_A_üssü)

        acı_A_üssü_çakma = Arc(cizgi_AB_üssü.get_angle(), cizgi_A_üssü_D_üssü.get_angle() - cizgi_AB_üssü.get_angle(),
                               radius=0.48).move_arc_center_to(nokta_A_üssü.get_center()).set_color(self.renk_acı_A)
        acı_D_üssü_çakma = Arc(PI - cizgi_BC_üssü.get_angle(), cizgi_A_üssü_D_üssü.get_angle(),
                               radius=0.4).move_arc_center_to(nokta_D_üssü.get_center()).set_color(self.renk_acı_C)

        self.play(ShowCreation(değil))
        self.wait()

        self.remove(nokta_B_üssü, nokta_C_üssü, cizgi_BC_üssü)
        self.play(
            Write(D_üssü),
            cizgi_D_üssü_C_üssü.add,
            ReplacementTransform(cizgi_BC_üssü, cizgi_B_üssü_D_üssü),
            TransformFromCopy(nokta_C_üssü, nokta_D_üssü),
            FadeOutAndShift(BC_eşittir_B_üssü_C_üssü, UP),
            FadeOutAndShift(değil, UP),
            nokta_B_üssü.add,
            nokta_C_üssü.add
        )
        self.remove(cizgi_BC_üssü, nokta_C_üssü, nokta_D_üssü, nokta_B_üssü)
        self.add(cizgi_B_üssü_D_üssü,
                 nokta_C_üssü, nokta_D_üssü, nokta_B_üssü)
        self.wait()

        self.remove(nokta_A_üssü, nokta_D_üssü)
        self.play(ShowCreation(cizgi_A_üssü_D_üssü),
                  nokta_A_üssü.add,
                  nokta_D_üssü.add)
        self.remove(noktalar_ABD_üssü)
        self.play(
            cizgi_BC_üssü.remove,
            Belirt(ucgen_ABC),
            Belirt(ucgen_ABD_üssü),
        )
        self.wait()

        self.remove(ucgen_ABD_üssü)
        self.play(*[ShowCreation(i) for i in [acı_A_üssü_çakma, acı_D_üssü_çakma]],
                  ucgen_ABD_üssü.add)
        self.wait()

        self.play(FadeInFrom(açı_BAD_üssü_eşittir_açı_A, DOWN))
        self.wait()

        self.play(FadeInFrom(açı_A_eşittir_açı_BAC_üssü, DOWN))
        self.wait()

        belit_IV_5.shift(UP * 0.5)
        acı_A_text.move_to(UP * 1.8)
        x = [3, 4]
        y = [0, 1]
        self.play(
            FadeInFrom(belit_IV_5, DOWN),
            *[ReplacementTransform(açı_BAD_üssü_eşittir_açı_A[x_i], acı_A_text[y_i]) for x_i, y_i in zip(x, y)],
            *[ReplacementTransform(açı_A_eşittir_açı_BAC_üssü[y_i], acı_A_text[y_i]) for x_i, y_i in zip(x, y)],
            açı_BAD_üssü_eşittir_açı_A[2].shift, RIGHT * 0.3,
            açı_A_eşittir_açı_BAC_üssü[2].shift, LEFT * 0.3
        )
        self.remove(acı_A_text)
        self.wait()

        self.play(
            FadeInFrom(belit_IV_4, DOWN),
            *[FadeOutAndShift(i, UP) for i in [belit_IV_5_d_0, acı_A_text, açı_A_eşittir_açı_BAC_üssü,
                                               açı_BAD_üssü_eşittir_açı_A]]
        )
        self.wait()

        self.play(FadeOutAndShift(belit_IV_4, UP))
        self.wait()

        def hareketli_nokta_D_üssü(obj):
            obj_acı_A_çakma, obj_acı_D_çakma, obj_cizgi_B_üssü_D_üssü, obj_nokta_D_üssü = obj
            obj_acı_A_çakma.become(
                Arc(
                    start_angle=cizgi_AB_üssü.get_angle(),
                    angle=cizgi_A_üssü_D_üssü.get_angle() - cizgi_AB_üssü.get_angle(),
                    radius=0.48,
                    color=self.renk_acı_A
                ).move_arc_center_to(cizgi_A_üssü_D_üssü.get_start())
            )
            obj_acı_D_çakma.become(
                Arc(
                    start_angle=PI - cizgi_BC_üssü.get_angle(),
                    angle=cizgi_A_üssü_D_üssü.get_angle(),
                    radius=0.4,
                    color=self.renk_acı_C
                ).move_arc_center_to(cizgi_A_üssü_D_üssü.get_end())
            )
            obj_cizgi_B_üssü_D_üssü.become(
                Line(
                    cizgi_BC_üssü.get_start(),
                    cizgi_A_üssü_D_üssü.get_end(),
                ).set_color(self.renk_BC)
            )
            obj_nokta_D_üssü.next_to(cizgi_A_üssü_D_üssü.get_end(), ORIGIN)

        hareketli_nokta_D_üssü_grubu = VGroup(acı_A_üssü_çakma, acı_D_üssü_çakma, cizgi_B_üssü_D_üssü, nokta_D_üssü)
        hareketli_nokta_D_üssü_grubu.add_updater(hareketli_nokta_D_üssü)
        self.add(hareketli_nokta_D_üssü_grubu)

        self.remove(cizgi_AB_üssü, cizgi_A_üssü_D_üssü, noktalar_ABC_üssü)
        self.play(FadeOutAndShift(D_üssü, RIGHT),
                  ReplacementTransform(cizgi_A_üssü_D_üssü, cizgi_AC_üssü),
                  cizgi_AB_üssü.add,
                  noktalar_ABC_üssü.add,
                  )
        self.add(noktalar_ABC_üssü)
        hareketli_nokta_D_üssü_grubu.remove_updater(hareketli_nokta_D_üssü)
        self.remove(cizgi_D_üssü_C_üssü)
        self.wait(0.5)
        self.play(*[FadeIn(i) for i in [BC_eşittir_B_üssü_C_üssü, değil]])
        self.wait(0.5)
        değil.rotate(PI)
        self.play(Uncreate(değil))
        self.wait()

        ekran_c = EkraniOrt()
        self.remove(ucgen_ABC)
        self.play(FadeIn(ekran_c),
                  ucgen_ABC.add
                  )
        self.play(ucgen_ABC.move_to, ORIGIN)
        self.wait()
        kenar_a.add_updater(lambda l: l.next_to(cizgi_AB.point_from_proportion(0.5), UL, 0.15))
        kenar_b.add_updater(lambda l: l.next_to(cizgi_AC.point_from_proportion(0.5), UR, 0.15))
        kenar_c.add_updater(lambda l: l.next_to(cizgi_BC.point_from_proportion(0.5), DOWN, 0.15))

        self.add(ucgen_ABC)
        self.wait(0.3)
        self.play(ucgen_ABC.move_to, UP,
                  *[FadeOut(ucgen_ABC[i], run_time=0.5) for i in [0, 1, 2]],
                  )
        self.wait()

        acı_A.add_updater(lambda l: l.move_arc_center_to(nokta_A.get_center()))
        acı_alpha.next_to(acı_A.point_from_proportion(0.5), DOWN, 0.15)

        self.play(*[Write(i) for i in [kenar_a, kenar_b]])

        self.remove(noktalar_ABC, cizgi_AC, cizgi_AB)
        self.play(Write(acı_alpha),
                  ShowCreation(acı_A),
                  cizgi_AB.add,
                  cizgi_AC.add,
                  noktalar_ABC.add
                  )
        self.wait()

        acı_alpha.add_updater(lambda l: l.next_to(acı_A.point_from_proportion(0.5), DOWN, 0.15))

        self.play(Write(kenar_c))
        self.wait()

        def hareketli_noktalar(obj):
            obj_acı_A, obj_cizgi_AB, obj_cizgi_AC, obj_cizgi_BC = obj

            acı_A.become(
                Arc(
                    start_angle=cizgi_AB.get_angle(),
                    angle=cizgi_AC.get_angle() - cizgi_AB.get_angle(),
                    radius=0.4,
                    color=self.renk_acı_A
                ).move_arc_center_to(nokta_A.get_start())
            )

            obj_cizgi_AB.become(
                Line(
                    nokta_A.get_center(),
                    nokta_B.get_center()
                ).set_color(self.renk_AB)
            )

            obj_cizgi_AC.become(
                Line(
                    nokta_A.get_center(),
                    nokta_C.get_center()
                ).set_color(self.renk_AC)
            )

            obj_cizgi_BC.become(
                Line(
                    nokta_B.get_center(),
                    nokta_C.get_center()
                ).set_color(self.renk_BC)
            )

        ucgen_ABC_ve_acı_A = VGroup(acı_A, cizgi_AB, cizgi_AC, cizgi_BC)

        ucgen_ABC_ve_acı_A.add_updater(hareketli_noktalar)
        self.add(ucgen_ABC_ve_acı_A)
        self.bring_to_front(noktalar_ABC)

        yörünge_1 = Polygon(nokta_A.get_center(), [2, 3, 0], [0, 3.5, 0], [-1, 2.7, 0]).make_smooth()
        yörünge_2 = Polygon(nokta_B.get_center(), [-2.5, 1, 0], [-3.5, 1.5, 0], [-4, 0.6, 0], [-3, -1, 0]).make_smooth()
        yörünge_3 = Polygon(nokta_C.get_center(), [2.5, -0.7, 0], [3.5, -1, 0], [4.5, 0, 0], [3, 1, 0]).make_smooth()
        self.play(MoveAlongPath(nokta_A, yörünge_1),
                  MoveAlongPath(nokta_B, yörünge_2),
                  MoveAlongPath(nokta_C, yörünge_3),
                  run_time=5)
        self.wait()

        cos_teoremi.next_to(cizgi_BC, DOWN, buff=1)

        self.play(TransformFromCopy(kenar_a, cos_teoremi[2]),
                  TransformFromCopy(kenar_a, cos_teoremi[9]),
                  TransformFromCopy(kenar_b, cos_teoremi[5]),
                  TransformFromCopy(kenar_b, cos_teoremi[10]),
                  TransformFromCopy(kenar_c, cos_teoremi[0]),
                  TransformFromCopy(acı_alpha, cos_teoremi[12]),
                  *[Write(cos_teoremi[t]) for t in [1, 3, 4, 6, 7, 8, 11]]
                  )
        self.wait()

        ekrann = EkraniOrt()
        self.play(FadeIn(ekrann))
        self.add(self.moyc)

    def ah_euclid_ah(self):

        önerme_1 = TextMobject("Önerme 1.1").scale(0.6)
        önerme_2 = TextMobject("Önerme 1.2").scale(0.6)
        önerme_3 = TextMobject("Önerme 1.3").scale(0.6)
        önerme_4 = TextMobject("Önerme 1.4").scale(0.6)
        önerme_8 = TextMobject("Önerme 1.8").scale(0.6)
        önerme_26 = TextMobject("Önerme 1.26").scale(0.6)

        A_1, B_1, C_1 = list(map(TextMobject, ["A", "B", "C"]))
        A_2, B_2, C_2, D_2, E_2, F_2, G_2, L_2 = list(map(TextMobject, ["A", "B", "C", "D", "E", "F", "G", "L"]))
        A_3, B_3, C_3, D_3, E_3, F_3 = list(map(TextMobject, ["A", "B", "C", "D", "E", "F"]))
        A_4, B_4, C_4, D_4, E_4, F_4 = list(map(TextMobject, ["A", "B", "C", "D", "E", "F"]))

        a_2 = LEFT * math.cos(self.acı_AB_2__x) * self.mesafe_AB_2 + DOWN * math.sin(
            self.acı_AB_2__x) * self.mesafe_AB_2 + RIGHT * 0.2
        b_2 = ORIGIN + RIGHT * 0.2
        c_2 = UP * self.mesafe_BC_2 + RIGHT * 0.2
        d_2 = LEFT * math.cos(self.acı_BD_2__x) * self.mesafe_AB_2 + UP * math.sin(
            self.acı_BD_2__x) * self.mesafe_AB_2 + RIGHT * 0.2
        e_2 = a_2 + RIGHT * math.cos(PI * 2 / 3 - self.acı_AB_2__x) * (self.mesafe_BC_2 + 0.5) + DOWN * math.sin(
            PI * 2 / 3 - self.acı_AB_2__x) * (self.mesafe_BC_2 + 0.5)
        f_2 = RIGHT * math.cos(self.acı_BD_2__x) * (self.mesafe_BC_2 + 0.5) + DOWN * math.sin(self.acı_BD_2__x) * (
                self.mesafe_BC_2 + 0.5) + RIGHT * 0.2
        g_2 = RIGHT * math.cos(self.acı_BD_2__x) * (self.mesafe_BC_2) + DOWN * math.sin(
            self.acı_BD_2__x) * self.mesafe_BC_2 + RIGHT * 0.2
        l_2 = a_2 + RIGHT * math.cos(PI * 2 / 3 - self.acı_AB_2__x) * (self.mesafe_BC_2) + DOWN * math.sin(
            PI * 2 / 3 - self.acı_AB_2__x) * (self.mesafe_BC_2)
        a_3 = LEFT
        b_3 = a_3 + RIGHT * self.uzunluk_AB_3
        c1_3 = LEFT * .75 + UP * 2.25
        c2_3 = c1_3 + RIGHT * self.uzunluk_C_3

        nokta_A_1, nokta_B_1, nokta_C_1 = list(map(Dot, [LEFT, RIGHT, UP * 1.732]))
        nokta_A_2, nokta_B_2, nokta_C_2, nokta_D_2, nokta_E_2, nokta_F_2, nokta_G_2, nokta_L_2 = list(
            map(Dot, [a_2, b_2, c_2, d_2, e_2, f_2, g_2, l_2]))
        cember_3 = Circle(radius=self.uzunluk_C_3).move_arc_center_to(a_3)
        nokta_A_3, nokta_B_3, nokta_C1_3, nokta_C2_3, nokta_D_3, nokta_E_3 = list(
            map(Dot, [a_3, b_3, c1_3, c2_3, cember_3.point_from_proportion(0.3), cember_3.point_from_proportion(0)]))
        nokta_A_4, nokta_B_4, nokta_C_4, nokta_D_4, nokta_E_4, nokta_F_4 = list(map(Dot, [self.a, self.b, self.c,
                                                                                          self.d, self.e, self.f]))

        cember_A_1 = Circle(radius=2).move_to(LEFT)
        cember_B_1 = Circle(radius=2).move_to(RIGHT).rotate(PI, [0, -1, 0])
        cember_GCH_2 = Circle(radius=self.mesafe_BC_2).move_arc_center_to(RIGHT * 0.2)
        cember_GLK_2 = Circle(radius=self.mesafe_AB_2 + self.mesafe_BC_2)
        cember_GLK_2.move_arc_center_to(
            LEFT * math.cos(self.acı_BD_2__x) * self.mesafe_AB_2 + UP * math.sin(
                self.acı_BD_2__x) * self.mesafe_AB_2 + + RIGHT * 0.2)

        cizgi_AB_1 = Line(nokta_A_1.get_center(), nokta_B_1.get_center())
        r_1 = cizgi_AB_1.copy()
        cizgi_BA_1 = r_1.copy().rotate(PI)
        cizgi_CA_1 = Line(nokta_C_1.get_center(), nokta_A_1.get_center())
        cizgi_CB_1 = Line(nokta_C_1.get_center(), nokta_B_1.get_center())
        cizgi_AB_2 = Line(a_2, b_2)
        cizgi_BC_2 = Line(b_2, c_2)
        r_2 = cizgi_BC_2.copy()
        rr_2 = Line(d_2, g_2)
        cizgi_AD_2 = Line(a_2, d_2)
        cizgi_BD_2 = Line(b_2, d_2)
        cizgi_BF_2 = Line(b_2, f_2)
        cizgi_AE_2 = Line(a_2, e_2)
        cizgi_AL_2 = Line(a_2, l_2)
        cizgi_LE_2 = Line(l_2, e_2)
        cizgi_C_3 = Line(c1_3, c2_3)
        cizgi_AB_3 = Line(a_3, b_3)
        cizgi_DA_3 = Line(cember_3.point_from_proportion(0.3), a_3)
        cizgi_AE_3 = Line(a_3, cember_3.point_from_proportion(0))
        cizgi_EB_3 = Line(cember_3.point_from_proportion(0), b_3)
        cember_3.rotate(PI + cizgi_DA_3.get_angle())
        r_3 = Line(a_3, cember_3.point_from_proportion(0.3))
        cizgi_AB_4 = Line(self.a, self.b)
        cizgi_AC_4 = Line(self.a, self.c)
        cizgi_BC_4 = Line(self.b, self.c)
        cizgi_DE_4 = Line(self.d, self.e)
        cizgi_DF_4 = Line(self.d, self.f)
        cizgi_EF_4 = Line(self.e, self.f)

        acı_A_4 = Arc(cizgi_AB_4.get_angle(), cizgi_AC_4.get_angle() - cizgi_AB_4.get_angle(),
                      radius=0.3).set_color(self.renk_acı_A).set_stroke(width=3)
        acı_B_4 = Arc(cizgi_BC_4.get_angle(), PI + cizgi_AB_4.get_angle(),
                      radius=0.3).set_color(self.renk_acı_B).set_stroke(width=3)
        acı_C_4 = Arc(PI - cizgi_BC_4.get_angle(), cizgi_AC_4.get_angle(),
                      radius=0.3).set_color(self.renk_acı_C).set_stroke(width=3)
        acı_D_4 = Arc(cizgi_DE_4.get_angle(), cizgi_DF_4.get_angle() - cizgi_DE_4.get_angle(),
                      radius=0.3).set_color(self.renk_acı_A).set_stroke(width=3)
        acı_E_4 = Arc(cizgi_EF_4.get_angle(), PI + cizgi_DE_4.get_angle(),
                      radius=0.3).set_color(self.renk_acı_B).set_stroke(width=3)
        acı_F_4 = Arc(PI - cizgi_EF_4.get_angle(), cizgi_DF_4.get_angle(),
                      radius=0.3).set_color(self.renk_acı_C).set_stroke(width=3)

        harfler_1 = VGroup(A_1, B_1, C_1).scale(0.5)
        harfler_2 = VGroup(A_2, B_2, C_2, D_2, E_2, F_2, G_2, L_2).scale(0.5)
        harfler_3 = VGroup(A_3, B_3, C_3, D_3, E_3, F_3).scale(0.5)
        harfler_4 = VGroup(A_4, B_4, C_4, D_4, E_4, F_4).scale(0.5)

        önerme_1_g = VGroup(
            cizgi_AB_1, cizgi_CA_1, cizgi_CB_1, r_1, cizgi_BA_1,
            cember_A_1, cember_B_1,
            nokta_A_1, nokta_B_1, nokta_C_1
        ).set_stroke(width=3).scale(0.5)
        önerme_2_g = VGroup(
            cizgi_AB_2, cizgi_AD_2, cizgi_AE_2, cizgi_BC_2, cizgi_BD_2, cizgi_BF_2, cizgi_AL_2, cizgi_LE_2, r_2, rr_2,
            cember_GCH_2, cember_GLK_2,
            nokta_A_2, nokta_B_2, nokta_C_2, nokta_D_2, nokta_E_2, nokta_F_2, nokta_G_2, nokta_L_2
        ).set_stroke(width=3).scale(0.3)
        önerme_3_g = VGroup(
            cizgi_C_3, cizgi_AB_3, cizgi_DA_3, cizgi_AE_3, cizgi_EB_3, r_3,
            cember_3,
            nokta_A_3, nokta_B_3, nokta_C1_3, nokta_C2_3, nokta_D_3, nokta_E_3
        ).set_stroke(width=3).scale(0.5)
        önerme_4_g = VGroup(
            cizgi_AB_4, cizgi_AC_4, cizgi_BC_4, cizgi_DE_4, cizgi_DF_4, cizgi_EF_4,
            nokta_A_4, nokta_B_4, nokta_C_4, nokta_D_4, nokta_E_4, nokta_F_4
        ).set_stroke(width=3).scale(0.55)
        acı_26_g = VGroup(
            acı_B_4, acı_C_4, acı_E_4, acı_F_4
        ).set_stroke(width=3)

        A_1.next_to(nokta_A_1, LEFT, 0.05)
        B_1.next_to(nokta_B_1, RIGHT, 0.05)
        C_1.next_to(nokta_C_1, UP, 0.05)
        A_2.next_to(nokta_A_2, LEFT, 0.05)
        B_2.next_to(nokta_B_2, UR, 0.02)
        C_2.next_to(nokta_C_2, UP, 0.05)
        D_2.next_to(nokta_D_2, UL, 0.02)
        E_2.next_to(nokta_E_2, LEFT, 0.05)
        F_2.next_to(nokta_F_2, RIGHT, 0.05)
        G_2.next_to(nokta_G_2, UR, 0.02)
        L_2.next_to(nokta_L_2, UL, 0.02)
        A_3.next_to(nokta_A_3, LEFT, 0.05)
        B_3.next_to(nokta_B_3, RIGHT, 0.05)
        C_3.next_to(cizgi_C_3, UP, 0.05)
        D_3.next_to(nokta_D_3, UL, 0.02)
        E_3.next_to(nokta_E_3, UR, 0.02)
        A_4.next_to(nokta_A_4, UP, 0.05)
        B_4.next_to(nokta_B_4, LEFT, 0.05)
        C_4.next_to(nokta_C_4, RIGHT, 0.05)
        D_4.next_to(nokta_D_4, UP, 0.05)
        E_4.next_to(nokta_E_4, LEFT, 0.05)
        F_4.next_to(nokta_F_4, RIGHT, 0.05)

        acı_A_4.move_arc_center_to(nokta_A_4.get_center())
        acı_B_4.move_arc_center_to(nokta_B_4.get_center())
        acı_C_4.move_arc_center_to(nokta_C_4.get_center())
        acı_D_4.move_arc_center_to(nokta_D_4.get_center())
        acı_E_4.move_arc_center_to(nokta_E_4.get_center())
        acı_F_4.move_arc_center_to(nokta_F_4.get_center())

        önerme_1_grup = VGroup(önerme_1_g, harfler_1)
        önerme_2_grup = VGroup(önerme_2_g, harfler_2)
        önerme_3_grup = VGroup(önerme_3_g, harfler_3)
        önerme_4_grup = VGroup(acı_D_4, acı_A_4, önerme_4_g, harfler_4)
        ön_8_g = önerme_4_g.copy()

        for i in [0, 3]:
            ön_8_g[i].set_color(self.renk_AB)
        for i in [1, 4]:
            ön_8_g[i].set_color(self.renk_AC)
        for i in [2, 5]:
            ön_8_g[i].set_color(self.renk_BC)

        harf_8_g = harfler_4.copy()
        önerme_8_grup = VGroup(ön_8_g, harf_8_g)
        ön_26_g = önerme_4_g.copy()
        harf_26_g = harfler_4.copy()
        önerme_26_grup = VGroup(ön_26_g, harf_26_g, acı_26_g)

        önerme_1_grup.move_to(LEFT * 3 + UP * 1.8)
        önerme_2_grup.move_to(RIGHT * 3 + UP * 1.8)
        önerme_3_grup.move_to(LEFT * 3 + DOWN * 1.5)
        önerme_4_grup.move_to(LEFT * 2.5)
        önerme_8_grup.move_to(RIGHT * 2.5)
        önerme_26_grup.move_to(RIGHT * 3 + DOWN * 1.5)

        dkdrtgn_önerme_1 = SurroundingRectangle(önerme_1_grup)
        dkdrtgn_önerme_1.scale(1.1)
        dkdrtgn_önerme_2 = dkdrtgn_önerme_1.copy().move_to(önerme_2_grup.get_center())
        dkdrtgn_önerme_3 = dkdrtgn_önerme_1.copy().move_to(önerme_3_grup.get_center())
        dkdrtgn_önerme_4 = dkdrtgn_önerme_1.copy().move_to(önerme_4_grup.get_center())
        dkdrtgn_önerme_26 = dkdrtgn_önerme_1.copy().move_to(önerme_26_grup.get_center())

        önerme_1.next_to(dkdrtgn_önerme_1, DOWN, 0.1)
        önerme_2.next_to(dkdrtgn_önerme_2, DOWN, 0.1)
        önerme_3.next_to(dkdrtgn_önerme_3, DOWN, 0.1)
        önerme_4.next_to(dkdrtgn_önerme_4, DOWN, 0.1)
        önerme_26.next_to(dkdrtgn_önerme_26, DOWN, 0.1)

        dkdrtgn_önerme_4 = dkdrtgn_önerme_1.copy().move_to(önerme_4_grup.get_center())
        dkdrtgn_önerme_8 = dkdrtgn_önerme_1.copy().move_to(önerme_8_grup.get_center())
        önerme_4.next_to(dkdrtgn_önerme_4, DOWN, 0.1)
        önerme_8.next_to(dkdrtgn_önerme_8, DOWN, 0.1)

        self.play(
            *[ShowCreation(i) for i in [acı_A_4, acı_D_4, önerme_4_g, ön_8_g, dkdrtgn_önerme_4, dkdrtgn_önerme_8]],
            *[Write(k) for k in [harfler_4, harf_8_g, önerme_4, önerme_8]]
        )
        self.wait()

        ekran = EkraniOrt()
        self.add(ekran, self.moyc)

        önerme_4_grup.move_to(RIGHT * 3 + DOWN * 1.5)

        for mob in [cizgi_AB_1, r_1, cizgi_BA_1, cizgi_CA_1, cizgi_CB_1, cizgi_BC_2, r_2, rr_2, cizgi_AL_2,
                    cizgi_C_3, cizgi_AE_3, cizgi_BC_4, cizgi_EF_4]:
            mob.set_color(self.renk_AB)

        self.bring_to_front(harfler_4)

        self.play(
            ShowCreation(cizgi_AL_2, rate_func=rush_into),
            *[ShowCreation(i) for i in [dkdrtgn_önerme_1, dkdrtgn_önerme_2, dkdrtgn_önerme_3, dkdrtgn_önerme_26,
                                        cizgi_AB_1,
                                        cizgi_BC_2, cizgi_AB_2, cizgi_AD_2, cizgi_BD_2, cizgi_BF_2,
                                        cizgi_C_3, cizgi_AB_3,
                                        cizgi_AB_4, cizgi_AC_4, cizgi_BC_4, cizgi_DE_4, cizgi_DF_4, cizgi_EF_4,
                                        nokta_A_1, nokta_B_1,
                                        nokta_A_2, nokta_B_2, nokta_C_2, nokta_D_2, nokta_E_2, nokta_F_2,
                                        nokta_A_3, nokta_B_3, nokta_C1_3, nokta_C2_3,
                                        nokta_A_4, nokta_B_4, nokta_C_4, nokta_D_4, nokta_E_4, nokta_F_4
                                        ]],

            *[Write(j) for j in [önerme_1, önerme_2, önerme_3, önerme_26,
                                 A_1, B_1, A_2, B_2, C_2, D_2, A_3, B_3, C_3, A_4, B_4, C_4, D_4, E_4, F_4
                                 ]]
        )

        nokta = nokta_A_3.copy()
        r_1.add_updater(lambda l: l.become(Line(r_1.get_start(), cember_A_1.get_end()).set_color(self.renk_AB)))
        cizgi_BA_1.add_updater(lambda l:
                               l.become(Line(cizgi_BA_1.get_start(), cember_B_1.get_end()).set_color(self.renk_AB)))
        cember_GCH_2.rotate(PI / 2)
        cember_GLK_2.rotate(-self.acı_BD_2__x)
        r_2.add_updater(lambda l: l.become(Line(r_2.get_start(), cember_GCH_2.get_end()).set_color(self.renk_AB)))
        rr_2.add_updater(lambda l: l.become(Line(rr_2.get_start(), cember_GLK_2.get_end())))
        self.add(r_1, cizgi_BA_1, r_2, rr_2)

        p = [cizgi_C_3, nokta_C1_3, nokta_C2_3]
        q = [cizgi_DA_3, nokta_D_3, nokta]

        self.remove(önerme_4_g)
        self.bring_to_front(nokta_A_1, nokta_B_1, nokta_B_2)
        self.play(
            *[FadeInFromPoint(i, nokta_C_1) for i in [nokta_C_1, C_1]],

            *[ShowCreation(i) for i in [cember_A_1, cember_B_1,
                                        cember_GCH_2, cember_GLK_2,
                                        nokta_G_2, nokta_L_2,
                                        acı_B_4, acı_C_4, acı_E_4, acı_F_4
                                        ]],
            ShowCreation(cizgi_LE_2, rate_func=rush_from),

            *[TransformFromCopy(p, q) for p, q in zip(p, q)],

            *[Write(i) for i in [E_2, F_2, D_3, G_2, L_2]],

            önerme_4_g.add,
            run_time=1.5
        )
        self.remove(r_1, cizgi_BA_1, nokta, r_2, rr_2)

        r_3.add_updater(lambda l: l.become(Line(r_3.get_start(), cember_3.get_end())))
        self.add(r_3)
        self.remove(nokta_A_1, nokta_B_1, nokta_C_1, nokta_A_3)
        self.play(
            *[ShowCreation(i) for i in [cizgi_CA_1, cizgi_CB_1,
                                        cember_3,
                                        cizgi_AE_3,
                                        nokta_E_3
                                        ]],

            *[Write(i) for i in [E_3]],

            *[i.add for i in [nokta_A_1, nokta_B_1, nokta_C_1, nokta_A_3]],
            run_time=1.5
        )
        self.remove(r_3)
        self.wait()

        ekran_c = ekran.copy()
        self.play(FadeIn(ekran_c),
                  self.moyc.add)

    def cikis(self):

        self.play(RotatingAndMove(self.moyc, LEFT * 6))
        self.play(FadeOut(self.moyc))
        self.wait()




