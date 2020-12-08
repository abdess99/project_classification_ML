
def main(db):
  clf,precision,recall=create_tree(db, 'gini', 'random')
  dot_data = tree.export_graphviz(clf)
  print(precision,recall)
