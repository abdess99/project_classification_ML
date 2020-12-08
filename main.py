
import graphviz
def main(db):        #Arthur
  """
  db is the the file path
  """
  clf,precision,recall=create_tree(db, 'gini', 'random')
  dot_data = tree.export_graphviz(clf)
  graph = graphviz.Source(dot_data)
  graph.render(db)
  tree.plot_tree(clf) 


