import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices = [ 
                [0, 0, 0 ], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0], 
                [0, self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                [0, self.parameters['thickness'],0],
                [self.parameters['width'], self.parameters['thickness'],0]
                ]
        self.faces = [
                [0,1,4,6],
                [1,4,5,2],
                [5,2,3,7],
                [7,6,0,3]
                ]   
              
    def draw(self):        
        
        gl.glPushMatrix()  
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
        gl.glColor3fv(self.parameters['color']) 
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'],0])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
        gl.glColor3fv(self.parameters['color']) 
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glEnd()
 
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
        gl.glColor3fv(self.parameters['color'])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv( [self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv( [self.parameters['width'], self.parameters['thickness'],0])
        gl.glEnd()
         
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
        gl.glColor3fv(self.parameters['color'])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'],0])
        gl.glVertex3fv( [0, self.parameters['thickness'],0])
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glEnd()
        gl.glPopMatrix()
       
