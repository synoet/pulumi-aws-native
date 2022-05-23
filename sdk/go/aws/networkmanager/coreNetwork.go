// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkmanager

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS::NetworkManager::CoreNetwork Resource Type Definition.
//
// Deprecated: CoreNetwork is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type CoreNetwork struct {
	pulumi.CustomResourceState

	// The ARN (Amazon resource name) of core network
	CoreNetworkArn pulumi.StringOutput `pulumi:"coreNetworkArn"`
	// The Id of core network
	CoreNetworkId pulumi.StringOutput `pulumi:"coreNetworkId"`
	// The creation time of core network
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The description of core network
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The edges within a core network.
	Edges CoreNetworkEdgeArrayOutput `pulumi:"edges"`
	// The ID of the global network that your core network is a part of.
	GlobalNetworkId pulumi.StringOutput `pulumi:"globalNetworkId"`
	// Owner of the core network
	OwnerAccount pulumi.StringOutput `pulumi:"ownerAccount"`
	// Live policy document for the core network
	PolicyDocument pulumi.StringPtrOutput `pulumi:"policyDocument"`
	// The segments within a core network.
	Segments CoreNetworkSegmentArrayOutput `pulumi:"segments"`
	// The state of core network
	State pulumi.StringOutput `pulumi:"state"`
	// The tags for the global network.
	Tags CoreNetworkTagArrayOutput `pulumi:"tags"`
}

// NewCoreNetwork registers a new resource with the given unique name, arguments, and options.
func NewCoreNetwork(ctx *pulumi.Context,
	name string, args *CoreNetworkArgs, opts ...pulumi.ResourceOption) (*CoreNetwork, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GlobalNetworkId == nil {
		return nil, errors.New("invalid value for required argument 'GlobalNetworkId'")
	}
	var resource CoreNetwork
	err := ctx.RegisterResource("aws-native:networkmanager:CoreNetwork", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCoreNetwork gets an existing CoreNetwork resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCoreNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CoreNetworkState, opts ...pulumi.ResourceOption) (*CoreNetwork, error) {
	var resource CoreNetwork
	err := ctx.ReadResource("aws-native:networkmanager:CoreNetwork", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CoreNetwork resources.
type coreNetworkState struct {
}

type CoreNetworkState struct {
}

func (CoreNetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*coreNetworkState)(nil)).Elem()
}

type coreNetworkArgs struct {
	// The description of core network
	Description *string `pulumi:"description"`
	// The ID of the global network that your core network is a part of.
	GlobalNetworkId string `pulumi:"globalNetworkId"`
	// Live policy document for the core network
	PolicyDocument *string `pulumi:"policyDocument"`
	// The tags for the global network.
	Tags []CoreNetworkTag `pulumi:"tags"`
}

// The set of arguments for constructing a CoreNetwork resource.
type CoreNetworkArgs struct {
	// The description of core network
	Description pulumi.StringPtrInput
	// The ID of the global network that your core network is a part of.
	GlobalNetworkId pulumi.StringInput
	// Live policy document for the core network
	PolicyDocument pulumi.StringPtrInput
	// The tags for the global network.
	Tags CoreNetworkTagArrayInput
}

func (CoreNetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*coreNetworkArgs)(nil)).Elem()
}

type CoreNetworkInput interface {
	pulumi.Input

	ToCoreNetworkOutput() CoreNetworkOutput
	ToCoreNetworkOutputWithContext(ctx context.Context) CoreNetworkOutput
}

func (*CoreNetwork) ElementType() reflect.Type {
	return reflect.TypeOf((**CoreNetwork)(nil)).Elem()
}

func (i *CoreNetwork) ToCoreNetworkOutput() CoreNetworkOutput {
	return i.ToCoreNetworkOutputWithContext(context.Background())
}

func (i *CoreNetwork) ToCoreNetworkOutputWithContext(ctx context.Context) CoreNetworkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CoreNetworkOutput)
}

type CoreNetworkOutput struct{ *pulumi.OutputState }

func (CoreNetworkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CoreNetwork)(nil)).Elem()
}

func (o CoreNetworkOutput) ToCoreNetworkOutput() CoreNetworkOutput {
	return o
}

func (o CoreNetworkOutput) ToCoreNetworkOutputWithContext(ctx context.Context) CoreNetworkOutput {
	return o
}

// The ARN (Amazon resource name) of core network
func (o CoreNetworkOutput) CoreNetworkArn() pulumi.StringOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringOutput { return v.CoreNetworkArn }).(pulumi.StringOutput)
}

// The Id of core network
func (o CoreNetworkOutput) CoreNetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringOutput { return v.CoreNetworkId }).(pulumi.StringOutput)
}

// The creation time of core network
func (o CoreNetworkOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The description of core network
func (o CoreNetworkOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The edges within a core network.
func (o CoreNetworkOutput) Edges() CoreNetworkEdgeArrayOutput {
	return o.ApplyT(func(v *CoreNetwork) CoreNetworkEdgeArrayOutput { return v.Edges }).(CoreNetworkEdgeArrayOutput)
}

// The ID of the global network that your core network is a part of.
func (o CoreNetworkOutput) GlobalNetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringOutput { return v.GlobalNetworkId }).(pulumi.StringOutput)
}

// Owner of the core network
func (o CoreNetworkOutput) OwnerAccount() pulumi.StringOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringOutput { return v.OwnerAccount }).(pulumi.StringOutput)
}

// Live policy document for the core network
func (o CoreNetworkOutput) PolicyDocument() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringPtrOutput { return v.PolicyDocument }).(pulumi.StringPtrOutput)
}

// The segments within a core network.
func (o CoreNetworkOutput) Segments() CoreNetworkSegmentArrayOutput {
	return o.ApplyT(func(v *CoreNetwork) CoreNetworkSegmentArrayOutput { return v.Segments }).(CoreNetworkSegmentArrayOutput)
}

// The state of core network
func (o CoreNetworkOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *CoreNetwork) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// The tags for the global network.
func (o CoreNetworkOutput) Tags() CoreNetworkTagArrayOutput {
	return o.ApplyT(func(v *CoreNetwork) CoreNetworkTagArrayOutput { return v.Tags }).(CoreNetworkTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CoreNetworkInput)(nil)).Elem(), &CoreNetwork{})
	pulumi.RegisterOutputType(CoreNetworkOutput{})
}
