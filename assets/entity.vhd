ENTITY ALU IS
generic(
  Depth : natural := 2;
  Overflow : boolean
);
port (
  A	 : in  std_logic_vector(7 downto 0);		--! ALU A input 8-bit from AC
	B	 : in  std_logic_vector(7 downto 0);		--! ALU B input 8-bit from B-register
  S  : out std_logic_vector(Depth-1 downto 0);		--! ALU output 8-bit to W-bus
	Su : in  std_logic;								--! Low Add, High Sub
	Eu : in  std_logic);								--! Active low enable ALU (tri-state)
END ALU ;
