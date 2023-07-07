// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkmanager

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS::NetworkManager::ConnectPeer Resource Type Definition.
type ConnectPeer struct {
	pulumi.CustomResourceState

	// Bgp options for connect peer.
	BgpOptions ConnectPeerBgpOptionsPtrOutput `pulumi:"bgpOptions"`
	// Configuration of the connect peer.
	Configuration ConnectPeerConfigurationOutput `pulumi:"configuration"`
	// The ID of the attachment to connect.
	ConnectAttachmentId pulumi.StringOutput `pulumi:"connectAttachmentId"`
	// The ID of the Connect peer.
	ConnectPeerId pulumi.StringOutput `pulumi:"connectPeerId"`
	// The IP address of a core network.
	CoreNetworkAddress pulumi.StringPtrOutput `pulumi:"coreNetworkAddress"`
	// The ID of the core network.
	CoreNetworkId pulumi.StringOutput `pulumi:"coreNetworkId"`
	// Connect peer creation time.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The Connect peer Regions where edges are located.
	EdgeLocation pulumi.StringOutput `pulumi:"edgeLocation"`
	// The inside IP addresses used for a Connect peer configuration.
	InsideCidrBlocks pulumi.StringArrayOutput `pulumi:"insideCidrBlocks"`
	// The IP address of the Connect peer.
	PeerAddress pulumi.StringOutput `pulumi:"peerAddress"`
	// State of the connect peer.
	State pulumi.StringOutput `pulumi:"state"`
	// An array of key-value pairs to apply to this resource.
	Tags ConnectPeerTagArrayOutput `pulumi:"tags"`
}

// NewConnectPeer registers a new resource with the given unique name, arguments, and options.
func NewConnectPeer(ctx *pulumi.Context,
	name string, args *ConnectPeerArgs, opts ...pulumi.ResourceOption) (*ConnectPeer, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConnectAttachmentId == nil {
		return nil, errors.New("invalid value for required argument 'ConnectAttachmentId'")
	}
	if args.PeerAddress == nil {
		return nil, errors.New("invalid value for required argument 'PeerAddress'")
	}
	var resource ConnectPeer
	err := ctx.RegisterResource("aws-native:networkmanager:ConnectPeer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConnectPeer gets an existing ConnectPeer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnectPeer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConnectPeerState, opts ...pulumi.ResourceOption) (*ConnectPeer, error) {
	var resource ConnectPeer
	err := ctx.ReadResource("aws-native:networkmanager:ConnectPeer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConnectPeer resources.
type connectPeerState struct {
}

type ConnectPeerState struct {
}

func (ConnectPeerState) ElementType() reflect.Type {
	return reflect.TypeOf((*connectPeerState)(nil)).Elem()
}

type connectPeerArgs struct {
	// Bgp options for connect peer.
	BgpOptions *ConnectPeerBgpOptions `pulumi:"bgpOptions"`
	// The ID of the attachment to connect.
	ConnectAttachmentId string `pulumi:"connectAttachmentId"`
	// The IP address of a core network.
	CoreNetworkAddress *string `pulumi:"coreNetworkAddress"`
	// The inside IP addresses used for a Connect peer configuration.
	InsideCidrBlocks []string `pulumi:"insideCidrBlocks"`
	// The IP address of the Connect peer.
	PeerAddress string `pulumi:"peerAddress"`
	// An array of key-value pairs to apply to this resource.
	Tags []ConnectPeerTag `pulumi:"tags"`
}

// The set of arguments for constructing a ConnectPeer resource.
type ConnectPeerArgs struct {
	// Bgp options for connect peer.
	BgpOptions ConnectPeerBgpOptionsPtrInput
	// The ID of the attachment to connect.
	ConnectAttachmentId pulumi.StringInput
	// The IP address of a core network.
	CoreNetworkAddress pulumi.StringPtrInput
	// The inside IP addresses used for a Connect peer configuration.
	InsideCidrBlocks pulumi.StringArrayInput
	// The IP address of the Connect peer.
	PeerAddress pulumi.StringInput
	// An array of key-value pairs to apply to this resource.
	Tags ConnectPeerTagArrayInput
}

func (ConnectPeerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*connectPeerArgs)(nil)).Elem()
}

type ConnectPeerInput interface {
	pulumi.Input

	ToConnectPeerOutput() ConnectPeerOutput
	ToConnectPeerOutputWithContext(ctx context.Context) ConnectPeerOutput
}

func (*ConnectPeer) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectPeer)(nil)).Elem()
}

func (i *ConnectPeer) ToConnectPeerOutput() ConnectPeerOutput {
	return i.ToConnectPeerOutputWithContext(context.Background())
}

func (i *ConnectPeer) ToConnectPeerOutputWithContext(ctx context.Context) ConnectPeerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectPeerOutput)
}

type ConnectPeerOutput struct{ *pulumi.OutputState }

func (ConnectPeerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectPeer)(nil)).Elem()
}

func (o ConnectPeerOutput) ToConnectPeerOutput() ConnectPeerOutput {
	return o
}

func (o ConnectPeerOutput) ToConnectPeerOutputWithContext(ctx context.Context) ConnectPeerOutput {
	return o
}

// Bgp options for connect peer.
func (o ConnectPeerOutput) BgpOptions() ConnectPeerBgpOptionsPtrOutput {
	return o.ApplyT(func(v *ConnectPeer) ConnectPeerBgpOptionsPtrOutput { return v.BgpOptions }).(ConnectPeerBgpOptionsPtrOutput)
}

// Configuration of the connect peer.
func (o ConnectPeerOutput) Configuration() ConnectPeerConfigurationOutput {
	return o.ApplyT(func(v *ConnectPeer) ConnectPeerConfigurationOutput { return v.Configuration }).(ConnectPeerConfigurationOutput)
}

// The ID of the attachment to connect.
func (o ConnectPeerOutput) ConnectAttachmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringOutput { return v.ConnectAttachmentId }).(pulumi.StringOutput)
}

// The ID of the Connect peer.
func (o ConnectPeerOutput) ConnectPeerId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringOutput { return v.ConnectPeerId }).(pulumi.StringOutput)
}

// The IP address of a core network.
func (o ConnectPeerOutput) CoreNetworkAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringPtrOutput { return v.CoreNetworkAddress }).(pulumi.StringPtrOutput)
}

// The ID of the core network.
func (o ConnectPeerOutput) CoreNetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringOutput { return v.CoreNetworkId }).(pulumi.StringOutput)
}

// Connect peer creation time.
func (o ConnectPeerOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The Connect peer Regions where edges are located.
func (o ConnectPeerOutput) EdgeLocation() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringOutput { return v.EdgeLocation }).(pulumi.StringOutput)
}

// The inside IP addresses used for a Connect peer configuration.
func (o ConnectPeerOutput) InsideCidrBlocks() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringArrayOutput { return v.InsideCidrBlocks }).(pulumi.StringArrayOutput)
}

// The IP address of the Connect peer.
func (o ConnectPeerOutput) PeerAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringOutput { return v.PeerAddress }).(pulumi.StringOutput)
}

// State of the connect peer.
func (o ConnectPeerOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectPeer) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o ConnectPeerOutput) Tags() ConnectPeerTagArrayOutput {
	return o.ApplyT(func(v *ConnectPeer) ConnectPeerTagArrayOutput { return v.Tags }).(ConnectPeerTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectPeerInput)(nil)).Elem(), &ConnectPeer{})
	pulumi.RegisterOutputType(ConnectPeerOutput{})
}
