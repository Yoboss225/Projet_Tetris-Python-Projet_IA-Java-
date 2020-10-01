package filrouge;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Start
{

   
    public static void main (String [] args) 
    {



        /*ACTIVITE*/

        Activity options = new Activity ("Choisir mes options", 20);
        Activity ip = new Activity ("Inscription pédagogique", 30);
        Activity a1 = new Activity ("a1", 20);
        Activity a2 = new Activity ("a2", 30);
        Activity a3 = new Activity ("a3", 20);
        Activity a4 = new Activity ("a4", 60);
        Activity a5 = new Activity ("a5", 30);

        /*LISTE D'ACTIVITE*/
        ArrayList<Activity> listAct = new ArrayList<>(){{
        add(a1);
        add(a2);
        add(a3);
        add(a4);
        add(a5);
        

        }};

        /*CONTRAINTES*/

        PrecedenceConstraintWithGap c1 = new PrecedenceConstraintWithGap (a1, a2,30);
        PrecedenceConstraint c2 = new PrecedenceConstraint(a2,a3);
        PrecedenceConstraint c3 = new PrecedenceConstraint(a3,a4);
        MeetConstraint c4 = new MeetConstraint(a4,a5);
        MaxSpanConstraint c5 = new MaxSpanConstraint(listAct,3);

        /*HEURES*/

        int neufHeures = 9;
        int dixHeures = 10;
        int onzeHeures = 11;

        
       

        /*TESTS CONTRAINTES*/
        // Test avec une programmation censée satisfaire la contrainte
        /*if ( ! contrainte.isSatisfied(neufHeures, onzeHeures) ) {
            System.out.println("Mon programme ne marche pas.");
            System.out.println("Il aurait dû trouver que la contrainte est satisfaite.");
        } else {
            System.out.println("Mon programme passe le premier test avec succès.");
        }a4,a5,edt

        // Test avec une programmation censée ne pas satisfaire la contrainte
        if ( contrainte.isSatisfied(dixHeures, neufHeures) ) {
            System.out.println("Mon programme ne marche pas.");
            System.out.println("Il aurait dû trouver que la contrainte n'est pas satisfaite.");
        } else {
            System.out.println("Mon programme passe le deuxième test avec succès.");
        }
                            
        // Test avec une programmation censée ne pas satisfaire la contrainte (car la première
        // activité finirait après le début de la seconde)
        if ( contrainte.isSatisfied(neufHeures, dixHeures) ) {
            System.out.println("Mon programme ne marche pas.");
            System.out.println("Il aurait dû trouver que la contrainte n'est pas satisfaite.");
        } else {
            System.out.println("Mon programme passe le troisième test avec succès.");
        }
*/
        /*TEST EMPLOI DU TEMPS AVEC CONTRAINTES*/
        HashMap<Activity, Integer> edt = new HashMap<> ();
        edt.put(a1, 9);
        edt.put(a2, 10);
        edt.put(a3, 11);
        edt.put(a4, 12);
        edt.put(a5, 13);
        System.out.println("L'emploi du temps satisfait-il c1 ? " + c1.isSatisfiedBySchedule(edt));
        System.out.println("L'emploi du temps satisfait-il c2 ? " + c2.isSatisfiedBySchedule(edt));
        System.out.println("L'emploi du temps satisfait-il c3 ? " + c3.isSatisfiedBySchedule(edt));
        System.out.println("L'emploi du temps satisfait-il c4 ? " + c4.isSatisfied(10,11));
        System.out.println("L'emploi du temps satisfait-il c5 ? " + c5.isSatisfiedBySchedule(edt));
    
        
        /*TEST AVEC VERIFIEUR*/

        Verifier verifieur = new Verifier();

        // Contrainte : activité1 doit être planifiée avant activité2
        verifieur.addObject(new PrecedenceConstraint(a1, a2));

        // Contrainte : activité4 doit commencer précisément quand activité3 se termine
        /*verifieur.addObject(new MeetConstraint(a3, a4));*/

        // Contrainte : activité1, activité2 et activité3 doivent toutes
        // être exécutées en au plus 90 minutes
        ArrayList<Activity> ensemble = new ArrayList<>();
        
        ensemble.add(a1);
        ensemble.add(a2);
        ensemble.add(a3);
        
        MaxSpanConstraint contrainteEnsemble = new MaxSpanConstraint(ensemble, 90);
        verifieur.addObject(contrainteEnsemble);

        
        

        System.out.println("L'emploi du temps satisfait-il toutes les contraintes ? ");
        
        if (verifieur.verify(edt))
        {
            System.out.println("Oui");
        } 
        else
        {
            System.out.println("Non");
        }
    

      /*INSTERACTIVE*/
      

    
   

    Scanner sc1 = new Scanner(System.in);
    System.out.println("Veuillez saisir la duree de l'activite maths: ");
    int x1 = sc1.nextInt();

    Scanner sc2 = new Scanner(System.in);
    System.out.println("Veuillez saisir la duree de l'activite anglais: ");
    int x2 = sc2.nextInt();

    Scanner sc3 = new Scanner(System.in);
    System.out.println("Veuillez saisir la duree de l'activite français: ");
    int x3 = sc3.nextInt();

    Scanner sc4 = new Scanner(System.in);
    System.out.println("Veuillez saisir la duree de l'activite physique: ");
    int x4 = sc4.nextInt();

    Scanner sc5 = new Scanner(System.in);
    System.out.println("Veuillez saisir la duree de l'activite sciences: ");
    int x5 = sc5.nextInt();




    Scanner sc11 = new Scanner(System.in);
    System.out.println("Veuillez saisir l'heure du debut de l'activite maths: ");
    int h1 = sc11.nextInt();

    Scanner sc22 = new Scanner(System.in);
    System.out.println("Veuillez saisir l'heure du debut de l'activite anglais: ");
    int h2 = sc22.nextInt();

    Scanner sc33 = new Scanner(System.in);
    System.out.println("Veuillez saisir l'heure du debut de l'activite français: ");
    int h3 = sc33.nextInt();

    Scanner sc44 = new Scanner(System.in);
    System.out.println("Veuillez saisir l'heure du debut de l'activite physique: ");
    int h4 = sc44.nextInt();

    Scanner sc55 = new Scanner(System.in);
    System.out.println("Veuillez saisir l'heure du debut de l'activite sciences: ");
    int h5 = sc55.nextInt();




    Activity maths = new Activity ("maths",x1);
    Activity anglais = new Activity ("anglais",x2);
    Activity français = new Activity ("français",x3);
    Activity physique = new Activity ("physique",x4);
    Activity sciences = new Activity ("sciences",x5);


    PrecedenceConstraintWithGap cont1 = new PrecedenceConstraintWithGap (anglais,sciences,30);
    PrecedenceConstraint cont2 = new PrecedenceConstraint(maths,français);
    PrecedenceConstraint cont3 = new PrecedenceConstraint(sciences,physique);


    HashMap<Activity, Integer> emploi = new HashMap<> ();
        emploi.put(maths, h1);
        emploi.put(anglais, h2);
        emploi.put(français, h3);
        emploi.put(physique, h4);
        emploi.put(sciences, h5);
    
    

    Verifier verifieur2 = new Verifier();
    verifieur2.addObject(cont1);
    verifieur2.addObject(cont2);
    verifieur2.addObject(cont3);

    System.out.println("L'emploi du temps satisfait-il toutes les contraintes ? ");
        
        if (verifieur2.verify(emploi))
        {
            System.out.println("Oui");
        } 
        else
        {
            System.out.println("Non");
        }

     
}

}