// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package emr

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::EMR::Studio
type Studio struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the EMR Studio.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Specifies whether the Studio authenticates users using single sign-on (SSO) or IAM. Amazon EMR Studio currently only supports SSO authentication.
	AuthMode StudioAuthModeOutput `pulumi:"authMode"`
	// The default Amazon S3 location to back up EMR Studio Workspaces and notebook files. A Studio user can select an alternative Amazon S3 location when creating a Workspace.
	DefaultS3Location pulumi.StringOutput `pulumi:"defaultS3Location"`
	// A detailed description of the Studio.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by VpcId.
	EngineSecurityGroupId pulumi.StringOutput `pulumi:"engineSecurityGroupId"`
	// Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.
	IdpAuthUrl pulumi.StringPtrOutput `pulumi:"idpAuthUrl"`
	// The name of relay state parameter for external Identity Provider.
	IdpRelayStateParameterName pulumi.StringPtrOutput `pulumi:"idpRelayStateParameterName"`
	// A descriptive name for the Amazon EMR Studio.
	Name pulumi.StringOutput `pulumi:"name"`
	// The IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.
	ServiceRole pulumi.StringOutput `pulumi:"serviceRole"`
	// The ID of the EMR Studio.
	StudioId pulumi.StringOutput `pulumi:"studioId"`
	// A list of up to 5 subnet IDs to associate with the Studio. The subnets must belong to the VPC specified by VpcId. Studio users can create a Workspace in any of the specified subnets.
	SubnetIds pulumi.StringArrayOutput `pulumi:"subnetIds"`
	// A list of tags to associate with the Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
	Tags StudioTagArrayOutput `pulumi:"tags"`
	// The unique Studio access URL.
	Url pulumi.StringOutput `pulumi:"url"`
	// The IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies.
	UserRole pulumi.StringPtrOutput `pulumi:"userRole"`
	// The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
	// The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by VpcId.
	WorkspaceSecurityGroupId pulumi.StringOutput `pulumi:"workspaceSecurityGroupId"`
}

