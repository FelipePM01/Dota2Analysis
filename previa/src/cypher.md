LOAD CSV WITH HEADERS FROM {url do git do csv dos jogadores} AS line
CREATE (:Jogador {id:line.id,rank:line.rank,mmr:line.mmr})
LOAD CSV WITH HEADERS FROM {url do git do csv dos jogadores} AS line
MATCH (j1:Jogador{id:line.jogador1})
MATCH (j2:Jogador{id:line.jogador2})
CREATE (j1)-[:jogou_com]->(j2)
MATCH (j1)-[:jogou_com]->(j2)
RETURN j1,j2


CALL algo.pageRank.stream('Jogador', 'jogou_com', {iterations:20, dampingFactor:0.85})
YIELD nodeId, score

RETURN algo.asNode(nodeId).id AS id,score
ORDER BY score DESC


CALL gds.graph.create(
  'communityGraph',
  'Jogador',
  {
    jogou_com: {
      orientation: 'UNDIRECTED'
    }
  }
)
CALL gds.louvain.stream('communityGraph')
YIELD nodeId, communityId
MATCH (j:Jogador {id: gds.util.asNode(nodeId).id})
SET j.community = communityId
RETURN gds.util.asNode(nodeId).id AS id, communityId