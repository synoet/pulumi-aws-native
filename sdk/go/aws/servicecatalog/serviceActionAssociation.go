// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html
type ServiceActionAssociation struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
	ProductId pulumi.StringOutput `pulumi:"productId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
	ProvisioningArtifactId pulumi.StringOutput `pulumi:"provisioningArtifactId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
	ServiceActionId pulumi.StringOutput `pulumi:"serviceActionId"`
}

// NewServiceActionAssociation registers a new resource with the given unique name, arguments, and options.
func NewServiceActionAssociation(ctx *pulumi.Context,
	name string, args *ServiceActionAssociationArgs, opts ...pulumi.ResourceOption) (*ServiceActionAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProductId == nil {
		return nil, errors.New("invalid value for required argument 'ProductId'")
	}
	if args.ProvisioningArtifactId == nil {
		return nil, errors.New("invalid value for required argument 'ProvisioningArtifactId'")
	}
	if args.ServiceActionId == nil {
		return nil, errors.New("invalid value for required argument 'ServiceActionId'")
	}
	var resource ServiceActionAssociation
	err := ctx.RegisterResource("aws-native:servicecatalog:ServiceActionAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceActionAssociation gets an existing ServiceActionAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceActionAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceActionAssociationState, opts ...pulumi.ResourceOption) (*ServiceActionAssociation, error) {
	var resource ServiceActionAssociation
	err := ctx.ReadResource("aws-native:servicecatalog:ServiceActionAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceActionAssociation resources.
type serviceActionAssociationState struct {
}

type ServiceActionAssociationState struct {
}

func (ServiceActionAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceActionAssociationState)(nil)).Elem()
}

type serviceActionAssociationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
	ProductId string `pulumi:"productId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
	ProvisioningArtifactId string `pulumi:"provisioningArtifactId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
	ServiceActionId string `pulumi:"serviceActionId"`
}

// The set of arguments for constructing a ServiceActionAssociation resource.
type ServiceActionAssociationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-productid
	ProductId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-provisioningartifactid
	ProvisioningArtifactId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-serviceactionassociation.html#cfn-servicecatalog-serviceactionassociation-serviceactionid
	ServiceActionId pulumi.StringInput
}

func (ServiceActionAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceActionAssociationArgs)(nil)).Elem()
}

type ServiceActionAssociationInput interface {
	pulumi.Input

	ToServiceActionAssociationOutput() ServiceActionAssociationOutput
	ToServiceActionAssociationOutputWithContext(ctx context.Context) ServiceActionAssociationOutput
}

func (*ServiceActionAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceActionAssociation)(nil))
}

func (i *ServiceActionAssociation) ToServiceActionAssociationOutput() ServiceActionAssociationOutput {
	return i.ToServiceActionAssociationOutputWithContext(context.Background())
}

func (i *ServiceActionAssociation) ToServiceActionAssociationOutputWithContext(ctx context.Context) ServiceActionAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceActionAssociationOutput)
}

type ServiceActionAssociationOutput struct{ *pulumi.OutputState }

func (ServiceActionAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ServiceActionAssociation)(nil))
}

func (o ServiceActionAssociationOutput) ToServiceActionAssociationOutput() ServiceActionAssociationOutput {
	return o
}

func (o ServiceActionAssociationOutput) ToServiceActionAssociationOutputWithContext(ctx context.Context) ServiceActionAssociationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ServiceActionAssociationOutput{})
}
