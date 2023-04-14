// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalogappregistry

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation.
type AttributeGroupAssociation struct {
	pulumi.CustomResourceState

	// The name or the Id of the Application.
	Application    pulumi.StringOutput `pulumi:"application"`
	ApplicationArn pulumi.StringOutput `pulumi:"applicationArn"`
	// The name or the Id of the AttributeGroup.
	AttributeGroup    pulumi.StringOutput `pulumi:"attributeGroup"`
	AttributeGroupArn pulumi.StringOutput `pulumi:"attributeGroupArn"`
}

// NewAttributeGroupAssociation registers a new resource with the given unique name, arguments, and options.
func NewAttributeGroupAssociation(ctx *pulumi.Context,
	name string, args *AttributeGroupAssociationArgs, opts ...pulumi.ResourceOption) (*AttributeGroupAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Application == nil {
		return nil, errors.New("invalid value for required argument 'Application'")
	}
	if args.AttributeGroup == nil {
		return nil, errors.New("invalid value for required argument 'AttributeGroup'")
	}
	var resource AttributeGroupAssociation
	err := ctx.RegisterResource("aws-native:servicecatalogappregistry:AttributeGroupAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAttributeGroupAssociation gets an existing AttributeGroupAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAttributeGroupAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AttributeGroupAssociationState, opts ...pulumi.ResourceOption) (*AttributeGroupAssociation, error) {
	var resource AttributeGroupAssociation
	err := ctx.ReadResource("aws-native:servicecatalogappregistry:AttributeGroupAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AttributeGroupAssociation resources.
type attributeGroupAssociationState struct {
}

type AttributeGroupAssociationState struct {
}

func (AttributeGroupAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*attributeGroupAssociationState)(nil)).Elem()
}

type attributeGroupAssociationArgs struct {
	// The name or the Id of the Application.
	Application string `pulumi:"application"`
	// The name or the Id of the AttributeGroup.
	AttributeGroup string `pulumi:"attributeGroup"`
}

// The set of arguments for constructing a AttributeGroupAssociation resource.
type AttributeGroupAssociationArgs struct {
	// The name or the Id of the Application.
	Application pulumi.StringInput
	// The name or the Id of the AttributeGroup.
	AttributeGroup pulumi.StringInput
}

func (AttributeGroupAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*attributeGroupAssociationArgs)(nil)).Elem()
}

type AttributeGroupAssociationInput interface {
	pulumi.Input

	ToAttributeGroupAssociationOutput() AttributeGroupAssociationOutput
	ToAttributeGroupAssociationOutputWithContext(ctx context.Context) AttributeGroupAssociationOutput
}

func (*AttributeGroupAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((**AttributeGroupAssociation)(nil)).Elem()
}

func (i *AttributeGroupAssociation) ToAttributeGroupAssociationOutput() AttributeGroupAssociationOutput {
	return i.ToAttributeGroupAssociationOutputWithContext(context.Background())
}

func (i *AttributeGroupAssociation) ToAttributeGroupAssociationOutputWithContext(ctx context.Context) AttributeGroupAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AttributeGroupAssociationOutput)
}

type AttributeGroupAssociationOutput struct{ *pulumi.OutputState }

func (AttributeGroupAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AttributeGroupAssociation)(nil)).Elem()
}

func (o AttributeGroupAssociationOutput) ToAttributeGroupAssociationOutput() AttributeGroupAssociationOutput {
	return o
}

func (o AttributeGroupAssociationOutput) ToAttributeGroupAssociationOutputWithContext(ctx context.Context) AttributeGroupAssociationOutput {
	return o
}

// The name or the Id of the Application.
func (o AttributeGroupAssociationOutput) Application() pulumi.StringOutput {
	return o.ApplyT(func(v *AttributeGroupAssociation) pulumi.StringOutput { return v.Application }).(pulumi.StringOutput)
}

func (o AttributeGroupAssociationOutput) ApplicationArn() pulumi.StringOutput {
	return o.ApplyT(func(v *AttributeGroupAssociation) pulumi.StringOutput { return v.ApplicationArn }).(pulumi.StringOutput)
}

// The name or the Id of the AttributeGroup.
func (o AttributeGroupAssociationOutput) AttributeGroup() pulumi.StringOutput {
	return o.ApplyT(func(v *AttributeGroupAssociation) pulumi.StringOutput { return v.AttributeGroup }).(pulumi.StringOutput)
}

func (o AttributeGroupAssociationOutput) AttributeGroupArn() pulumi.StringOutput {
	return o.ApplyT(func(v *AttributeGroupAssociation) pulumi.StringOutput { return v.AttributeGroupArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AttributeGroupAssociationInput)(nil)).Elem(), &AttributeGroupAssociation{})
	pulumi.RegisterOutputType(AttributeGroupAssociationOutput{})
}
