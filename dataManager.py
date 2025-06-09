class dataManager():
    """
    An object that manages data related to simulations, security and graphs.

    Attributes
    ----------
    self.__graphIDs: Dict[str: Dict[str: list[str], str: json]]
        Dictionary of all graphs
    self.__simIDs: Dict[str: DcrGraph]
        Dictionary of all simulations
    self.__access: Dict[str: list[str]]
        A dictionary over which security keys(key) has access to which graphs(item)
    self.__reavailableGid: list[str]:
        A list of recently deleted graphs, which IDs can be used again
    self.__reavailableSid: list[str]:
        A list of recently deleted simulations, which IDs can be used again
        
    Methods
    --------
    findgraph(GID) -> Dict[str: list[str], str: json] | None:
        returns the DcrGraph corresponding to SID
    removeGraph(GID, Auth) -> bool:
        returns a bool of wether the deletion was successful or not
    findSim(SID) -> DcrGraph | None:
        returns the DcrGraph corresponding to SID
    removeSim(SID) -> void:
        deletes a simulation
    findAccess(key) -> list[str] | None
        returns a list of accessible graphs
    checkAccessGraph(header, GID) -> bool
        returns a bool of wether the user has access to the graph or not
    checkAccessSim(header, GID) -> bool
        returns a bool of wether the user has access to the graph or not
    checkLoggedIn(header, GID) -> bool
        returns a bool of wether the requester is logged-in with correct encryption or not
    assignGid() -> str
        returns a GID from __reavailableGid if not empty, else the number instances in __graphIDs
    assignSid() -> str
        returns a SID from __reavailableSid if not empty, else the number instances in __simIDs
    """
    def __init__(self):
        self.__graphIDs = {}
        self.__simIDs = {}
        self.__access = {}
        self.__reavailableGid = []
        self.__reavailableSid = []

    @property
    def graphIDs(self):
        return self.__graphIDs
    
    @graphIDs.setter
    def graphIDs(self, value):
        self.__graphIDs = value

    @property
    def simIDs(self):
        return self.__simIDs
    
    @simIDs.setter
    def simIDs(self, value):
        self.__simIDs = value

    @property
    def access(self):
        return self.__access
    
    @access.setter
    def access(self, value):
        self.__access = value

    @property
    def reavailableGid(self):
        return self.__reavailableGid
    
    @property
    def reavailableSid(self):
        return self.__reavailableSid
    
    """
        Get the graph that matches the GID

        Parameters
        ----------
        GID
            ID of a graph

        Returns
        -------
        graph
            the graph associated with the GID
        """
    def findGraph(self, GID):
        try:
            return self.__graphIDs[GID]
        except:
            return None

    """
        Remove a graph and security assigned to it from the data manager

        Parameters
        ----------
        GID
            ID of a graph
        Auth
            Authentication key

        Returns
        -------
        :returns: Bool of wether the graph deleted or not
        """
    #TODO: Either provide a False case or return type void
    def removeGraph(self, GID, Auth):
        graph = self.__graphIDs.pop(GID)
        SIDs = graph['SIDs']
        for s in SIDs:
            self.__simIDs.pop(s)
        
        self.__access[Auth].remove(GID)

        self.__reavailableGid.append(GID)
        return True
    
    """
        Get the simulation that matches the SID

        Parameters
        ----------
        SID
            ID of a simulation

        Returns
        -------
        simulation
            the DcrGraph object related to the SID
        """
    def findSim(self, SID):
        try:
            return self.__simIDs[SID]
        except:
            return None

    """
        Removes a simulation from the data manager

        Parameters
        ----------
        SID
            ID of a simulation
        """
    def removeSim(self, GID, SID):
        self.__simIDs.pop(SID)
        graph = self.__graphIDs[GID] 
        graph['SIDs'].remove(SID)
        self.__graphIDs[GID]['SIDs'] = graph['SIDs']
        self.__reavailableSid.append(SID)

    """
        Get the accessible graphs associated with a authorization key

        Parameters
        ----------
        key
            authorization key

        Returns
        -------
        graphs
            graphs associated with the authorization key
        """
    def findAccess(self, key):
        try:
            return self.__access[key]
        except:
            return None

    """
        Check if a user has access to a specifc graph

        Parameters
        ----------
        header
            header of the request
        GID
            ID of a graph

        Returns
        -------
        :returns: A bool of wether the user had access or not
        """
    def checkAccessGraph(self, header, GID):
        try:
            key = header['Authorization']
        except:
            return False
        access = self.findAccess(key)
        if access is None:
            return False
        if GID in access:
            return True
        
        return False

    """
        Check if a user has access to a specifc simulation

        Parameters
        ----------
        header
            header of the request
        GID
            ID of a graph
        SID
            ID of a simulation
            
        Returns
        -------
        :returns: A bool of wether the user had access or not
        """
    def checkAccessSim(self, header, GID, SID):
        if self.checkAccessGraph(header, GID):
            graph = self.findGraph(GID)
            if SID in graph['SIDs']:
                return True
        return False
    
    """
        Check if a request uses correct authorization therby checking if logged-in

        Parameters
        ----------
        header
            header of the request

        Returns
        -------
        :returns: A bool of wether the request is authorized as logged-in or not
        """
    def checkLoggedIn(self, header):
        try: 
            if header['Authorization'] == "Basic Og==" or not ('Basic' in header['Authorization']):
                return False
            return True 
        except:
            return False

    """
        Assigns GID based on if there are any IDs made reavailable

        Returns
        -------
        :returns: An ID as a string
        """
    def assignGid(self):
        if self.__reavailableGid:
            return self.__reavailableGid.pop()
        else:
            return str(len(self.__graphIDs))

    """
        Assigns SID based on if there are any IDs made reavailable

        Returns
        -------
        :returns: An ID as a string
        """
    def assignSid(self):
        if self.__reavailableSid:
            return self.__reavailableSid.pop()
        else:
            return str(len(self.__simIDs))
        