// NewStudio registers a new resource with the given unique name, arguments, and options.
func NewStudio(ctx *pulumi.Context,
	name string, args *StudioArgs, opts ...pulumi.ResourceOption) (*Studio, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AuthMode == nil {
		return nil, errors.New("invalid value for required argument 'AuthMode'")
	}
	if args.DefaultS3Location == nil {
		return nil, errors.New("invalid value for required argument 'DefaultS3Location'")
	}
	if args.EngineSecurityGroupId == nil {
		return nil, errors.New("invalid value for required argument 'EngineSecurityGroupId'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.ServiceRole == nil {
		return nil, errors.New("invalid value for required argument 'ServiceRole'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	if args.WorkspaceSecurityGroupId == nil {
		return nil, errors.New("invalid value for required argument 'WorkspaceSecurityGroupId'")
	}
	var resource Studio
	err := ctx.RegisterResource("aws-native:emr:Studio", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStudio gets an existing Studio resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStudio(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StudioState, opts ...pulumi.ResourceOption) (*Studio, error) {
	var resource Studio
	err := ctx.ReadResource("aws-native:emr:Studio", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Studio resources.
type studioState struct {
}

type StudioState struct {
}

func (StudioState) ElementType() reflect.Type {
	return reflect.TypeOf((*studioState)(nil)).Elem()
}

type studioArgs struct {
	// Specifies whether the Studio authenticates users using single sign-on (SSO) or IAM. Amazon EMR Studio currently only supports SSO authentication.
	AuthMode StudioAuthMode `pulumi:"authMode"`
	// The default Amazon S3 location to back up EMR Studio Workspaces and notebook files. A Studio user can select an alternative Amazon S3 location when creating a Workspace.
	DefaultS3Location string `pulumi:"defaultS3Location"`
	// A detailed description of the Studio.
	Description *string `pulumi:"description"`
	// The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by VpcId.
	EngineSecurityGroupId string `pulumi:"engineSecurityGroupId"`
	// Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.
	IdpAuthUrl *string `pulumi:"idpAuthUrl"`
	// The name of relay state parameter for external Identity Provider.
	IdpRelayStateParameterName *string `pulumi:"idpRelayStateParameterName"`
	// A descriptive name for the Amazon EMR Studio.
	Name string `pulumi:"name"`
	// The IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.
	ServiceRole string `pulumi:"serviceRole"`
	// A list of up to 5 subnet IDs to associate with the Studio. The subnets must belong to the VPC specified by VpcId. Studio users can create a Workspace in any of the specified subnets.
	SubnetIds []string `pulumi:"subnetIds"`
	// A list of tags to associate with the Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
	Tags []StudioTag `pulumi:"tags"`
	// The IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies.
	UserRole *string `pulumi:"userRole"`
	// The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
	VpcId string `pulumi:"vpcId"`
	// The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by VpcId.
	WorkspaceSecurityGroupId string `pulumi:"workspaceSecurityGroupId"`
}

// The set of arguments for constructing a Studio resource.
type StudioArgs struct {
	// Specifies whether the Studio authenticates users using single sign-on (SSO) or IAM. Amazon EMR Studio currently only supports SSO authentication.
	AuthMode StudioAuthModeInput
	// The default Amazon S3 location to back up EMR Studio Workspaces and notebook files. A Studio user can select an alternative Amazon S3 location when creating a Workspace.
	DefaultS3Location pulumi.StringInput
	// A detailed description of the Studio.
	Description pulumi.StringPtrInput
	// The ID of the Amazon EMR Studio Engine security group. The Engine security group allows inbound network traffic from the Workspace security group, and it must be in the same VPC specified by VpcId.
	EngineSecurityGroupId pulumi.StringInput
	// Your identity provider's authentication endpoint. Amazon EMR Studio redirects federated users to this endpoint for authentication when logging in to a Studio with the Studio URL.
	IdpAuthUrl pulumi.StringPtrInput
	// The name of relay state parameter for external Identity Provider.
	IdpRelayStateParameterName pulumi.StringPtrInput
	// A descriptive name for the Amazon EMR Studio.
	Name pulumi.StringInput
	// The IAM role that will be assumed by the Amazon EMR Studio. The service role provides a way for Amazon EMR Studio to interoperate with other AWS services.
	ServiceRole pulumi.StringInput
	// A list of up to 5 subnet IDs to associate with the Studio. The subnets must belong to the VPC specified by VpcId. Studio users can create a Workspace in any of the specified subnets.
	SubnetIds pulumi.StringArrayInput
	// A list of tags to associate with the Studio. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters, and an optional value string with a maximum of 256 characters.
	Tags StudioTagArrayInput
	// The IAM user role that will be assumed by users and groups logged in to a Studio. The permissions attached to this IAM role can be scoped down for each user or group using session policies.
	UserRole pulumi.StringPtrInput
	// The ID of the Amazon Virtual Private Cloud (Amazon VPC) to associate with the Studio.
	VpcId pulumi.StringInput
	// The ID of the Amazon EMR Studio Workspace security group. The Workspace security group allows outbound network traffic to resources in the Engine security group, and it must be in the same VPC specified by VpcId.
	WorkspaceSecurityGroupId pulumi.StringInput
}

func (StudioArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*studioArgs)(nil)).Elem()
}

type StudioInput interface {
	pulumi.Input

	ToStudioOutput() StudioOutput
	ToStudioOutputWithContext(ctx context.Context) StudioOutput
}

func (*Studio) ElementType() reflect.Type {
	return reflect.TypeOf((*Studio)(nil))
}

func (i *Studio) ToStudioOutput() StudioOutput {
	return i.ToStudioOutputWithContext(context.Background())
}

func (i *Studio) ToStudioOutputWithContext(ctx context.Context) StudioOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StudioOutput)
}

type StudioOutput struct{ *pulumi.OutputState }

func (StudioOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Studio)(nil))
}

func (o StudioOutput) ToStudioOutput() StudioOutput {
	return o
}

func (o StudioOutput) ToStudioOutputWithContext(ctx context.Context) StudioOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(StudioOutput{})
}
