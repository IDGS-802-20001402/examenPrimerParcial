

class TuclaseExamen():

    def arithmetic_arranger(self, problemas, ver_solucion=False):
        if len(problemas) > 5:
            return 'Error: Too many problems.'

        linea1 = linea2 = linea3 = linea4 = ''

        for problema in problemas:
            partes = problema.split()

            if len(partes) != 3:
                return "Error: Problem must contain two operands and an operator."
            
            v1, op, v2 = partes[0], partes[1], partes[2]

            if op not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
            
            if not v1.isdigit() or not v2.isdigit():
                return 'Error: Numbers must only contain digits.'

            if len(v1) > 4 or len(v2) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            
            max_len = max(len(v1), len(v2)) + 2
            acomodado1 = v1.rjust(max_len)
            acomodado2 = op + ' ' + v2.rjust(max_len - 2)

            linea1 += acomodado1 + '    '
            linea2 += acomodado2 + '    '
            linea3 += '-' * max_len + '    '

            if ver_solucion:

                if op == '+':
                    solucion = str(int(v1) + int(v2)).rjust(max_len)
                else:
                    solucion = str(int(v1) - int(v2)).rjust(max_len)

                linea4 += solucion + '    '

        problemas_acomodados = linea1.rstrip() + '\n' + linea2.rstrip() + '\n' + linea3.rstrip()

        if ver_solucion:
            problemas_acomodados += '\n' + linea4.rstrip()

        return problemas_acomodados