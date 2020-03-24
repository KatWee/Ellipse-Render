class Carpenter:

    def __init__(this,a ,b):
        this.a = a
        this.b = b
        this.x = 0
        this.y = b
        this.a2t8 = 8*a*a
        this.b2t8 = 8*b*b
        this.h = 4*b*b + a*a*(1-4*b)
        this.d1 = 12*b*b
        this.d2 = -this.a2t8*(b-1)
        this.sn = b*b
        this.sd = a*a*b - a*a/2
        this.xResult = []
        this.yResult = []
        this.xNegResult = []
        this.yNegResult = []

    def midpoint(this):
        # slope < 1
        while(this.sn < this.sd):
            if(this.h > 0):
                this.y -= 1
                this.h += this.d2
                this.sd -= this.a*this.a
                this.d2 += this.a2t8
            this.x += 1
            this.h += this.d1
            this.sn += this.b*this.b
            this.d1 += this.b2t8
            this.plot()

        # slope >1
        this.h -= this.b*this.b*(4*this.x*this.x + 4*this.x + 1) + \
                  4*this.a*this.a*(this.y - 1)*(this.y - 1) - \
                  4*this.a*this.a*this.b*this.b
        this.d1 = this.b2t8*(this.x + 1)
        this.d2 = -4*this.a*this.a*(2*this.y - 3)
        while(this.y > 1):
            if(this.h < 0):
                this.x += 1
                this.h += this.d1
                this.d1 += this.b2t8
            this.y -= 1
            this.h += this.d2
            this.d2 += this.a2t8
            this.plot()

    def plot(this):
        this.xResult.append(this.x)
        this.yResult.append(this.y)

    def negResult(this):
        this.xNegResult = [-x for x in this.xResult]
        this.yNegResult = [-y for y in this.yResult]

