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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        if(n==1 && head->next==NULL)
            return NULL;
        
        ListNode *temp = head;
        int count=0;
        
        while(temp!=NULL)
        {
            count++;
            temp = temp->next; 
        }
        
        //new 'n' from beginning (n = count-n)
        count = count-n;
        
        if(count==0)
            return head->next;
        
        temp = head;
        
        while(count > 1)
        {
            temp = temp->next;
            count--;
        }
        
        temp->next = temp->next->next;
        
        return head;
        
    }
};