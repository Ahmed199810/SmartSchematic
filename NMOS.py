from schemdraw.segments import *
import schemdraw.elements as elm

class NMOS(elm.Element):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.segments.append(Segment([[0, 0], [1, 0]]))
        self.segments.append(Segment([[1, 0.7], [1, -0.7]]))
        self.segments.append(Segment([[1.2, 1], [1.2, -1]]))
        self.segments.append(SegmentArrow([1.2, 0.7], [2, 0.7]))
        self.segments.append(Segment([[1.2, -0.7], [2, -0.7]]))


        self.anchors['S'] = [2, 0.7]
        self.anchors['G'] = [0, 0]
        self.anchors['D'] = [2, -0.7]



