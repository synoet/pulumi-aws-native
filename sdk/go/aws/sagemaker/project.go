// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SageMaker::Project
type Project struct {
	pulumi.CustomResourceState

	// The time at which the project was created.
	CreationTime       pulumi.StringOutput    `pulumi:"creationTime"`
	ProjectArn         pulumi.StringOutput    `pulumi:"projectArn"`
	ProjectDescription pulumi.StringPtrOutput `pulumi:"projectDescription"`
	ProjectId          pulumi.StringOutput    `pulumi:"projectId"`
	ProjectName        pulumi.StringOutput    `pulumi:"projectName"`
	// The status of a project.
	ProjectStatus ProjectProjectStatusOutput `pulumi:"projectStatus"`
	// Provisioned ServiceCatalog  Details
	ServiceCatalogProvisionedProductDetails pulumi.AnyOutput `pulumi:"serviceCatalogProvisionedProductDetails"`
	// Input ServiceCatalog Provisioning Details
	ServiceCatalogProvisioningDetails pulumi.AnyOutput `pulumi:"serviceCatalogProvisioningDetails"`
	// An array of key-value pairs to apply to this resource.
	Tags ProjectTagArrayOutput `pulumi:"tags"`
}

// NewProject registers a new resource with the given unique name, arguments, and options.
func NewProject(ctx *pulumi.Context,
	name string, args *ProjectArgs, opts ...pulumi.ResourceOption) (*Project, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProjectName == nil {
		return nil, errors.New("invalid value for required argument 'ProjectName'")
	}
	if args.ServiceCatalogProvisioningDetails == nil {
		return nil, errors.New("invalid value for required argument 'ServiceCatalogProvisioningDetails'")
	}
	var resource Project
	err := ctx.RegisterResource("aws-native:sagemaker:Project", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProject gets an existing Project resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProjectState, opts ...pulumi.ResourceOption) (*Project, error) {
	var resource Project
	err := ctx.ReadResource("aws-native:sagemaker:Project", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Project resources.
type projectState struct {
}

type ProjectState struct {
}

func (ProjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*projectState)(nil)).Elem()
}

type projectArgs struct {
	ProjectDescription *string `pulumi:"projectDescription"`
	ProjectName        string  `pulumi:"projectName"`
	// Input ServiceCatalog Provisioning Details
	ServiceCatalogProvisioningDetails interface{} `pulumi:"serviceCatalogProvisioningDetails"`
	// An array of key-value pairs to apply to this resource.
	Tags []ProjectTag `pulumi:"tags"`
}

// The set of arguments for constructing a Project resource.
type ProjectArgs struct {
	ProjectDescription pulumi.StringPtrInput
	ProjectName        pulumi.StringInput
	// Input ServiceCatalog Provisioning Details
	ServiceCatalogProvisioningDetails pulumi.Input
	// An array of key-value pairs to apply to this resource.
	Tags ProjectTagArrayInput
}

func (ProjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*projectArgs)(nil)).Elem()
}

type ProjectInput interface {
	pulumi.Input

	ToProjectOutput() ProjectOutput
	ToProjectOutputWithContext(ctx context.Context) ProjectOutput
}

func (*Project) ElementType() reflect.Type {
	return reflect.TypeOf((*Project)(nil))
}

func (i *Project) ToProjectOutput() ProjectOutput {
	return i.ToProjectOutputWithContext(context.Background())
}

func (i *Project) ToProjectOutputWithContext(ctx context.Context) ProjectOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProjectOutput)
}

type ProjectOutput struct{ *pulumi.OutputState }

func (ProjectOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Project)(nil))
}

func (o ProjectOutput) ToProjectOutput() ProjectOutput {
	return o
}

func (o ProjectOutput) ToProjectOutputWithContext(ctx context.Context) ProjectOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ProjectOutput{})
}
