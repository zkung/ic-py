from ic.canister import Canister
from ic.client import Client
from ic.identity import Identity
from ic.agent import Agent
from ic.candid import Types

iden = Identity()
client = Client()
agent = Agent(iden, client)


# wicp_candid="""
# type Metadata = record {
#   fee : nat;
#   decimals : nat8;
#   owner : principal;
#   logo : text;
#   name : text;
#   totalSupply : nat;
#   symbol : text;
# };
# type Result = variant { Ok : nat; Err : TxError };
# type TokenInfo = record {
#   holderNumber : nat64;
#   deployTime : nat64;
#   metadata : Metadata;
#   historySize : nat64;
#   cycles : nat64;
#   feeTo : principal;
# };
# type TxError = variant {
#   InsufficientAllowance;
#   InsufficientBalance;
#   ErrorOperationStyle;
#   Unauthorized;
#   LedgerTrap;
#   ErrorTo;
#   Other;
#   BlockUsed;
#   AmountTooSmall;
# };
# service : (
#   text,
#   text,
#   text,
#   nat8,
#   nat,
#   principal,
#   nat,
#   principal,
#   principal,
# ) -> {
#   allowance : (principal, principal) -> (nat) query;
#   approve : (principal, nat) -> (Result);
#   balanceOf : (principal) -> (nat) query;
#   decimals : () -> (nat8) query;
#   getAllowanceSize : () -> (nat64) query;
#   getBlockUsed : () -> (vec nat64) query;
#   getHolders : (nat64, nat64) -> (vec record { principal; nat }) query;
#   getMetadata : () -> (Metadata) query;
#   getTokenInfo : () -> (TokenInfo) query;
#   getUserApprovals : (principal) -> (vec record { principal; nat }) query;
#   historySize : () -> (nat64) query;
#   isBlockUsed : (nat64) -> (bool) query;
#   logo : () -> (text) query;
#   mint : (opt vec nat8, nat64) -> (Result);
#   mintFor : (opt vec nat8, nat64, principal) -> (Result);
#   name : () -> (text) query;
#   owner : () -> (principal) query;
#   setFee : (nat) -> ();
#   setFeeTo : (principal) -> ();
#   setGenesis : () -> (Result);
#   setLogo : (text) -> ();
#   setName : (text) -> ();
#   setOwner : (principal) -> ();
#   symbol : () -> (text) query;
#   totalSupply : () -> (nat) query;
#   transfer : (principal, nat) -> (Result);
#   transferFrom : (principal, principal, nat) -> (Result);
#   withdraw : (nat64, text) -> (Result);
# }
# """
# wicp = Canister(agent=agent, canister_id="wjsrf-myaaa-aaaam-qaayq-cai", candid=wicp_candid)
# res = wicp.getTokenInfo()
# print(res)
# res = wicp.totalSupply()
# print(res)


