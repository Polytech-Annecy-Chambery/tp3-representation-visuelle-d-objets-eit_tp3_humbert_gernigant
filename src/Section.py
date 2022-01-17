import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
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
                [0, 3, 2, 1],
                [0,1,4,6],
                [1,4,5,2],
                [6,7,5,4],
                [5,2,3,7],
                [7,6,0,3]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        return x.parameters['position'][0] >= 0 and x.parameters['position'][0]< 7\
        and x.parameters['position'][0] + x.parameters['width'] >= 0 and x.parameters['position'][0] + x.parameters['width'] <self.parameters['width'] \
        and x.parameters['position'][1] == 0\
        and x.parameters['thickness']== self.parameters['thickness']\
        and x.parameters['position'][2] >= 0 and x.parameters['position'][2]<self.parameters['height']\
        and x.parameters['position'][2] + x.parameters['height'] >= 0 and x.parameters['position'][2] + x.parameters['height'] < self.parameters['height']
                    
      
      
    # Creates the new sections for the object x
    def createNewSections(self, x):
        liste=[]
        s=0        
        if x.parameters['position'][0]-self.parameters['position'][0]!=0:
            s=Section({'width':x.parameters['position'][0]-self.parameters['position'][0], 'height':2.6, 'thickness':0.2, 'position': self.parameters['position']})
            liste.append(s)
        if self.parameters['position'][1]-x.parameters['position'][1]!=0:
            s=Section({'width':x.parameters['width'], 'height':self.parameters['position'][1]-x.parameters['position'][1], 'thickness':0.2,\
                       'position':[x.parameters['position'][0]-self.parameters['position'][0],0,self.parameters['position'][1]-x.parameters['position'][1]] })
            liste.append(s)
        if x.parameters['position'][1]-self.parameters['position'][1]!=0:
            s=Section({'width':x.parameters['width'], 'height':x.parameters['position'][1]-self.parameters['position'][1], 'thickness':0.2,\
                       'position':[x.parameters['position'][0]-self.parameters['position'][0],0,x.parameters['position'][1]-self.parameters['position'][1]] }) 
            liste.append(s)
        if self.parameters['position'][0]-x.parameters['position'][0]!=0:
            s=Section({'width':self.parameters['position'][0]-x.parameters['position'][0], 'height':self.parameters['position'][2], 'thickness':0.2,\
                       'position':[self.parameters['position'][0]-x.parameters['position'][0],0,self.parameters['position'][2]] }) 
            liste.append(s)    
            
        return liste   
            
    def drawEdges(self):
        
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)   
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.1, 0.1, 0.1]) 
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv( [self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glEnd()
                    
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)   
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.1, 0.1, 0.1]) 
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'],0])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)   
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.1, 0.1, 0.1]) 
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)   
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.1, 0.1, 0.1]) 
        gl.glVertex3fv([0, self.parameters['thickness'],0])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'],0])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)   
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.1, 0.1, 0.1]) 
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv( [self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv( [self.parameters['width'], self.parameters['thickness'],0])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)   
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.1, 0.1, 0.1])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'],0])
        gl.glVertex3fv( [0, self.parameters['thickness'],0])
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glEnd()
        
        gl.glPopMatrix()
    # Draws the faces
    def draw(self):
        
        if self.parameters['edges']:
            self.drawEdges()
            
            
        
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glPushMatrix()

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv( [self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'],0])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([0, 0, self.parameters['height']])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, self.parameters['height']])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([0, self.parameters['thickness'],0])
        gl.glVertex3fv([0, self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv( [self.parameters['width'], self.parameters['thickness'],0])
        gl.glEnd()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'], self.parameters['height']])
        gl.glVertex3fv( [self.parameters['width'], 0, self.parameters['height']])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glVertex3fv( [self.parameters['width'], self.parameters['thickness'],0])
        gl.glEnd()
         
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
        gl.glVertex3fv([self.parameters['width'], self.parameters['thickness'],0])
        gl.glVertex3fv( [0, self.parameters['thickness'],0])
        gl.glVertex3fv([0, 0, 0])
        gl.glVertex3fv([self.parameters['width'], 0, 0])
        gl.glEnd()

        gl.glPopMatrix()
