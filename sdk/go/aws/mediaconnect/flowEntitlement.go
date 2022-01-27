// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mediaconnect

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::MediaConnect::FlowEntitlement
type FlowEntitlement struct {
	pulumi.CustomResourceState

	// Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
	DataTransferSubscriberFeePercent pulumi.IntPtrOutput `pulumi:"dataTransferSubscriberFeePercent"`
	// A description of the entitlement.
	Description pulumi.StringOutput `pulumi:"description"`
	// The type of encryption that will be used on the output that is associated with this entitlement.
	Encryption FlowEntitlementEncryptionPtrOutput `pulumi:"encryption"`
	// The ARN of the entitlement.
	EntitlementArn pulumi.StringOutput `pulumi:"entitlementArn"`
	//  An indication of whether the entitlement is enabled.
	EntitlementStatus FlowEntitlementEntitlementStatusPtrOutput `pulumi:"entitlementStatus"`
	// The ARN of the flow.
	FlowArn pulumi.StringOutput `pulumi:"flowArn"`
	// The name of the entitlement.
	Name pulumi.StringOutput `pulumi:"name"`
	// The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
	Subscribers pulumi.StringArrayOutput `pulumi:"subscribers"`
}

// NewFlowEntitlement registers a new resource with the given unique name, arguments, and options.
func NewFlowEntitlement(ctx *pulumi.Context,
	name string, args *FlowEntitlementArgs, opts ...pulumi.ResourceOption) (*FlowEntitlement, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.FlowArn == nil {
		return nil, errors.New("invalid value for required argument 'FlowArn'")
	}
	if args.Subscribers == nil {
		return nil, errors.New("invalid value for required argument 'Subscribers'")
	}
	var resource FlowEntitlement
	err := ctx.RegisterResource("aws-native:mediaconnect:FlowEntitlement", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlowEntitlement gets an existing FlowEntitlement resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlowEntitlement(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlowEntitlementState, opts ...pulumi.ResourceOption) (*FlowEntitlement, error) {
	var resource FlowEntitlement
	err := ctx.ReadResource("aws-native:mediaconnect:FlowEntitlement", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FlowEntitlement resources.
type flowEntitlementState struct {
}

type FlowEntitlementState struct {
}

func (FlowEntitlementState) ElementType() reflect.Type {
	return reflect.TypeOf((*flowEntitlementState)(nil)).Elem()
}

type flowEntitlementArgs struct {
	// Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
	DataTransferSubscriberFeePercent *int `pulumi:"dataTransferSubscriberFeePercent"`
	// A description of the entitlement.
	Description string `pulumi:"description"`
	// The type of encryption that will be used on the output that is associated with this entitlement.
	Encryption *FlowEntitlementEncryption `pulumi:"encryption"`
	//  An indication of whether the entitlement is enabled.
	EntitlementStatus *FlowEntitlementEntitlementStatus `pulumi:"entitlementStatus"`
	// The ARN of the flow.
	FlowArn string `pulumi:"flowArn"`
	// The name of the entitlement.
	Name *string `pulumi:"name"`
	// The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
	Subscribers []string `pulumi:"subscribers"`
}

// The set of arguments for constructing a FlowEntitlement resource.
type FlowEntitlementArgs struct {
	// Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
	DataTransferSubscriberFeePercent pulumi.IntPtrInput
	// A description of the entitlement.
	Description pulumi.StringInput
	// The type of encryption that will be used on the output that is associated with this entitlement.
	Encryption FlowEntitlementEncryptionPtrInput
	//  An indication of whether the entitlement is enabled.
	EntitlementStatus FlowEntitlementEntitlementStatusPtrInput
	// The ARN of the flow.
	FlowArn pulumi.StringInput
	// The name of the entitlement.
	Name pulumi.StringPtrInput
	// The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
	Subscribers pulumi.StringArrayInput
}

func (FlowEntitlementArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flowEntitlementArgs)(nil)).Elem()
}

type FlowEntitlementInput interface {
	pulumi.Input

	ToFlowEntitlementOutput() FlowEntitlementOutput
	ToFlowEntitlementOutputWithContext(ctx context.Context) FlowEntitlementOutput
}

func (*FlowEntitlement) ElementType() reflect.Type {
	return reflect.TypeOf((**FlowEntitlement)(nil)).Elem()
}

func (i *FlowEntitlement) ToFlowEntitlementOutput() FlowEntitlementOutput {
	return i.ToFlowEntitlementOutputWithContext(context.Background())
}

func (i *FlowEntitlement) ToFlowEntitlementOutputWithContext(ctx context.Context) FlowEntitlementOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FlowEntitlementOutput)
}

type FlowEntitlementOutput struct{ *pulumi.OutputState }

func (FlowEntitlementOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FlowEntitlement)(nil)).Elem()
}

func (o FlowEntitlementOutput) ToFlowEntitlementOutput() FlowEntitlementOutput {
	return o
}

func (o FlowEntitlementOutput) ToFlowEntitlementOutputWithContext(ctx context.Context) FlowEntitlementOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FlowEntitlementInput)(nil)).Elem(), &FlowEntitlement{})
	pulumi.RegisterOutputType(FlowEntitlementOutput{})
}
