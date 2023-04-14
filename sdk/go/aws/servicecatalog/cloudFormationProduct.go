// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package servicecatalog

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ServiceCatalog::CloudFormationProduct
//
// Deprecated: CloudFormationProduct is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type CloudFormationProduct struct {
	pulumi.CustomResourceState

	AcceptLanguage                 pulumi.StringPtrOutput                                         `pulumi:"acceptLanguage"`
	Description                    pulumi.StringPtrOutput                                         `pulumi:"description"`
	Distributor                    pulumi.StringPtrOutput                                         `pulumi:"distributor"`
	Name                           pulumi.StringOutput                                            `pulumi:"name"`
	Owner                          pulumi.StringOutput                                            `pulumi:"owner"`
	ProductName                    pulumi.StringOutput                                            `pulumi:"productName"`
	ProductType                    pulumi.StringPtrOutput                                         `pulumi:"productType"`
	ProvisioningArtifactIds        pulumi.StringOutput                                            `pulumi:"provisioningArtifactIds"`
	ProvisioningArtifactNames      pulumi.StringOutput                                            `pulumi:"provisioningArtifactNames"`
	ProvisioningArtifactParameters CloudFormationProductProvisioningArtifactPropertiesArrayOutput `pulumi:"provisioningArtifactParameters"`
	ReplaceProvisioningArtifacts   pulumi.BoolPtrOutput                                           `pulumi:"replaceProvisioningArtifacts"`
	SourceConnection               CloudFormationProductSourceConnectionPtrOutput                 `pulumi:"sourceConnection"`
	SupportDescription             pulumi.StringPtrOutput                                         `pulumi:"supportDescription"`
	SupportEmail                   pulumi.StringPtrOutput                                         `pulumi:"supportEmail"`
	SupportUrl                     pulumi.StringPtrOutput                                         `pulumi:"supportUrl"`
	Tags                           CloudFormationProductTagArrayOutput                            `pulumi:"tags"`
}

// NewCloudFormationProduct registers a new resource with the given unique name, arguments, and options.
func NewCloudFormationProduct(ctx *pulumi.Context,
	name string, args *CloudFormationProductArgs, opts ...pulumi.ResourceOption) (*CloudFormationProduct, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Owner == nil {
		return nil, errors.New("invalid value for required argument 'Owner'")
	}
	var resource CloudFormationProduct
	err := ctx.RegisterResource("aws-native:servicecatalog:CloudFormationProduct", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCloudFormationProduct gets an existing CloudFormationProduct resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCloudFormationProduct(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CloudFormationProductState, opts ...pulumi.ResourceOption) (*CloudFormationProduct, error) {
	var resource CloudFormationProduct
	err := ctx.ReadResource("aws-native:servicecatalog:CloudFormationProduct", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CloudFormationProduct resources.
type cloudFormationProductState struct {
}

type CloudFormationProductState struct {
}

func (CloudFormationProductState) ElementType() reflect.Type {
	return reflect.TypeOf((*cloudFormationProductState)(nil)).Elem()
}

type cloudFormationProductArgs struct {
	AcceptLanguage                 *string                                               `pulumi:"acceptLanguage"`
	Description                    *string                                               `pulumi:"description"`
	Distributor                    *string                                               `pulumi:"distributor"`
	Name                           *string                                               `pulumi:"name"`
	Owner                          string                                                `pulumi:"owner"`
	ProductType                    *string                                               `pulumi:"productType"`
	ProvisioningArtifactParameters []CloudFormationProductProvisioningArtifactProperties `pulumi:"provisioningArtifactParameters"`
	ReplaceProvisioningArtifacts   *bool                                                 `pulumi:"replaceProvisioningArtifacts"`
	SourceConnection               *CloudFormationProductSourceConnection                `pulumi:"sourceConnection"`
	SupportDescription             *string                                               `pulumi:"supportDescription"`
	SupportEmail                   *string                                               `pulumi:"supportEmail"`
	SupportUrl                     *string                                               `pulumi:"supportUrl"`
	Tags                           []CloudFormationProductTag                            `pulumi:"tags"`
}

// The set of arguments for constructing a CloudFormationProduct resource.
type CloudFormationProductArgs struct {
	AcceptLanguage                 pulumi.StringPtrInput
	Description                    pulumi.StringPtrInput
	Distributor                    pulumi.StringPtrInput
	Name                           pulumi.StringPtrInput
	Owner                          pulumi.StringInput
	ProductType                    pulumi.StringPtrInput
	ProvisioningArtifactParameters CloudFormationProductProvisioningArtifactPropertiesArrayInput
	ReplaceProvisioningArtifacts   pulumi.BoolPtrInput
	SourceConnection               CloudFormationProductSourceConnectionPtrInput
	SupportDescription             pulumi.StringPtrInput
	SupportEmail                   pulumi.StringPtrInput
	SupportUrl                     pulumi.StringPtrInput
	Tags                           CloudFormationProductTagArrayInput
}

func (CloudFormationProductArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cloudFormationProductArgs)(nil)).Elem()
}

type CloudFormationProductInput interface {
	pulumi.Input

	ToCloudFormationProductOutput() CloudFormationProductOutput
	ToCloudFormationProductOutputWithContext(ctx context.Context) CloudFormationProductOutput
}

func (*CloudFormationProduct) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudFormationProduct)(nil)).Elem()
}

