      let entrada = document.querySelector('textarea')
      let saida = document.querySelector('p')
      let amigos = []
      
      let keys = {
        R(int) {
          if(!amigos[int]) {
            amigos[int] = [0, false]
            console.log("Recebeu uma mensagem do amigo", int, "agora o amigo", int, "esperou", amigos[int][0], "segundos")
          }
          if(amigos[int][1]) {
            console.log("Recebeu uma mensagem do amigo", int, "agora o amigo", int, "esperou", amigos[int][0], "segundos")
            amigos[int][1] = false
          }
        },
        E(int) {
          console.log(amigos)
          if(amigos[int][1] == false) {
            console.log("Enviou uma mensagem ao amigo", int, "agora o amigo", int, "esperou", amigos[int][0], "segundos")
            console.log(amigos)
            amigos[int][1] = true
            console.log(amigos)
          }  
        },
        T(int) {
          for (let i = 0; i < amigos.length; i++) {
            if (amigos[i]) {
              console.log("Se passou", int, "segundos", "agora o amigo", i, "esperou", amigos[i][0], "segundos")
              if (!amigos[i][1]) {
                amigos[i][0] += int
              }
            }
          }
        }
      } 
      document.querySelector('button').addEventListener('click', () => {
        amigos = []
        let registros = entrada.value.split('\n')
        for (let i = 1; i < registros.length; i++) {
          registros[i] = registros[i].split(" ")
        }
        
        for (let i = 1; i < registros.length; i++) {
          keys[registros[i][0]](parseInt(registros[i][1]))

          if(registros[i][0] != 'T' && !amigos[registros[i][1]][1]) {
            amigos[parseInt(registros[i][1])][0]++   
          } else {
            console.log("Este amigo já foi respondido!")
          }
          
          if(i == registros.length - 1) {
            console.log("Chegou aqui!")
            for(let j = 0; j < amigos.length; j++) {
              if(amigos[j]) {
                if(!amigos[j][1]) {
                  amigos[j][0] = -1
                }
              }
            }
          }
        }
        console.log(amigos)
      })

