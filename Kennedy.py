class Kennedy:

    def __init__(this,a ,b):
        this.a = a
        this.b = b
        this.x = a
        this.y = 0
        this.xChange = b*b*(1-2*a)
        this.yChange = a*a
        this.error = 0
        this.xStop = 2*b*b*a
        this.yStop = 0
        this.xResult = []
        this.yResult = []
        this.xNegResult = []
        this.yNegResult = []

    def midpoint(this):
        # octant 1
        while this.xStop >= this.yStop:
            this.plot()
            this.y += 1
            this.yStop += 2*this.a*this.a
            this.error += this.yChange
            this.yChange += 2*this.a*this.a
            if (2*this.error + this.xChange) > 0:
                this.x -= 1
                this.xStop -= 2*this.b*this.b
                this.error += this.xChange
                this.xChange += 2*this.b*this.b

        # octant 2
        this.x = 0
        this.y = this.b
        this.xChange = this.b*this.b
        this.yChange = this.a*this.a*(1 - 2*this.b)
        this.error = 0
        this.xStop = 0
        this.yStop = 2*this.a*this.a*this.b

        while this.xStop <= this.yStop:
            this.plot()
            this.x += 1
            this.xStop += 2 * this.b * this.b
            this.error += this.xChange
            this.xChange += 2 * this.b * this.b
            if (2 * this.error + this.yChange) > 0:
                this.y -= 1
                this.yStop -= 2 * this.a * this.a
                this.error += this.yChange
                this.yChange += 2 * this.a * this.a

    def plot(this):
        this.xResult.append(this.x)
        this.yResult.append(this.y)

    def negResult(this):
        this.xNegResult = [-x for x in this.xResult]
        this.yNegResult = [-y for y in this.yResult]

