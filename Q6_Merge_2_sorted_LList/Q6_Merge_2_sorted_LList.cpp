/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        if(l1==NULL && l2==NULL)
            return NULL;
        if(l1 && l2==NULL)
            return l1;
        if(l2 && l1==NULL)
            return l2;
        
        ListNode *l3 = new ListNode(0);
        ListNode *temp = l3;
        
        while(l1 && l2)
        {
            if (l1->val <= l2->val)
            {
                l3->next = new ListNode(l1->val);
                l1 = l1->next;
            }
            else
            {
               l3->next = new ListNode(l2->val);
               l2 = l2->next;
            }
            
            l3 = l3->next;
        }
        
        while(l1)
        {
            l3->next = new ListNode(l1->val);
            l1 = l1->next;
            l3 = l3->next;
        }
        
        while(l2)
        {
            l3->next = new ListNode(l2->val);
            l2 = l2->next;
            l3 = l3->next;
        }
        
        return temp->next;
        
    }
};