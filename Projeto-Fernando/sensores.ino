/*
Nome do arquivo: sensores.ino
Equipe: João Vítor, Maria Clara e Pedro Matias.
Turma: G93314
*/

// LEDs representando os setores
const int OFICINA_LedVermelho     = 2;
const int GALPAO_1_LedVerde       = 3;
const int GALPAO_2_LedLaranja     = 4;
const int GALPAO_3_LedBranco      = 5;
const int ESCRITORIO_LedAmarelo   = 6;
const int CORREDOR_LedAzul        = 7;
const int AREA_SERVICO_LedVermelho = 8;
const int AREA_EXTERNA_LedVerde   = 9;

void setup() {
  Serial.begin(9600);

  // Configura todos os pinos como saída
  pinMode(OFICINA_LedVermelho, OUTPUT);
  pinMode(GALPAO_1_LedVerde, OUTPUT);
  pinMode(GALPAO_2_LedLaranja, OUTPUT);
  pinMode(GALPAO_3_LedBranco, OUTPUT);
  pinMode(ESCRITORIO_LedAmarelo, OUTPUT);
  pinMode(CORREDOR_LedAzul, OUTPUT);
  pinMode(AREA_SERVICO_LedVermelho, OUTPUT);
  pinMode(AREA_EXTERNA_LedVerde, OUTPUT);

  // Garante tudo apagado inicialmente
  for (int i = 2; i <= 9; i++) {
    digitalWrite(i, LOW);
  }
}

void loop() {

  if (Serial.available()) {
    char comando = Serial.read();

    switch (comando) {

      case 'A': digitalWrite(OFICINA_LedVermelho, HIGH); break;
      case 'a': digitalWrite(OFICINA_LedVermelho, LOW);  break;

      case 'B': digitalWrite(GALPAO_1_LedVerde, HIGH); break;
      case 'b': digitalWrite(GALPAO_1_LedVerde, LOW);  break;

      case 'C': digitalWrite(GALPAO_2_LedLaranja, HIGH); break;
      case 'c': digitalWrite(GALPAO_2_LedLaranja, LOW);  break;

      case 'D': digitalWrite(GALPAO_3_LedBranco, HIGH); break;
      case 'd': digitalWrite(GALPAO_3_LedBranco, LOW);  break;

      case 'E': digitalWrite(ESCRITORIO_LedAmarelo, HIGH); break;
      case 'e': digitalWrite(ESCRITORIO_LedAmarelo, LOW);  break;

      case 'F': digitalWrite(CORREDOR_LedAzul, HIGH); break;
      case 'f': digitalWrite(CORREDOR_LedAzul, LOW);  break;

      case 'G': digitalWrite(AREA_SERVICO_LedVermelho, HIGH); break;
      case 'g': digitalWrite(AREA_SERVICO_LedVermelho, LOW);  break;

      case 'H': digitalWrite(AREA_EXTERNA_LedVerde, HIGH); break;
      case 'h': digitalWrite(AREA_EXTERNA_LedVerde, LOW);  break;

      default:
        Serial.println("COMANDO_INVALIDO");
        break;
    }

    Serial.print("COMANDO_RECEBIDO: ");
    Serial.println(comando);
  }
}