func (i *CloudFormationProduct) ToCloudFormationProductOutput() CloudFormationProductOutput {
	return i.ToCloudFormationProductOutputWithContext(context.Background())
}

func (i *CloudFormationProduct) ToCloudFormationProductOutputWithContext(ctx context.Context) CloudFormationProductOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CloudFormationProductOutput)
}

type CloudFormationProductOutput struct{ *pulumi.OutputState }

func (CloudFormationProductOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudFormationProduct)(nil)).Elem()
}

func (o CloudFormationProductOutput) ToCloudFormationProductOutput() CloudFormationProductOutput {
	return o
}

func (o CloudFormationProductOutput) ToCloudFormationProductOutputWithContext(ctx context.Context) CloudFormationProductOutput {
	return o
}

func (o CloudFormationProductOutput) AcceptLanguage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringPtrOutput { return v.AcceptLanguage }).(pulumi.StringPtrOutput)
}

func (o CloudFormationProductOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o CloudFormationProductOutput) Distributor() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringPtrOutput { return v.Distributor }).(pulumi.StringPtrOutput)
}

func (o CloudFormationProductOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o CloudFormationProductOutput) Owner() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringOutput { return v.Owner }).(pulumi.StringOutput)
}

func (o CloudFormationProductOutput) ProductName() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringOutput { return v.ProductName }).(pulumi.StringOutput)
}

func (o CloudFormationProductOutput) ProductType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringPtrOutput { return v.ProductType }).(pulumi.StringPtrOutput)
}

func (o CloudFormationProductOutput) ProvisioningArtifactIds() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringOutput { return v.ProvisioningArtifactIds }).(pulumi.StringOutput)
}

func (o CloudFormationProductOutput) ProvisioningArtifactNames() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringOutput { return v.ProvisioningArtifactNames }).(pulumi.StringOutput)
}

func (o CloudFormationProductOutput) ProvisioningArtifactParameters() CloudFormationProductProvisioningArtifactPropertiesArrayOutput {
	return o.ApplyT(func(v *CloudFormationProduct) CloudFormationProductProvisioningArtifactPropertiesArrayOutput {
		return v.ProvisioningArtifactParameters
	}).(CloudFormationProductProvisioningArtifactPropertiesArrayOutput)
}

func (o CloudFormationProductOutput) ReplaceProvisioningArtifacts() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.BoolPtrOutput { return v.ReplaceProvisioningArtifacts }).(pulumi.BoolPtrOutput)
}

func (o CloudFormationProductOutput) SourceConnection() CloudFormationProductSourceConnectionPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) CloudFormationProductSourceConnectionPtrOutput {
		return v.SourceConnection
	}).(CloudFormationProductSourceConnectionPtrOutput)
}

func (o CloudFormationProductOutput) SupportDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringPtrOutput { return v.SupportDescription }).(pulumi.StringPtrOutput)
}

func (o CloudFormationProductOutput) SupportEmail() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringPtrOutput { return v.SupportEmail }).(pulumi.StringPtrOutput)
}

func (o CloudFormationProductOutput) SupportUrl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CloudFormationProduct) pulumi.StringPtrOutput { return v.SupportUrl }).(pulumi.StringPtrOutput)
}

func (o CloudFormationProductOutput) Tags() CloudFormationProductTagArrayOutput {
	return o.ApplyT(func(v *CloudFormationProduct) CloudFormationProductTagArrayOutput { return v.Tags }).(CloudFormationProductTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CloudFormationProductInput)(nil)).Elem(), &CloudFormationProduct{})
	pulumi.RegisterOutputType(CloudFormationProductOutput{})
}
