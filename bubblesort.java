public class bubblesort {
    public static void bubble(int arr[]){
        for (int i=0;i<arr.length-1;i++){
            for(int j=0;j<arr.length-1-i;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
    }
    public static void printarr(int arr[]) {
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }

   public static void selectionSort(int arr[]){
        for(int i=0;i<arr.length-1;i++){
            int minpos=i;
            for (int j=i+1;j<arr.length;j++){
                if (arr[minpos]>arr[j]){         //to print in descending order just reverse the sign
                    minpos=j;
                }
            }
            //swap
        int temp=arr[minpos];
        arr[minpos]=arr[i];
        arr[i]=temp;
        }
        

   }
    public static void main(String[] args) {
        int arr[]={5,4,1,3,2};
        selectionSort(arr);
        printarr(arr);
    }
}
