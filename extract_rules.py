from decision_tree import tree
import pickle as c


class ExtractRules:

    def __init__(self):
        self.rules = []
        self.left = []
        self.l_id = []
        self.r_id = []
        self.right = []

    def dfs(self, visited, tree, node):
        if node not in visited:

            if len(tree.children(node)) != 0:
                self.left.append(node)
                self.right.append(node)
                visited.append(node)
                child = tree.children(node)
                l = child[0]
                r = child[1]
                # .....left side traversal.......
                l_sub = tree.subtree(l.identifier)
                self.left.append(l.identifier)
                self.l_id.append(l.identifier)
                self.dfs(visited, l_sub, l.identifier)

                # ......right side traversal.......
                r_sub = tree.subtree(r.identifier)
                # tag_val=r.tag
                self.r_id.append(r.identifier)
                tag_val = r.tag.replace('>=', '<')
                self.right.append(r.identifier)
                self.dfs(visited, r_sub, r.identifier)
            else:
                if node in self.r_id:
                    val = self.right

    def create_rules(self, tree, root):
        node = tree.all_nodes()
        paths = tree.paths_to_leaves()
        for path in paths:
            rule = []
            length = len(path) + 1
            p = 0
            for p in range(len(path)):

                if path[p] == root:
                    continue
                else:
                    par = tree.parent(path[p])
                    child = tree.children(par.identifier)

                    if path[p] == child[0].identifier and path[p] in self.left:
                        for n in node:
                            if par.identifier == n.identifier:
                                rule.append(n.tag)

                    else:
                        if path[p] == child[1].identifier and path[p] in self.right:
                            for n in node:
                                if par.identifier == n.identifier:
                                    rule.append(n.tag.replace('>=', '<'))

                    if p == len(path) - 1:

                        par = tree.parent(path[p])
                        child = tree.children(par.identifier)

                        if path[p] == child[0].identifier and path[p] in self.left:
                            for n in node:
                                if child[0].identifier == n.identifier:
                                    rule.append(n.tag)

                        else:

                            if path[p] == child[1].identifier and path[p] in self.right:
                                for n in node:
                                    if child[1].identifier == n.identifier:
                                        rule.append(n.tag.replace('>=', '<'))
            self.rules.append(rule)
        return self.rules

    def save(self, clf, name):
        with open(name, 'wb') as fp:
            c.dump(clf, fp)
        print("Rules Saved")


visited = []  # Set to keep track of visited nodes.
r = ExtractRules()
r.dfs(visited, tree, tree.root)
rules = r.create_rules(tree, tree.root)
r.save(rules, "rules.mdl")
