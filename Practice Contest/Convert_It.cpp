#include <bits/stdc++.h>
using namespace std;

priority_queue<int> pq;

class BTnode
{
public:
    int data;
    BTnode *leftChild, *rightChild;
    BTnode(int data)
    {
        this->data = data;
        this->leftChild = nullptr;
        this->rightChild = nullptr;
    }
};

BTnode *inputTree()
{
    int val;
    cin >> val;
    BTnode *root = nullptr;

    root = new BTnode(val);

    queue<BTnode *> treeNodes;
    if (root)
        treeNodes.push(root);

    while (!treeNodes.empty())
    {
        BTnode *currentRoot = treeNodes.front();
        treeNodes.pop();

        int valLeft, valRight;
        cin >> valLeft >> valRight;
        BTnode *left = nullptr, *right = nullptr;

        if (valLeft > 0)
            left = new BTnode(valLeft);
        if (valRight > 0)
            right = new BTnode(valRight);

        currentRoot->leftChild = left;
        currentRoot->rightChild = right;

        if (left)
            treeNodes.push(left);
        if (right)
            treeNodes.push(right);
    }

    return root;
}

void levelOrderTraverse(BTnode *root)
{
    if (!root)
    {
        cout << "Tree is empty\n";
        return;
    }

    queue<BTnode *> nodesQueue;
    nodesQueue.push(root);

    while (!nodesQueue.empty())
    {
        BTnode *current = nodesQueue.front();
        nodesQueue.pop();

        pq.push(current->data);

        if (current->leftChild)
            nodesQueue.push(current->leftChild);

        if (current->rightChild)
            nodesQueue.push(current->rightChild);
    }
}

int main()
{
    BTnode *root = inputTree();
    levelOrderTraverse(root);

    int q;
    cin >> q;
    while (q--)
    {
        int i;
        cin >> i;
        if (i == 1)
        {
            int x;
            cin >> x;
            pq.push(x);
        }
        else
        {
            cout << pq.top() << endl;
            pq.pop();
        }
    }

    return 0;
}