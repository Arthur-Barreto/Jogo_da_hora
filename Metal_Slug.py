# == Start Screen ==
i=0
while start_screen:
    clock.tick(FPS_sc)
    menu.blit(assets["startsc_anim"][i%2],(0,0))
    for event in pg.event.get():
        #Aperte Enter para começar / Quebrar Looping
        if event.type== pg.KEYDOWN: #Detecta Evento de Apertar
            if event.key == pg.K_RETURN:
                start_screen=False
        if event.type == pg.QUIT:
            start_screen = False
    pg.display.update()
    i+=1
#Tela principal
window = pg.display.set_mode((ms_settings.screen_width, ms_settings.screen_height))
pg.display.set_caption("Metal Slug Remake Bom Jogo")
# ===== Game Loop =====
i = 0
while game:
    clock.tick(FPS)
    #Trata Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
        if event.type == pg.K_DOWN:
            pass

    #Saidas
    window.blit(assets["background"],(0,0))
    window.blit(assets["player"][i%11],(300,200))
    #Update
    pg.display.update()
    i += 1
#===== Finalização =====
pg.quit()