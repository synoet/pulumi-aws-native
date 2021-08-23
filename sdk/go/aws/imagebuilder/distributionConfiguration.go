// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package imagebuilder

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
type DistributionConfiguration struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
	Distributions DistributionConfigurationDistributionArrayOutput `pulumi:"distributions"`
	Name          pulumi.StringOutput                              `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewDistributionConfiguration registers a new resource with the given unique name, arguments, and options.
func NewDistributionConfiguration(ctx *pulumi.Context,
	name string, args *DistributionConfigurationArgs, opts ...pulumi.ResourceOption) (*DistributionConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Distributions == nil {
		return nil, errors.New("invalid value for required argument 'Distributions'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource DistributionConfiguration
	err := ctx.RegisterResource("aws-native:imagebuilder:DistributionConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDistributionConfiguration gets an existing DistributionConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDistributionConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DistributionConfigurationState, opts ...pulumi.ResourceOption) (*DistributionConfiguration, error) {
	var resource DistributionConfiguration
	err := ctx.ReadResource("aws-native:imagebuilder:DistributionConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DistributionConfiguration resources.
type distributionConfigurationState struct {
}

type DistributionConfigurationState struct {
}

func (DistributionConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*distributionConfigurationState)(nil)).Elem()
}

type distributionConfigurationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
	Description *string `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
	Distributions []DistributionConfigurationDistribution `pulumi:"distributions"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name
	Name string `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a DistributionConfiguration resource.
type DistributionConfigurationArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
	Description pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
	Distributions DistributionConfigurationDistributionArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name
	Name pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
	Tags pulumi.StringMapInput
}

func (DistributionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*distributionConfigurationArgs)(nil)).Elem()
}

type DistributionConfigurationInput interface {
	pulumi.Input

	ToDistributionConfigurationOutput() DistributionConfigurationOutput
	ToDistributionConfigurationOutputWithContext(ctx context.Context) DistributionConfigurationOutput
}

func (*DistributionConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((*DistributionConfiguration)(nil))
}

func (i *DistributionConfiguration) ToDistributionConfigurationOutput() DistributionConfigurationOutput {
	return i.ToDistributionConfigurationOutputWithContext(context.Background())
}

func (i *DistributionConfiguration) ToDistributionConfigurationOutputWithContext(ctx context.Context) DistributionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DistributionConfigurationOutput)
}

type DistributionConfigurationOutput struct{ *pulumi.OutputState }

func (DistributionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DistributionConfiguration)(nil))
}

func (o DistributionConfigurationOutput) ToDistributionConfigurationOutput() DistributionConfigurationOutput {
	return o
}

func (o DistributionConfigurationOutput) ToDistributionConfigurationOutputWithContext(ctx context.Context) DistributionConfigurationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DistributionConfigurationOutput{})
}