governance_did="""
type AccountIdentifier = record { hash : vec nat8 };
type Action = variant {
  RegisterKnownNeuron : KnownNeuron;
  ManageNeuron : ManageNeuron;
  ExecuteNnsFunction : ExecuteNnsFunction;
  RewardNodeProvider : RewardNodeProvider;
  SetDefaultFollowees : SetDefaultFollowees;
  RewardNodeProviders : RewardNodeProviders;
  ManageNetworkEconomics : NetworkEconomics;
  ApproveGenesisKyc : ApproveGenesisKyc;
  AddOrRemoveNodeProvider : AddOrRemoveNodeProvider;
  Motion : Motion;
};
type AddHotKey = record { new_hot_key : opt principal };
type AddOrRemoveNodeProvider = record { change : opt Change };
type Amount = record { e8s : nat64 };
type ApproveGenesisKyc = record { principals : vec principal };
type Ballot = record { vote : int32; voting_power : nat64 };
type BallotInfo = record { vote : int32; proposal_id : opt NeuronId };
type By = variant {
  NeuronIdOrSubaccount : record {};
  MemoAndController : ClaimOrRefreshNeuronFromAccount;
  Memo : nat64;
};
type Change = variant { ToRemove : NodeProvider; ToAdd : NodeProvider };
type ClaimOrRefresh = record { by : opt By };
type ClaimOrRefreshNeuronFromAccount = record {
  controller : opt principal;
  memo : nat64;
};
type ClaimOrRefreshNeuronFromAccountResponse = record { result : opt Result_1 };
type ClaimOrRefreshResponse = record { refreshed_neuron_id : opt NeuronId };
type Command = variant {
  Spawn : Spawn;
  Split : Split;
  Follow : Follow;
  ClaimOrRefresh : ClaimOrRefresh;
  Configure : Configure;
  RegisterVote : RegisterVote;
  Merge : Merge;
  DisburseToNeuron : DisburseToNeuron;
  MakeProposal : Proposal;
  MergeMaturity : MergeMaturity;
  Disburse : Disburse;
};
type Command_1 = variant {
  Error : GovernanceError;
  Spawn : SpawnResponse;
  Split : SpawnResponse;
  Follow : record {};
  ClaimOrRefresh : ClaimOrRefreshResponse;
  Configure : record {};
  RegisterVote : record {};
  Merge : record {};
  DisburseToNeuron : SpawnResponse;
  MakeProposal : MakeProposalResponse;
  MergeMaturity : MergeMaturityResponse;
  Disburse : DisburseResponse;
};
type Command_2 = variant {
  Spawn : Spawn;
  Split : Split;
  Configure : Configure;
  Merge : Merge;
  DisburseToNeuron : DisburseToNeuron;
  ClaimOrRefreshNeuron : ClaimOrRefresh;
  MergeMaturity : MergeMaturity;
  Disburse : Disburse;
};
type Configure = record { operation : opt Operation };
type Disburse = record {
  to_account : opt AccountIdentifier;
  amount : opt Amount;
};
type DisburseResponse = record { transfer_block_height : nat64 };
type DisburseToNeuron = record {
  dissolve_delay_seconds : nat64;
  kyc_verified : bool;
  amount_e8s : nat64;
  new_controller : opt principal;
  nonce : nat64;
};
type DissolveState = variant {
  DissolveDelaySeconds : nat64;
  WhenDissolvedTimestampSeconds : nat64;
};
type ExecuteNnsFunction = record { nns_function : int32; payload : vec nat8 };
type Follow = record { topic : int32; followees : vec NeuronId };
type Followees = record { followees : vec NeuronId };
type Governance = record {
  default_followees : vec record { int32; Followees };
  wait_for_quiet_threshold_seconds : nat64;
  metrics : opt GovernanceCachedMetrics;
  node_providers : vec NodeProvider;
  economics : opt NetworkEconomics;
  latest_reward_event : opt RewardEvent;
  to_claim_transfers : vec NeuronStakeTransfer;
  short_voting_period_seconds : nat64;
  proposals : vec record { nat64; ProposalData };
  in_flight_commands : vec record { nat64; NeuronInFlightCommand };
  neurons : vec record { nat64; Neuron };
  genesis_timestamp_seconds : nat64;
};
type GovernanceCachedMetrics = record {
  not_dissolving_neurons_e8s_buckets : vec record { nat64; float64 };
  garbage_collectable_neurons_count : nat64;
  neurons_with_invalid_stake_count : nat64;
  not_dissolving_neurons_count_buckets : vec record { nat64; nat64 };
  total_supply_icp : nat64;
  neurons_with_less_than_6_months_dissolve_delay_count : nat64;
  dissolved_neurons_count : nat64;
  total_staked_e8s : nat64;
  not_dissolving_neurons_count : nat64;
  dissolved_neurons_e8s : nat64;
  neurons_with_less_than_6_months_dissolve_delay_e8s : nat64;
  dissolving_neurons_count_buckets : vec record { nat64; nat64 };
  dissolving_neurons_count : nat64;
  dissolving_neurons_e8s_buckets : vec record { nat64; float64 };
  community_fund_total_staked_e8s : nat64;
  timestamp_seconds : nat64;
};
type GovernanceError = record { error_message : text; error_type : int32 };
type IncreaseDissolveDelay = record {
  additional_dissolve_delay_seconds : nat32;
};
type KnownNeuron = record {
  id : opt NeuronId;
  known_neuron_data : opt KnownNeuronData;
};
type KnownNeuronData = record { name : text; description : opt text };
type ListKnownNeuronsResponse = record { known_neurons : vec KnownNeuron };
type ListNeurons = record {
  neuron_ids : vec nat64;
  include_neurons_readable_by_caller : bool;
};
type ListNeuronsResponse = record {
  neuron_infos : vec record { nat64; NeuronInfo };
  full_neurons : vec Neuron;
};
type ListProposalInfo = record {
  include_reward_status : vec int32;
  before_proposal : opt NeuronId;
  limit : nat32;
  exclude_topic : vec int32;
  include_status : vec int32;
};
type ListProposalInfoResponse = record { proposal_info : vec ProposalInfo };
type MakeProposalResponse = record { proposal_id : opt NeuronId };
type ManageNeuron = record {
  id : opt NeuronId;
  command : opt Command;
  neuron_id_or_subaccount : opt NeuronIdOrSubaccount;
};
type ManageNeuronResponse = record { command : opt Command_1 };
type Merge = record { source_neuron_id : opt NeuronId };
type MergeMaturity = record { percentage_to_merge : nat32 };
type MergeMaturityResponse = record {
  merged_maturity_e8s : nat64;
  new_stake_e8s : nat64;
};
type Motion = record { motion_text : text };
type NetworkEconomics = record {
  neuron_minimum_stake_e8s : nat64;
  max_proposals_to_keep_per_topic : nat32;
  neuron_management_fee_per_proposal_e8s : nat64;
  reject_cost_e8s : nat64;
  transaction_fee_e8s : nat64;
  neuron_spawn_dissolve_delay_seconds : nat64;
  minimum_icp_xdr_rate : nat64;
  maximum_node_provider_rewards_e8s : nat64;
};
type Neuron = record {
  id : opt NeuronId;
  controller : opt principal;
  recent_ballots : vec BallotInfo;
  kyc_verified : bool;
  not_for_profit : bool;
  maturity_e8s_equivalent : nat64;
  cached_neuron_stake_e8s : nat64;
  created_timestamp_seconds : nat64;
  aging_since_timestamp_seconds : nat64;
  hot_keys : vec principal;
  account : vec nat8;
  joined_community_fund_timestamp_seconds : opt nat64;
  dissolve_state : opt DissolveState;
  followees : vec record { int32; Followees };
  neuron_fees_e8s : nat64;
  transfer : opt NeuronStakeTransfer;
  known_neuron_data : opt KnownNeuronData;
};
type NeuronId = record { id : nat64 };
type NeuronIdOrSubaccount = variant {
  Subaccount : vec nat8;
  NeuronId : NeuronId;
};
type NeuronInFlightCommand = record {
  command : opt Command_2;
  timestamp : nat64;
};
type NeuronInfo = record {
  dissolve_delay_seconds : nat64;
  recent_ballots : vec BallotInfo;
  created_timestamp_seconds : nat64;
  state : int32;
  stake_e8s : nat64;
  joined_community_fund_timestamp_seconds : opt nat64;
  retrieved_at_timestamp_seconds : nat64;
  known_neuron_data : opt KnownNeuronData;
  voting_power : nat64;
  age_seconds : nat64;
};
type NeuronStakeTransfer = record {
  to_subaccount : vec nat8;
  neuron_stake_e8s : nat64;
  from : opt principal;
  memo : nat64;
  from_subaccount : vec nat8;
  transfer_timestamp : nat64;
  block_height : nat64;
};
type NodeProvider = record {
  id : opt principal;
  reward_account : opt AccountIdentifier;
};
type Operation = variant {
  RemoveHotKey : RemoveHotKey;
  AddHotKey : AddHotKey;
  StopDissolving : record {};
  StartDissolving : record {};
  IncreaseDissolveDelay : IncreaseDissolveDelay;
  JoinCommunityFund : record {};
  SetDissolveTimestamp : SetDissolveTimestamp;
};
type Proposal = record {
  url : text;
  title : opt text;
  action : opt Action;
  summary : text;
};
type ProposalData = record {
  id : opt NeuronId;
  failure_reason : opt GovernanceError;
  ballots : vec record { nat64; Ballot };
  proposal_timestamp_seconds : nat64;
  reward_event_round : nat64;
  failed_timestamp_seconds : nat64;
  reject_cost_e8s : nat64;
  latest_tally : opt Tally;
  decided_timestamp_seconds : nat64;
  proposal : opt Proposal;
  proposer : opt NeuronId;
  wait_for_quiet_state : opt WaitForQuietState;
  executed_timestamp_seconds : nat64;
};
type ProposalInfo = record {
  id : opt NeuronId;
  status : int32;
  topic : int32;
  failure_reason : opt GovernanceError;
  ballots : vec record { nat64; Ballot };
  proposal_timestamp_seconds : nat64;
  reward_event_round : nat64;
  deadline_timestamp_seconds : opt nat64;
  failed_timestamp_seconds : nat64;
  reject_cost_e8s : nat64;
  latest_tally : opt Tally;
  reward_status : int32;
  decided_timestamp_seconds : nat64;
  proposal : opt Proposal;
  proposer : opt NeuronId;
  executed_timestamp_seconds : nat64;
};
type RegisterVote = record { vote : int32; proposal : opt NeuronId };
type RemoveHotKey = record { hot_key_to_remove : opt principal };
type Result = variant { Ok; Err : GovernanceError };
type Result_1 = variant { Error : GovernanceError; NeuronId : NeuronId };
type Result_2 = variant { Ok : Neuron; Err : GovernanceError };
type Result_3 = variant { Ok : RewardNodeProviders; Err : GovernanceError };
type Result_4 = variant { Ok : NeuronInfo; Err : GovernanceError };
type RewardEvent = record {
  day_after_genesis : nat64;
  actual_timestamp_seconds : nat64;
  distributed_e8s_equivalent : nat64;
  settled_proposals : vec NeuronId;
};
type RewardMode = variant {
  RewardToNeuron : RewardToNeuron;
  RewardToAccount : RewardToAccount;
};
type RewardNodeProvider = record {
  node_provider : opt NodeProvider;
  reward_mode : opt RewardMode;
  amount_e8s : nat64;
};
type RewardNodeProviders = record { rewards : vec RewardNodeProvider };
type RewardToAccount = record { to_account : opt AccountIdentifier };
type RewardToNeuron = record { dissolve_delay_seconds : nat64 };
type SetDefaultFollowees = record {
  default_followees : vec record { int32; Followees };
};
type SetDissolveTimestamp = record { dissolve_timestamp_seconds : nat64 };
type Spawn = record { new_controller : opt principal; nonce : opt nat64 };
type SpawnResponse = record { created_neuron_id : opt NeuronId };
type Split = record { amount_e8s : nat64 };
type Tally = record {
  no : nat64;
  yes : nat64;
  total : nat64;
  timestamp_seconds : nat64;
};
type UpdateNodeProvider = record { reward_account : opt AccountIdentifier };
type WaitForQuietState = record { current_deadline_timestamp_seconds : nat64 };
service : (Governance) -> {
  claim_gtc_neurons : (principal, vec NeuronId) -> (Result);
  claim_or_refresh_neuron_from_account : (ClaimOrRefreshNeuronFromAccount) -> (
      ClaimOrRefreshNeuronFromAccountResponse,
    );
  get_full_neuron : (nat64) -> (Result_2) query;
  get_full_neuron_by_id_or_subaccount : (NeuronIdOrSubaccount) -> (
      Result_2,
    ) query;
  get_monthly_node_provider_rewards : () -> (Result_3);
  get_neuron_ids : () -> (vec nat64) query;
  get_neuron_info : (nat64) -> (Result_4) query;
  get_neuron_info_by_id_or_subaccount : (NeuronIdOrSubaccount) -> (
      Result_4,
    ) query;
  get_pending_proposals : () -> (vec ProposalInfo) query;
  get_proposal_info : (nat64) -> (opt ProposalInfo) query;
  list_known_neurons : () -> (ListKnownNeuronsResponse) query;
  list_neurons : (ListNeurons) -> (ListNeuronsResponse) query;
  list_proposals : (ListProposalInfo) -> (ListProposalInfoResponse) query;
  manage_neuron : (ManageNeuron) -> (ManageNeuronResponse);
  transfer_gtc_neuron : (NeuronId, NeuronId) -> (Result);
  update_node_provider : (UpdateNodeProvider) -> (Result) query;
}
"""
governance = Canister(agent=agent, canister_id="rrkah-fqaaa-aaaaa-aaaaq-cai", candid=governance_did)
res = governance.list_proposals(
    {
        'include_reward_status': [], 
        'before_proposal': [],
        'limit': 100, 
        'exclude_topic': [], 
        'include_status': [1]
    }
)
print(res)