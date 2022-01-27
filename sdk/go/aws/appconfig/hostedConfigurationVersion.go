// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appconfig

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppConfig::HostedConfigurationVersion
//
// Deprecated: HostedConfigurationVersion is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type HostedConfigurationVersion struct {
	pulumi.CustomResourceState

	ApplicationId          pulumi.StringOutput     `pulumi:"applicationId"`
	ConfigurationProfileId pulumi.StringOutput     `pulumi:"configurationProfileId"`
	Content                pulumi.StringOutput     `pulumi:"content"`
	ContentType            pulumi.StringOutput     `pulumi:"contentType"`
	Description            pulumi.StringPtrOutput  `pulumi:"description"`
	LatestVersionNumber    pulumi.Float64PtrOutput `pulumi:"latestVersionNumber"`
}

// NewHostedConfigurationVersion registers a new resource with the given unique name, arguments, and options.
func NewHostedConfigurationVersion(ctx *pulumi.Context,
	name string, args *HostedConfigurationVersionArgs, opts ...pulumi.ResourceOption) (*HostedConfigurationVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationId == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationId'")
	}
	if args.ConfigurationProfileId == nil {
		return nil, errors.New("invalid value for required argument 'ConfigurationProfileId'")
	}
	if args.Content == nil {
		return nil, errors.New("invalid value for required argument 'Content'")
	}
	if args.ContentType == nil {
		return nil, errors.New("invalid value for required argument 'ContentType'")
	}
	var resource HostedConfigurationVersion
	err := ctx.RegisterResource("aws-native:appconfig:HostedConfigurationVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHostedConfigurationVersion gets an existing HostedConfigurationVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHostedConfigurationVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HostedConfigurationVersionState, opts ...pulumi.ResourceOption) (*HostedConfigurationVersion, error) {
	var resource HostedConfigurationVersion
	err := ctx.ReadResource("aws-native:appconfig:HostedConfigurationVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HostedConfigurationVersion resources.
type hostedConfigurationVersionState struct {
}

type HostedConfigurationVersionState struct {
}

func (HostedConfigurationVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedConfigurationVersionState)(nil)).Elem()
}

type hostedConfigurationVersionArgs struct {
	ApplicationId          string   `pulumi:"applicationId"`
	ConfigurationProfileId string   `pulumi:"configurationProfileId"`
	Content                string   `pulumi:"content"`
	ContentType            string   `pulumi:"contentType"`
	Description            *string  `pulumi:"description"`
	LatestVersionNumber    *float64 `pulumi:"latestVersionNumber"`
}

// The set of arguments for constructing a HostedConfigurationVersion resource.
type HostedConfigurationVersionArgs struct {
	ApplicationId          pulumi.StringInput
	ConfigurationProfileId pulumi.StringInput
	Content                pulumi.StringInput
	ContentType            pulumi.StringInput
	Description            pulumi.StringPtrInput
	LatestVersionNumber    pulumi.Float64PtrInput
}

func (HostedConfigurationVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hostedConfigurationVersionArgs)(nil)).Elem()
}

type HostedConfigurationVersionInput interface {
	pulumi.Input

	ToHostedConfigurationVersionOutput() HostedConfigurationVersionOutput
	ToHostedConfigurationVersionOutputWithContext(ctx context.Context) HostedConfigurationVersionOutput
}

func (*HostedConfigurationVersion) ElementType() reflect.Type {
	return reflect.TypeOf((**HostedConfigurationVersion)(nil)).Elem()
}

func (i *HostedConfigurationVersion) ToHostedConfigurationVersionOutput() HostedConfigurationVersionOutput {
	return i.ToHostedConfigurationVersionOutputWithContext(context.Background())
}

func (i *HostedConfigurationVersion) ToHostedConfigurationVersionOutputWithContext(ctx context.Context) HostedConfigurationVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HostedConfigurationVersionOutput)
}

type HostedConfigurationVersionOutput struct{ *pulumi.OutputState }

func (HostedConfigurationVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**HostedConfigurationVersion)(nil)).Elem()
}

func (o HostedConfigurationVersionOutput) ToHostedConfigurationVersionOutput() HostedConfigurationVersionOutput {
	return o
}

func (o HostedConfigurationVersionOutput) ToHostedConfigurationVersionOutputWithContext(ctx context.Context) HostedConfigurationVersionOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HostedConfigurationVersionInput)(nil)).Elem(), &HostedConfigurationVersion{})
	pulumi.RegisterOutputType(HostedConfigurationVersionOutput{})
}
