import pygame #Impordime pygame'i

#Defineerime funktsiooni, mis joonistab ruudustiku
def draw_grid(screen, ruudu_suurus, read, veerud, joone_värv):
    for i in range(read): #Esimene tsükel, mis käib läbi kõik read
        for j in range(veerud): #Teine tsükel, mis käib läbi kõik veerud
            rect = pygame.Rect(j * ruudu_suurus, i * ruudu_suurus, ruudu_suurus, ruudu_suurus) #Loon rect objekti (x-koordinaat, y-koordinaat, laius ja kõrgus)
            pygame.draw.rect(screen, joone_värv, rect, 1) #Joonistab kasti (ekraani väärtus, joone värv, kast ja joone laius)


# Loome Pygame'i ekraani
pygame.init() #Algatan pygame'i
screen = pygame.display.set_mode((640, 480)) #Määrab akna suuruse
pygame.display.set_caption("Ruudustik") #Määrab praeguse akna pealkirja

# Määrame parameetrid
ruudu_suurus = 20 #Määrab ruudu suuruse
read = 24 #Määrab ridade arvu
veerud = 32 #Määrab veergude arvu
joone_värv = (255, 0, 0)  #Määrab joone värvi

#Ristist sulgemine
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Joonistame ekraani täis ruute
    screen.fill((150, 255, 150))  #Roheline värv taustaks
    draw_grid(screen, ruudu_suurus, read, veerud, joone_värv) #Joonistab ekraanile ruudustiku
    pygame.display.update() #Uuendab ekranni

#Lõpetame Pygame'i
pygame.quit()




