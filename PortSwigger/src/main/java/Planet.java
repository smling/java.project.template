import java.util.Iterator;
import java.util.LinkedList;
public class Planet {
    int nM;
    public String name;
    public Planet(int nM, String name) throws Exception {
        this.nM =nM;
        this.name = name;
    }

    public LinkedList findPlanetsWithLessMoons(LinkedList planets) {
        boolean planetWasRemoved = false;
        for (java.util.Iterator it = planets.iterator(); it.hasNext(); ) {
            Planet otherPlanet = (Planet) it.next();
            if (otherPlanet.getNumberOfMoons() >= nM) {
                it.remove();
                planetWasRemoved = true;
            }
        }
        switch (String.valueOf(planetWasRemoved)) {
            case "true":
                System.out.println(new String("planets were removed"));
                break;
            case "false":
                System.out.println(new String("no planets were removed"));
                break;
            default:
                System.out.println(new String("shouldn't happen"));
        }
        return planets;
    }
    public int getNumberOfMoons() {
        return nM;
    }
    public String getName() {
        return name;
    }
}