import itertools

# Função para calcular a distância total de uma rota
def calculate_distance(route, distances):
    # Soma as distâncias entre as cidades na rota e retorna à cidade de origem
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1)) + distances[route[-1]][route[0]]

# Função para resolver o TSP usando força bruta
def tsp_brute_force(cities, distances):
    shortest_route = None
    min_distance = float('inf')
    # Gera todas as permutações possíveis das cidades
    for route in itertools.permutations(cities):
        current_distance = calculate_distance(route, distances)
        # Atualiza a rota mais curta se a distância atual for menor
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = route
    return shortest_route, min_distance

# Exemplo de uso
cities = [0, 1, 2, 3]
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Encontra a rota mais curta e a distância mínima
shortest_route, min_distance = tsp_brute_force(cities, distances)
print(f"Rota mais curta: {shortest_route} com distância de {min_distance}")
