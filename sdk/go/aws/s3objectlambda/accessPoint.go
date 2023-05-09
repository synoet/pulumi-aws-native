// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package s3objectlambda

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::S3ObjectLambda::AccessPoint resource is an Amazon S3ObjectLambda resource type that you can use to add computation to S3 actions
type AccessPoint struct {
	pulumi.CustomResourceState

	Alias AccessPointAliasOutput `pulumi:"alias"`
	Arn   pulumi.StringOutput    `pulumi:"arn"`
	// The date and time when the Object lambda Access Point was created.
	CreationDate pulumi.StringOutput `pulumi:"creationDate"`
	// The name you want to assign to this Object lambda Access Point.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
	ObjectLambdaConfiguration AccessPointObjectLambdaConfigurationOutput `pulumi:"objectLambdaConfiguration"`
	PolicyStatus              AccessPointPolicyStatusOutput              `pulumi:"policyStatus"`
	// The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
	PublicAccessBlockConfiguration AccessPointPublicAccessBlockConfigurationOutput `pulumi:"publicAccessBlockConfiguration"`
}

// NewAccessPoint registers a new resource with the given unique name, arguments, and options.
func NewAccessPoint(ctx *pulumi.Context,
	name string, args *AccessPointArgs, opts ...pulumi.ResourceOption) (*AccessPoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ObjectLambdaConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'ObjectLambdaConfiguration'")
	}
	var resource AccessPoint
	err := ctx.RegisterResource("aws-native:s3objectlambda:AccessPoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAccessPoint gets an existing AccessPoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAccessPoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AccessPointState, opts ...pulumi.ResourceOption) (*AccessPoint, error) {
	var resource AccessPoint
	err := ctx.ReadResource("aws-native:s3objectlambda:AccessPoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AccessPoint resources.
type accessPointState struct {
}

type AccessPointState struct {
}

func (AccessPointState) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPointState)(nil)).Elem()
}

type accessPointArgs struct {
	// The name you want to assign to this Object lambda Access Point.
	Name *string `pulumi:"name"`
	// The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
	ObjectLambdaConfiguration AccessPointObjectLambdaConfiguration `pulumi:"objectLambdaConfiguration"`
}

// The set of arguments for constructing a AccessPoint resource.
type AccessPointArgs struct {
	// The name you want to assign to this Object lambda Access Point.
	Name pulumi.StringPtrInput
	// The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
	ObjectLambdaConfiguration AccessPointObjectLambdaConfigurationInput
}

func (AccessPointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*accessPointArgs)(nil)).Elem()
}

type AccessPointInput interface {
	pulumi.Input

	ToAccessPointOutput() AccessPointOutput
	ToAccessPointOutputWithContext(ctx context.Context) AccessPointOutput
}

func (*AccessPoint) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessPoint)(nil)).Elem()
}

func (i *AccessPoint) ToAccessPointOutput() AccessPointOutput {
	return i.ToAccessPointOutputWithContext(context.Background())
}

func (i *AccessPoint) ToAccessPointOutputWithContext(ctx context.Context) AccessPointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AccessPointOutput)
}

type AccessPointOutput struct{ *pulumi.OutputState }

func (AccessPointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AccessPoint)(nil)).Elem()
}

func (o AccessPointOutput) ToAccessPointOutput() AccessPointOutput {
	return o
}

func (o AccessPointOutput) ToAccessPointOutputWithContext(ctx context.Context) AccessPointOutput {
	return o
}

func (o AccessPointOutput) Alias() AccessPointAliasOutput {
	return o.ApplyT(func(v *AccessPoint) AccessPointAliasOutput { return v.Alias }).(AccessPointAliasOutput)
}

func (o AccessPointOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessPoint) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The date and time when the Object lambda Access Point was created.
func (o AccessPointOutput) CreationDate() pulumi.StringOutput {
	return o.ApplyT(func(v *AccessPoint) pulumi.StringOutput { return v.CreationDate }).(pulumi.StringOutput)
}

// The name you want to assign to this Object lambda Access Point.
func (o AccessPointOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AccessPoint) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// The Object lambda Access Point Configuration that configures transformations to be applied on the objects on specified S3 Actions
func (o AccessPointOutput) ObjectLambdaConfiguration() AccessPointObjectLambdaConfigurationOutput {
	return o.ApplyT(func(v *AccessPoint) AccessPointObjectLambdaConfigurationOutput { return v.ObjectLambdaConfiguration }).(AccessPointObjectLambdaConfigurationOutput)
}

func (o AccessPointOutput) PolicyStatus() AccessPointPolicyStatusOutput {
	return o.ApplyT(func(v *AccessPoint) AccessPointPolicyStatusOutput { return v.PolicyStatus }).(AccessPointPolicyStatusOutput)
}

// The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
func (o AccessPointOutput) PublicAccessBlockConfiguration() AccessPointPublicAccessBlockConfigurationOutput {
	return o.ApplyT(func(v *AccessPoint) AccessPointPublicAccessBlockConfigurationOutput {
		return v.PublicAccessBlockConfiguration
	}).(AccessPointPublicAccessBlockConfigurationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AccessPointInput)(nil)).Elem(), &AccessPoint{})
	pulumi.RegisterOutputType(AccessPointOutput{})
}
